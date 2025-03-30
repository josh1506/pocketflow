from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Expenses


class ExpensesListView(ListView):
    model = Expenses
    template_name = "expenses/index.html"
    context_object_name = "expenses"
    paginate_by = 20
    ordering = ["-date"]
