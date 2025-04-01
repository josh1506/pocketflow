from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import TemplateView

from app.income.models import Income
from app.expenses.models import Expenses


class Overview(LoginRequiredMixin, TemplateView):
    template_name = 'overview/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        three_months_ago = datetime.now() - timedelta(days=90)

        total_income = Income.objects.filter(
            user=user,
            date__gte=three_months_ago
        ).aggregate(total=Sum('amount'))['total'] or 0

        total_expenses = Expenses.objects.filter(
            user=user,
            date__gte=three_months_ago
        ).aggregate(total=Sum('amount'))['total'] or 0

        context['chart_data'] = {
            'labels': ['Income', 'Expenses'],
            'datasets': [
                {
                    'name': 'Overview',
                    'data': [total_income, total_expenses]
                }
            ]
        }
        return context
