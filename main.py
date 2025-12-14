import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from llm_util import llm_gemini, llm_groq
from langchain_tavily import TavilySearch
load_dotenv()


llm = llm_gemini
tools = [TavilySearch()]
simple_agent = create_agent(model=llm, tools=tools)


def main():
    result = simple_agent.invoke(
        {"messages": [HumanMessage(content="What's the weather in Tokyo? Search the internet")]})
    print(result)


if __name__ == "__main__":
    main()
