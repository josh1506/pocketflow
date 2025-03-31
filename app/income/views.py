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


class IncomeDetailView(DetailView):
    model = Income
    template_name = "income/details.html"
    context_object_name = "income"
    pk_url_kwarg = "income_id"


class IncomeUpdateView(UpdateView):
    model = Income
    template_name = "income/update.html"
    context_object_name = "income"
    form_class = IncomeForm
    pk_url_kwarg = "income_id"

    def get_success_url(self):
        return reverse_lazy("income:details", kwargs={"income_id": self.object.id})


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "income/delete.html"
    context_object_name = "income"
    pk_url_kwarg = "income_id"
    success_url = reverse_lazy("income:list")
