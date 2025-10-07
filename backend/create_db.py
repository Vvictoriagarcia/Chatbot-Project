import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain.schema import Document
from pymongo import MongoClient

load_dotenv()

with open("data/movies.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_text(text)

docs = [Document(page_content=chunk) for chunk in chunks]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

client = MongoClient(os.getenv("MONGO_URI"))
collection = client[os.getenv("MONGO_DB")][os.getenv("MONGO_COLLECTION")]

db = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name="vector_index"
)

db.add_documents(docs)

print("Database created successfully")
