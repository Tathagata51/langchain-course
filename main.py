import os
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from llm_util import llm_gemini, llm_groq
from langchain_tavily import TavilySearch
load_dotenv()


class Source(BaseModel):
    '''Schema for a source used by the agent'''
    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    '''Schema for the agent response with answer and sources'''
    answer: str = Field(description="The answer to the question")
    sources: List[Source] = Field(default_factory=list,
                                  description="The list of sources used to answer the question")


llm = llm_gemini
tools = [TavilySearch()]
simple_agent = create_agent(model=llm, tools=tools,
                            response_format=AgentResponse, system_prompt=(
                                "Answer the question using tools when needed. "
                                "Include a list of source URLs used to answer the question."
                            ))


def main():
    result = simple_agent.invoke(
        {"messages": [HumanMessage(content="What's the weather in Tokyo? Search the internet")]})
    print(result['structured_response'])


if __name__ == "__main__":
    main()
