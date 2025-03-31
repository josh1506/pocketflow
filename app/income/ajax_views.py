from datetime import datetime

from django.http import JsonResponse
from django.db.models import Sum

from .models import Income


def load_income_chart_data(request):
    incomes = Income.objects.filter(user=request.user)
    categories = ['SALARY', 'BUSINESS', 'INVESTMENT', 'FREELANCE', 'OTHER']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    current_year = datetime.now().year

    datasets = []

    for category in categories:
        monthly_data = []

        for month_index in range(1, 7):
            total_amount = incomes.filter(
                category=category,
                date__year=current_year,
                date__month=month_index
            ).aggregate(total=Sum('amount'))['total'] or 0

            monthly_data.append(total_amount)

        datasets.append({
            'name': category.capitalize(),
            'data': monthly_data
        })

    data = {
        'labels': months,
        'datasets': datasets
    }
    return JsonResponse(data)