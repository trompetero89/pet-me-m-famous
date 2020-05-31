# Create your models here.
from django.db import models
from django.conf import settings
from django.urls import reverse
import misaka
from society.models import Society

from django.contrib.auth import get_user_model
User = get_user_model()


class Pet(models.Model):
    user = models.ForeignKey(User, related_name="petsposts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    pet_name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    animal_type = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    message_html = models.TextField(editable=False)
    society = models.ForeignKey(Society, related_name="petsposts",null=True, 
                                blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name

    def save(self, *args, **kwargs):
        self.pet_name = misaka.html(self.pet_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "petsposts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "pet_name"]