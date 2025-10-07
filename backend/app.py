import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
collection = client[os.getenv("MONGO_DB")][os.getenv("MONGO_COLLECTION")]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.4)

RAG_PROMPT = """
You are a movie expert. The user is looking for movie recommendations.
You MUST base your entire answer **only** on the movies provided in the context below.
Do not invent or add movies that are not in the context.
Summarize each one briefly and rank them as top 3 recommendations.
For each movie tell when was created <created_date>,the director of the movie <director> and a description of 20 words.
If the user talk to you about anything else that is not a movie recommendation you should say 'Sorry, I'm here just to recommend you movies'

Context (movies from the database):
{context}

User question:
{question}

Answer in this format:
My recommendation to what you are looking for is:
1. <movie 1> - Created by <director> in <created_date>. <description>
2. <movie 2> - Created by <director> in <created_date>. <description>
3. <movie 3> - Created by <director> in <created_date>. <description>

Then, list their vector similarity scores like this:
🎬 Top Results:
• <movie 1> — score: <score1>
• <movie 2> — score: <score2>
• <movie 3> — score: <score3>
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # 1️⃣ Generar embedding del query
    query_vector = embeddings.embed_query(user_input) 

    # 2️⃣ Vector search en MongoDB
    results = list(collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": query_vector,
                "path": "embedding",
                "numCandidates": 100,
                "limit": 3,
                "index": "vector_index"
            }
        },
        {
            "$project": {"_id": 0, "text": 1, "score": {"$meta": "vectorSearchScore"}}
        }
    ]))

    if not results:
        return jsonify({"response": "No matches found.", "matches": []})

    context = "\n".join([
        f"Movie: {r['text']}\nScore: {r['score']:.3f}"
        for r in results
    ])

    prompt = RAG_PROMPT.format(context=context, question=user_input)
    answer = llm.invoke(prompt)

    return jsonify({
        "response": answer.content.strip(),
    })

if __name__ == "__main__":
    app.run(debug=True)
