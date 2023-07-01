# Natural Language to SQL Query Converter

This module provides functionality for converting natural language queries into SQL queries.

## Installation

To use this module, you need to have the following prerequisites:

- Python 3.x
- langchain library

You can install the langchain library using pip:

```shell
pip install langchain
```

## Usage

Here's an example of how to use the `text2sql` function provided by this module:

```python
from .config import LLM, PROMPT
from langchain import SQLDatabase, SQLDatabaseChain
from converter.text2sql import text2sql

# Specify the database URL
db_url = "your_database_url"

# User input in natural language
user_input = "your_question"

# Convert natural language to SQL query
result = text2sql(db_url, user_input)

print("SQL Query:", result)
```

Make sure to replace `"your_database_url"` with the actual URL of your database and `"your_question"` with the user's input.

The `text2sql` function takes a database URL and a user input string as parameters. It converts the natural language input into an SQL query using the langchain library and returns the resulting SQL query as a string.

Please note that you need to import the necessary modules and configure the `OPENAI_KEY` variable before using the `text2sql` function.
