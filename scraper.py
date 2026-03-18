import os
from tavily import TavilyClient
from dotenv import load_dotenv, find_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(current_dir, '.env')

load_dotenv(find_dotenv())




TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def get_market_data(sector: str) -> str:
    """
    Searches the web using Tavily (an AI-optimized search engine) 
    to get deep context for our LLM.
    """
    print(f"Fetching AI-optimized data for: {sector}...")
    
    
    tavily = TavilyClient(api_key=TAVILY_API_KEY)

    if not TAVILY_API_KEY:
        raise ValueError("No TAVILY_API_KEY found. Check your .env file.")
    
    
    query = f"Latest market analysis and trade opportunities for {sector} sector in India"
    
    try:
        
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        
        
        formatted_data = f"Search Results for '{query}':\n\n"
        
        for result in response.get('results', []):
            formatted_data += f"Title: {result.get('title')}\n"
            
            formatted_data += f"Content: {result.get('content')}\n"
            formatted_data += f"Source: {result.get('url')}\n"
            formatted_data += "-" * 40 + "\n"
            
        return formatted_data
        
    except Exception as e:
        return f"Error fetching data from Tavily: {str(e)}"


if __name__ == "__main__":
    test_sector = "pharmaceuticals"
    scraped_info = get_market_data(test_sector)
    print("\n" + scraped_info)