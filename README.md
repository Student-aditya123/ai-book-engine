# 🚀 AI Book Intelligence Platform (RAG Powered)

An AI-powered full-stack web application that intelligently processes book data and enables contextual question answering using Retrieval-Augmented Generation (RAG).

---

## 🌟 Features

- 📚 Automated Book Scraping using Selenium
- 🧠 AI-Powered Insights Generation
- 🔍 Semantic Search with FAISS Vector DB
- 🤖 Context-Aware Q&A (RAG Pipeline)
- ⚡ Fast API with Django REST Framework
- 🎨 Modern UI with React + Tailwind CSS

---

## 🧠 AI Capabilities

- 📖 Book Summary Generation
- 🧬 Semantic Similarity Search
- 🤝 Intelligent Recommendations
- 💬 Context-Based Question Answering

---

## 🏗️ System Architecture
User Query → API → RAG Pipeline → FAISS → Context Retrieval → LLM → Response

---
## ⚠️ Note

Due to system/network constraints, a lightweight AI model is used for demo.
Full RAG pipeline is implemented and can be scaled with higher compute resources.

---
### ⚡ Optimizations
🚀 Lightweight model used for faster inference
💾 FAISS for efficient similarity search
🔄 Duplicate handling in scraping
⚙️ Modular architecture
⚠️ Note

## ⚙️ Tech Stack

### Backend
- Django REST Framework
- Selenium (Web Scraping)
- FAISS (Vector Database)

### AI/ML
- HuggingFace Transformers
- Sentence Transformers (Embeddings)
- RAG Architecture

### Frontend
- React.js
- Tailwind CSS
- Axios

---

## 📸 Screenshots
 
![alt text](<Screenshot 2026-04-17 180825.png>)
---
![alt text](<Screenshot 2026-04-17 180900-1.png>)
---
![alt text](<Screenshot 2026-04-17 180921.png>)
---
![alt text](<Screenshot 2026-04-17 180847.png>)
---

## 🚀 Setup Instructions
  ```bash
### 1. Clone Repo
git clone https://github.com/your-username/ai-book-engine.git
cd ai-book-engine

## 2. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 3. Run Scraper
python books/scraper/scrape_books.py

## 4. Build Vector DB
python manage.py shell
from books.rag.rag_pipeline import build_vector_store
build_vector_store()

## 5. Frontend Setup
cd frontend
npm install
npm start

## API Endpoints
📚 Get Books
GET /api/books/
🤖 Ask AI
POST /api/ask/

Request Body:

{
  "question": "Recommend books like this"
}


🧪 Sample Q&A

Q: What is this book about?
A: The book explores...


