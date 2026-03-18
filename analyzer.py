import os
from google import genai
from dotenv import load_dotenv, find_dotenv

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