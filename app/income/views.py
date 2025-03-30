from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Income


class IncomeListView(ListView):
    model = Income
    template_name = "income/index.html"
    context_object_name = "incomes"
    paginate_by = 20
    ordering = ["-date"]
