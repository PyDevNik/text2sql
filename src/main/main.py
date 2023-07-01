"""
Main file in package
"""

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from converter.text2sql import text2sql
from converter.config import CLICKHOUSE_URL

DB_URL = CLICKHOUSE_URL.format(
    hostname = "x7m875xoon.europe-west4.gcp.clickhouse.cloud",
    port = 8443,
    username = "default",
    password = "vzO9~.wflbn8B",
)

question = input("Prompt: ")

result = text2sql(DB_URL, question)

print(result)