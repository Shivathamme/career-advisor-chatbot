from llm import llm
from prompt import career_prompt

from langchain_core.output_parsers import StrOutputParser

chain = (career_prompt | llm |StrOutputParser())