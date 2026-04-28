from django.db import models
from packaging.tags import Tag


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    mark = models.BooleanField()
    tags = models.ManyToManyField(
        "Tags",
        related_name="tasks",
    )

    def __str__(self):
        return f"{self.content} - {self.datetime}"


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
