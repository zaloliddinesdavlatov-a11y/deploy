from django.urls import path
from .views import BookListApiView,BookCreateApiView,BookMixedApView,BookDeleteApiView,BookEditApiView,BookDetailApView

urlpatterns=[
    path('books/',BookListApiView.as_view(),name='book'),
    path('books/create/',BookCreateApiView.as_view(),name='book_create'),
    path('books/edit/',BookEditApiView.as_view(),name='book_edit'),
    path('books/delete/',BookDeleteApiView.as_view(),name='book_delete'),
    path('books/detail/',BookDetailApView.as_view(),name='book_detail'),
    path('books/mixed/',BookMixedApView.as_view(),name='book_mixed')
]