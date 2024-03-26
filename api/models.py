# from django.db import models
# from .models import Patient, Service, Visit
#
#
# class Specialization(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Doctor(models.Model):
#     first_name = models.CharField(max_length=256)
#     last_name = models.CharField(max_length=256)
#     specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL,null=True)
#     date_of_birth = models.DateField()
#     contact_info = models.CharField(max_length=256)
#     patients = models.ManyToManyField(Patient)
#
#     def __str__(self):
#         return self.full_name
#
#     @property
#     def full_name(self):
#         return '%s %s' % (self.first_name, self.last_name)
#
#
# class Patient(models.Model):
#     first_name = models.CharField(max_length=256)
#     last_name = models.CharField(max_length=256)
#     date_of_birth = models.DateField()
#     medical_history = models.TextField()
#     gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
#     contact_info = models.CharField(max_length=256)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     visits = models.OneToManyField(Visit)
#
#     def __str__(self):
#         return self.full_name
#
#     @property
#     def full_name(self):
#         return '%s %s' % (self.first_name, self.last_name)
#
#
# class Visit(models.Model):
#     PLANNED = 'PLANNED'
#     COMPLETED = 'COMPLETED'
#     CANCELLED = 'CANCELLED'
#
#     STATUS_CHOICES = [
#         (PLANNED, PLANNED),
#         (COMPLETED, COMPLETED),
#         (CANCELLED, CANCELLED)
#     ]
#
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
#     visit_date_time = models.DateTimeField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#
#     def __str__(self):
#         return self.name
#
#
# class Service(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     visit = models.OneToOneField(Visit, on_delete=models.CASCADE)
#     notes = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name

from django.contrib.auth.models import User
from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    timestamp_start = models.DateTimeField()
    timestamp_end = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL, related_name='schedules')


class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(null=True, blank=True)
    schedule = models.ForeignKey(Schedule, null=True, on_delete=models.SET_NULL, related_name='visits')
    rating = models.PositiveIntegerField(default=0)
    rating_set = models.BooleanField()

    def __str__(self):
        return f"{self.doctor.full_name} - {self.patient.full_name} - {self.visit_date_time}"


class Notification(models.Model):
    NEW = 'NEW'
    READ = 'READ'
    ARCHIVED = 'ARCHIVED'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (READ, 'Read'),
        (ARCHIVED, 'Archived'),
    ]

    VISIT_CREATED = 'VISIT_CREATED'
    VISIT_CANCELLED = 'VISIT_CANCELLED'
    DOCTOR_DELETED = 'DOCTOR_DELETED'
    OTHER = 'OTHER'

    TYPE_CHOICES = [
        (VISIT_CREATED, 'Visit Created'),
        (VISIT_CANCELLED, 'Visit Cancelled'),
        (DOCTOR_DELETED, 'Doctor Deleted'),
        (OTHER, 'Other'),
    ]

    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient} : {self.message[:20]}"

    class Meta:
        ordering = ['-created_at']