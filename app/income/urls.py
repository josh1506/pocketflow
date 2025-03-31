from django.urls import path

from .views import IncomeListView, IncomeCreateView, IncomeDetailView, IncomeUpdateView, IncomeDeleteView
from .ajax_views import load_income_chart_data, load_total_income_chart_data

app_name = "income"

ui_patterns = [
    path('', IncomeListView.as_view(), name='list'),
    path('create/', IncomeCreateView.as_view(), name='create'),
    path('details/<str:income_id>/', IncomeDetailView.as_view(), name='details'),
    path('update/<str:income_id>/', IncomeUpdateView.as_view(), name='update'),
    path('delete/<str:income_id>/', IncomeDeleteView.as_view(), name='delete'),
]

api_patterns = [
    path("chart-data/", load_income_chart_data, name="income_chart_data"),
    path("chart-data/total/", load_total_income_chart_data, name="total_income_chart_data")
]

urlpatterns = ui_patterns + api_patterns
