from django.urls import path

from app.overview.views import Overview

app_name = 'overview'

urlpatterns = [
    path('', Overview.as_view(), name='dashboard'),
]
