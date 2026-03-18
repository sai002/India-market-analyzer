import os
from tavily import TavilyClient
from dotenv import load_dotenv, find_dotenv

# 1. Setup Environment
load_dotenv(find_dotenv())
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# 2. Initialize Client (Do this outside the function for better performance)
if not TAVILY_API_KEY:
    raise ValueError("No TAVILY_API_KEY found. Check your .env file.")

tavily = TavilyClient(api_key=TAVILY_API_KEY)

def get_market_data(sector):
    """
    Scrapes Indian market data for a specific sector using Tavily.
    """
    query = f"Latest market analysis and trade opportunities for {sector} sector in India 2026"
    
    try:
        # Perform the search
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        
        # DEBUG: Check if we actually got results
        results_list = response.get('results', [])
        print(f"DEBUG: Scraped {len(results_list)} links for {sector}")
        
        if not results_list:
            return f"No recent news found for the {sector} sector."

        # Format the data into a single string for Gemini
        formatted_data = f"Search Results for '{query}':\n\n"
        
        for result in results_list:
            formatted_data += f"Title: {result.get('title')}\n"
            formatted_data += f"Content: {result.get('content')}\n"
            formatted_data += f"Source: {result.get('url')}\n"
            formatted_data += "-" * 40 + "\n"
            
        return formatted_data
        
    except Exception as e:
        return f"Error fetching data from Tavily: {str(e)}"

if __name__ == "__main__":
    # Test script
    test_sector = "pharmaceuticals"
    scraped_info = get_market_data(test_sector)
    print("\n" + scraped_info)