1. Clone the repository
2. Go to backend (cd backend)
3. Run the command `python3 -m venv venv`
4. Run the command `source venv/bin/activate`
5. Install the requirements with `pip install -r requirements.txt`
6. Add .env with the variables in the .env.default
7. Create a free cluster in Atlas
8. Add the connection string to the .env variables
9. Run the file python create_db with the command `create_db.py`
10. Create a vector search with an index as above
11. Check you have the movies with their embeddings on Atlas
12. Once you have everything run `python app.py`

```
{
  "fields": [
    {
      "numDimensions": 768,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}
```
