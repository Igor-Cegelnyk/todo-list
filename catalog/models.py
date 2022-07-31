from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(
        help_text=
        "Please use the following format: "
        "<em>YYYY-MM-DD hh:mm:ss</em>.",
        blank=True,
        null=True,
    )
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-datetime"]

    def __str__(self):
        return \
            f"{self.content} " \
            f"(created: {self.datetime}; " \
            f"deadline: {self.deadline}; " \
            f"status:{self.status}) " \
            f"Tags: {self.tags}"
