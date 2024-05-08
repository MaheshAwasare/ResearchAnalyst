from crewai_tools import BaseTool
from tavily import TavilyClient
import os

from dotenv import load_dotenv
load_dotenv()
class SearchTool(BaseTool):
    name: str = "SearchTool"
    description: str = "This tool will search web using tavily and provide results"

    def _run(self, argument: str) -> str:
       tavily_api_key = os.getenv("TAVILY_API_KEY")
       tavily = TavilyClient(api_key=tavily_api_key)
       response = tavily.search(query=argument)
       print(f'response from tavily {response}')
       # Extracting information from the response
       results = response.get("results", [])
       extracted_info = ""
       for result in results:
           title = result.get("title", "")
           url = result.get("url", "")
           content = result.get("content", "")
           extracted_info += f"Title: {title}\nURL: {url}\nContent: {content}\n\n"


if __name__ == "__main__":
    query = input("Enter your search query: ")
    search_tool = SearchTool()
    result = search_tool.run(query)
    print(result)