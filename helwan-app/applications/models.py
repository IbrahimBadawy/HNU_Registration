# 📁 backend/applications/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)


class StudentApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    step_completed = models.IntegerField(default=1)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "قيد المراجعة"),
            ("accepted", "مقبول"),
            ("rejected", "مرفوض"),
        ],
        default="pending",
    )
    rejection_reason = models.TextField(blank=True, null=True)

    # بيانات شخصية
    full_name_ar = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255)
    national_id = models.CharField(max_length=14)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    governorate = models.CharField(max_length=100)

    # أكاديمي
    certificate_type = models.CharField(max_length=100)
    grad_year = models.PositiveIntegerField()
    total_score = models.FloatField()
    percentage = models.FloatField()
    desired_college = models.CharField(max_length=100)

    # ولي الأمر
    guardian_name = models.CharField(max_length=255)
    guardian_relation = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=20)
    guardian_email = models.EmailField(blank=True, null=True)
    guardian_job = models.CharField(max_length=100)

    # صحي
    illnesses = models.TextField(blank=True)
    disabilities = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=255)


class UploadedDocument(models.Model):
    application = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")


class Payment(models.Model):
    application = models.OneToOneField(StudentApplication, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=50, default="pending")
    payment_date = models.DateTimeField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)


class ApplicationReview(models.Model):
    application = models.ForeignKey(StudentApplication, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10)  # accepted / rejected
    rejection_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
