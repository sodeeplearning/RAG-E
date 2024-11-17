from langchain_community.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

from rage.config import llm_name, temperature, chunk_size, chunk_overlap, use_gpu, num_gpu


llm = Ollama(
    model=llm_name,
    temperature=temperature,
)

text_splitter = CharacterTextSplitter(separator="/n",
                                      chunk_size=chunk_size,
                                      chunk_overlap=chunk_overlap)

embeddings = HuggingFaceEmbeddings()
