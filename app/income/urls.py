from django.urls import path

from .views import IncomeListView, IncomeCreateView, IncomeDetailView, IncomeUpdateView, IncomeDeleteView

app_name = "income"

urlpatterns = [
    path('', IncomeListView.as_view(), name='list'),
    path('create/', IncomeCreateView.as_view(), name='create'),
    path('details/<str:income_id>/', IncomeDetailView.as_view(), name='details'),
    path('update/<str:income_id>/', IncomeUpdateView.as_view(), name='update'),
    path('delete/<str:income_id>/', IncomeDeleteView.as_view(), name='delete'),
]
