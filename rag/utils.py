from langchain_community.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

from config import *


llm = Ollama(
    model="owl/t-lite:latest",
    temperature=temperature,
)

text_splitter = CharacterTextSplitter(separator="/n",
                                      chunk_size=chunk_size,
                                      chunk_overlap=chunk_overlap)

embeddings = HuggingFaceEmbeddings()
