from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.rag_services import embeddings

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

vector_db = Chroma(persist_directory="./vectorstore", embedding_function=embeddings)

retriever = vector_db.as_retriever()


def embed_docs(path):
    loader = PyPDFLoader(path)
    data = loader.load()
    splits = text_splitter.split_documents(data)
    vector_db.add_documents(splits)


def get_context(question: str) -> str:
    related_docs = vector_db.similarity_search(question)
    res = []
    for doc in related_docs:
        res.append(doc.page_content)
    return '\n'.join(res)


