from django.db import models

# Define class XXModel(models.Model) -> python manage.py makemigrations learning_logs -> generate migrations/0001_initial.py
# -> python manage.py migrate -> modify DB

# Whenever we want to modify the data that Learning Log manages, we’ll follow these three steps: modify models.py, call makemigrations on
# learning_logs, and tell Django to migrate the project.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    # on deleting topic, all the entry associated with this topic will be deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
