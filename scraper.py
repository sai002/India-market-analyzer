import os
from tavily import TavilyClient
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


if not TAVILY_API_KEY:
    raise ValueError("No TAVILY_API_KEY found. Check your .env file.")

tavily = TavilyClient(api_key=TAVILY_API_KEY)

def get_market_data(sector: str) -> str:
    """
    Scrapes Indian market data for a specific sector using Tavily.
    """
    print(f"Fetching AI-optimized data for: {sector}...")
    
    
    query = f"Latest market analysis and trade opportunities for {sector} sector in India 2026"
    
    try:
        
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        
        
        results_list = response.get('results', [])
        print(f"DEBUG: Scraped {len(results_list)} links for {sector}")
        
        
        if not results_list:
            return ""

        
        formatted_data = f"Search Results for '{query}':\n\n"
        
        for result in results_list:
            formatted_data += f"Title: {result.get('title')}\n"
            formatted_data += f"Content: {result.get('content')}\n"
            formatted_data += f"Source: {result.get('url')}\n"
            formatted_data += "-" * 40 + "\n"
            
        return formatted_data
        
    except Exception as e:
        print(f"Scraper Error: {e}")
        return ""

if __name__ == "__main__":
    # Test script
    test_sector = "pharmaceuticals"
    scraped_info = get_market_data(test_sector)
    print("\n" + scraped_info)