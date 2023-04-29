import os
from uuid import uuid4

from django.db import models


def upload(instance, filename):
    return "/".join([f"employee/resume", f"{str(uuid4())}{os.path.splitext(filename)[1]}"])

class Employee(models.Model):
    """Model of an employee"""

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    first_name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, db_index=True)
    gender = models.CharField(
        max_length=6, choices=gender_choices, null=False, blank=False
    )
    # removed because of storage dependency
    # resume = models.FileField(upload_to=upload)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
