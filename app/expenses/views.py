from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ExpensesForm
from .models import Expenses


class ExpensesListView(ListView):
    model = Expenses
    template_name = "expenses/index.html"
    context_object_name = "expenses"
    paginate_by = 20
    ordering = ["-date"]


class ExpensesCreateView(CreateView):
    model = Expenses
    template_name = "expenses/create.html"
    form_class = ExpensesForm
    success_url = reverse_lazy("expenses:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpensesDetailView(DetailView):
    model = Expenses
    template_name = "expenses/details.html"
    context_object_name = "expenses"
    pk_url_kwarg = "expense_id"
