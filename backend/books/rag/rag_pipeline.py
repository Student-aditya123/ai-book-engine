import os
import sys
import django

# Django setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from books.models import Book

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


# 🔹 STEP 1: Build Vector Store
def build_vector_store():
    print("📚 Loading books from DB...")

    books = Book.objects.all()
    texts = []

    for book in books:
        content = f"Title: {book.title}\nDescription: {book.description}"
        texts.append(content)

    print("🔄 Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(texts, embeddings)

    db.save_local("faiss_index")

    print("✅ FAISS vector DB created!")


# 🔹 STEP 2: Ask Question
def ask_question(query):
    print("🔍 Loading vector DB...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
               "faiss_index",
               embeddings,
               allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    print("📖 Retrieved context")

    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔥 HuggingFace LLM (lightweight)
    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-small",
        max_length=200
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    answer = llm(prompt)

    return answer