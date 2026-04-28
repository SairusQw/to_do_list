from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    mark = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        "Tag",
        related_name="tasks",
    )

    class Meta:
        ordering = ["deadline", "mark", "-datetime"]

    def __str__(self):
        return f"{self.content} - {self.datetime}"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
