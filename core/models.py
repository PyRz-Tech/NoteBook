from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Text(models.Model):
    SENTIMENT_CHOICES = [
        ('POSITIVE', 'Positive'),
        ('NEUTRAL', 'Neutral'),
        ('NEGATIVE', 'Negative')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='texts')
    text = models.TextField(max_length=1000, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, blank=True)
    sentiment_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment} ({self.date})"

    class Meta:
            ordering = ['-date']
