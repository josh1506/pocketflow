from datetime import datetime, timedelta

from django.db.models import Sum
from django.http import JsonResponse

from .models import Expenses


def load_expenses_chart_data(request):
    expenses = Expenses.objects.filter(user=request.user)
    categories = ['FOOD', 'RENT', 'BILLS', 'ENTERTAINMENT', 'TRAVEL', 'HEALTH', 'OTHER']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    current_year = datetime.now().year

    datasets = []

    for category in categories:
        monthly_data = []

        for month_index in range(1, 7):
            total_amount = expenses.filter(
                category=category,
                date__year=current_year,
                date__month=month_index,
            ).aggregate(Sum('amount'))["amount__sum"] or 0

            monthly_data.append(total_amount)

        datasets.append({
            'name': category,
            'data': monthly_data,
        })

    data = {
        'labels': months,
        'datasets': datasets,
    }
    return JsonResponse(data)


def load_total_expenses_chart_data(request):
    expenses = Expenses.objects.filter(user=request.user)

    thirty_days = datetime.now() - timedelta(days=30)
    expenses_dates = expenses.filter(date__gte=thirty_days).values_list('date', flat=True).distinct().order_by('date')

    labels = [date.strftime('%Y-%m-%d') for date in expenses_dates]

    total_expenses_per_day = [
        expenses.filter(date=date).aggregate(total=Sum('amount'))['total'] or 0
        for date in expenses_dates
    ]

    data = {
        'labels': labels,
        'datasets': [
            {
                'name': 'Expenses',
                'data': total_expenses_per_day
            }
        ]
    }
    return JsonResponse(data)
