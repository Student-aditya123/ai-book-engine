from django.urls import path
from .views import book_list, book_detail, ask_ai

urlpatterns = [
    path('books/', book_list),
    path('books/<int:pk>/', book_detail),
    path('ask/', ask_ai),
]