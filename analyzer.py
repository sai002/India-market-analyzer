import os
from google import genai
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
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
    
    if not scraped_text or len(scraped_text) < 20:
        return "## No Data Found\n\nCould not find sufficient recent news for this sector. Please try a different keyword."

    
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
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text if response.text else "AI returned empty content. Safety filters may have blocked the response."
        
    except Exception as e:
        return f"## Error generating report\n\nThe AI analysis failed: {str(e)}"

if __name__ == "__main__":
    print("\nTesting the AI Analyzer...")
    test_sector = "pharmaceuticals"
    test_data = "The Indian pharma sector is seeing a 20% rise in generic drug exports to Africa. Supply chain costs have decreased slightly due to new tech."
    
    print("Sending mock data to Gemini (this might take a few seconds)...\n")
    report = analyze_market_data(test_sector, test_data)
    print(report)