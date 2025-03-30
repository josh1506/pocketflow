from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import IncomeForm
from .models import Income


class IncomeListView(ListView):
    model = Income
    template_name = "income/index.html"
    context_object_name = "incomes"
    paginate_by = 20
    ordering = ["-date"]


class IncomeCreateView(CreateView):
    model = Income
    template_name = "income/create.html"
    form_class = IncomeForm
    success_url = reverse_lazy("income:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
