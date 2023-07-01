"""
Main configuration file for text2sql converter
"""

from langchain import OpenAI
from langchain.prompts.prompt import PromptTemplate

CLICKHOUSE_URL = "clickhouse://{hostname}:{port}/?user={username}:{password}"

OPENAI_KEY = "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"

_DEFAULT_TEMPLATE = """\
Given an input question, create a syntactically correct {query} query to run.
Use the following format:

Question: "Question here"
Query: "SQL Query to run"

Only use the following tables:
{table_info}

Question: {input}
"""

PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "query"], template=_DEFAULT_TEMPLATE
)

LLM = OpenAI(openai_api_key=OPENAI_KEY,temperature=0)
