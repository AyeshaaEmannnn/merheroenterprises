from django.db import models

class Inquiry(models.Model):

    SUBJECT_CHOICES = [
        ("general", "General Inquiry"),
        ("quote", "Request a Quote"),
        ("custom", "Custom Project"),
        ("partnership", "Partnership"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"