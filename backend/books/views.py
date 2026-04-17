from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404
from books.rag.rag_pipeline import ask_question


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def ask_ai(request):
    query = request.data.get("question")

    if not query:
        return Response({"error": "No question provided"}, status=400)

    # ✅ FAST MOCK RESPONSE (NO AI CALL)
    return Response({
        "question": query,
        "answer": "This book provides an engaging story and insightful content. (Demo AI response)"
    })