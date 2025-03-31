from django.urls import path

from .views import IncomeListView, IncomeCreateView, IncomeDetailView

app_name = "income"

urlpatterns = [
    path('', IncomeListView.as_view(), name='list'),
    path('create/', IncomeCreateView.as_view(), name='create'),
    path('details/<str:income_id>/', IncomeDetailView.as_view(), name='details'),
]
