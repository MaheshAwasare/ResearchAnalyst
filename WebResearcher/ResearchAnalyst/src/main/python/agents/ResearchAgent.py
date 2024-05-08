import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms.ollama import Ollama

llama3 = Ollama(model='phi:latest')


def websearchanalyst():
    return Agent(
        role='The Best Web Search expert',
        goal="""Based on search results from web get the best results out""",
        backstory="""The most seasoned web search expert whoc takes out relvant content from web""",
        verbose=True,
        tools=[
            BrowserTools.scrape_and_summarize_website,
            SearchTools.search_internet,
            CalculatorTools.calculate,
            SECTools.search_10q,
            SECTools.search_10k
        ]
    )


class ResearchAgent():
    pass
