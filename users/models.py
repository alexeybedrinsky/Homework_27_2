from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    # Add any additional fields you need for your User model

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_payments')
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, related_name='user_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"UserPayment {self.id} for {self.course.title} by {self.user.email}"
