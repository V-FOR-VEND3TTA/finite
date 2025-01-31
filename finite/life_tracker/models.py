from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    expected_lifespan = models.IntegerField(default=80)  # Default to 80 years

    def weeks_lived(self):
        today = date.today()
        birth_date = self.birthdate
        weeks = (today - birth_date).days // 7
        return weeks

    def weeks_remaining(self):
        total_weeks = self.expected_lifespan * 52
        return total_weeks - self.weeks_lived()

    def life_completion_percentage(self):
        total_weeks = self.expected_lifespan * 52
        return (self.weeks_lived() / total_weeks) * 100

    def __str__(self):
        return f"{self.user.username}'s Profile"
