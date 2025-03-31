from django.urls import path

from .ajax_views import load_expenses_chart_data
from .views import ExpensesListView, ExpensesCreateView, ExpensesDetailView, ExpensesUpdateView, ExpensesDeleteView

app_name = "expenses"

ui_patterns = [
    path('', ExpensesListView.as_view(), name='list'),
    path('create/', ExpensesCreateView.as_view(), name='create'),
    path('details/<str:expense_id>/', ExpensesDetailView.as_view(), name='details'),
    path('update/<str:expense_id>/', ExpensesUpdateView.as_view(), name='update'),
    path('delete/<str:expense_id>/', ExpensesDeleteView.as_view(), name='delete'),
]


api_patterns = [
    path('chart-data/', load_expenses_chart_data, name='expenses_chart_data'),
]

urlpatterns = ui_patterns + api_patterns
