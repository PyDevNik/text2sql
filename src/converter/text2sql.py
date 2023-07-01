"""
Module for converting Natural Language to SQL Query
"""

from .config import LLM, PROMPT
from langchain import SQLDatabase, SQLDatabaseChain

def text2sql(db_url: str, input: str):
    """
    Simple function to convert Natural Language to SQL Queries
    :param db: DB URL
    :param input: User Input
    """
    database = SQLDatabase.from_uri(db_url)
    db_chain = SQLDatabaseChain.from_llm(
        llm=LLM, 
        database=database, 
        prompt=PROMPT, 
        verbose=True, 
        use_query_checker=True, 
        return_intermediate_steps=True
        )
    
    result = db_chain(input)[2]["query"]
    return result