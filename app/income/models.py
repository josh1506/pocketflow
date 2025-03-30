import uuid

from django.contrib.auth.models import User
from django.db import models


class Income(models.Model):
    CATEGORY_CHOICES = [
        ('SALARY', 'Salary'),
        ('BUSINESS', 'Business'),
        ('INVESTMENT', 'Investment'),
        ('FREELANCE', 'Freelance'),
        ('OTHER', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
