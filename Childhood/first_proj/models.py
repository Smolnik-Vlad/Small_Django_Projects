from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, help_text="period of your life")

    def __str__(self):
        return f"{self.id}. {self.title}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f"id: {self.id}, title: {self.title}, connection: {self.event.title}"
