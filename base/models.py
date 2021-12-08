from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    Mon = models.BooleanField(default=False)
    Tue = models.BooleanField(default=False)
    Wed = models.BooleanField(default=False)
    Thu = models.BooleanField(default=False)
    Fri = models.BooleanField(default=False)
    Sat = models.BooleanField(default=False)
    Sun = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        order_with_respect_to = 'user'
