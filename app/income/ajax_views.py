from datetime import datetime, timedelta

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


def load_total_income_chart_data(request):
    incomes = Income.objects.filter(user=request.user)

    thirty_days = datetime.now() - timedelta(days=30)
    income_dates = incomes.filter(date__gte=thirty_days).values_list('date', flat=True).distinct().order_by('date')

    labels = [date.strftime('%Y-%m-%d') for date in income_dates]

    total_income_per_day = [
        incomes.filter(date=date).aggregate(total=Sum('amount'))['total'] or 0
        for date in income_dates
    ]

    data = {
        'labels': labels,
        'datasets': [
            {
                'name': 'Income',
                'data': total_income_per_day
            }
        ]
    }
    return JsonResponse(data)
