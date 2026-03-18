import os
from google import genai
from dotenv import load_dotenv, find_dotenv

<<<<<<< HEAD

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print(f"Debug (Analyzer) - Did we load the Gemini key?: {'YES' if GEMINI_API_KEY else 'NO'}")

if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found. Check your .env file.")


client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_market_data(sector: str, scraped_text: str) -> str:
    """
    Sends the scraped market data to Gemini and asks for a structured 
    Markdown report on trade opportunities.
    """
    
    prompt = f"""
    You are an expert market analyst focusing on the Indian market.
    I will provide you with recent news and data snippets regarding the '{sector}' sector.
    
    Based ONLY on the provided data, generate a structured market analysis report highlighting trade opportunities.
    
    Format the output strictly in Markdown with the following sections:
    # Market Analysis Report: {sector.capitalize()} Sector (India)
    ## Executive Summary
    ## Current Market Trends
    ## Key Trade Opportunities
    ## Potential Risks/Challenges
    
    Here is the data:
    {scraped_text}
    """
    
    try:
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"## Error generating report\n\nThe AI analysis failed: {str(e)}"


if __name__ == "__main__":
    print("\nTesting the AI Analyzer...")
    
    test_sector = "pharmaceuticals"
    test_data = "The Indian pharma sector is seeing a 20% rise in generic drug exports to Africa. Supply chain costs have decreased slightly due to new tech."
    
    print("Sending mock data to Gemini (this might take a few seconds)...\n")
    report = analyze_market_data(test_sector, test_data)
    print(report)
=======
load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found.")

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_market_data(sector, scraped_text):
    if not scraped_text:
        return "## No Data Found\n\nCould not find recent news for this sector. Please try a different keyword."

    prompt = f"""
    You are an expert Indian market analyst. Based on this data:
    {scraped_text}
    
    Generate a Markdown report for the {sector} sector with:
    # Market Analysis: {sector.capitalize()}
    ## Executive Summary
    ## Trends
    ## Trade Opportunities
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        return response.text if response.text else "AI returned empty content."
    except Exception as e:
        return f"AI Error: {str(e)}"

if __name__ == "__main__":
    print(analyze_market_data("test", "India's tech sector is growing."))
>>>>>>> temp-branch
