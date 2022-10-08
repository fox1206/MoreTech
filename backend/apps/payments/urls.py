from django.urls import path

from . import views

urlpatterns = [
    # post - новая транзакция
    # get - все транзакции пользователя
    path('user-transactions/', views.TransactionView.as_view({'get': 'list', 'post': 'create'})),
    # детальная транзакция
    path('transaction/<int:pk>/', views.TransactionDetailView.as_view({'get': 'retrieve'})),
]