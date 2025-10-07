This project implements a Movie Recommendation Chatbot using a Retrieval-Augmented Generation (RAG) architecture.
The chatbot allows users to describe what kind of movie they want to watch (e.g., “a love story that transcends social classes”), and the system returns personalized movie suggestions using semantic search over a movie knowledge base.
It combines Flask as a backend API, MongoDB Atlas Vector Search for similarity queries, Google Gemini (Generative AI) for natural language generation, and an Angular frontend for the chat interface.


Architecture and Technologies Used: 
Frontend: Angular 17. It provides a simple, reactive chat interface where the user interacts with the AI model.

Backend: Flask REST API handling user requests, embedding generation, and retrieval from MongoDB.

Database: MongoDB Atlas with a vector index for fast similarity search on movie embeddings.

LLM: Gemini 2.5 Flash (Google Generative AI), used to generate human-like, concise movie recommendations based on the retrieved context.

Embeddings: models/embedding-001 from Google Generative AI to encode text into numerical vectors.

RAG pipeline: Combines document retrieval (vector search) + reasoning (Gemini response).


It was a very interesting mini project to work on, especially the part about prompt engineering.
Trying out different prompts and adjusting them to get the best response according to my own criteria was really enjoyable.
It was fun to see how you can make an AI say almost anything with just a 10-word prompt.

It was also a challenge since I had never worked with Python before. The previous classes before the project were very interesting and clear.
Personally, I’ve always found it difficult to truly understand how artificial intelligence works, but thanks to these lessons, I now have a much clearer understanding.

I still have a lot to learn, but I think this was a great start.
Thank you for giving us the opportunity to learn and taking the time to teach us about AI.
