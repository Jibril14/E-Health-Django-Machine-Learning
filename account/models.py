from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = 'male', ('male')
        FEMALE = 'female', ('female')
        OTHERS = 'others', ('others')

    class Role(models.TextChoices):
        DOCTOR = 'doctor', ('doctor')
        PATIENT = 'patient', ('patient')

    base_role = Role.PATIENT
    gender = models.CharField(max_length=10, choices=Gender.choices, default=Gender.MALE)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.PATIENT)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    # At creation we assign a base role
    def save(self, *args, **kwargs):
        if not self.pk:  
            self.role = self.base_role
            return super().save(*args, **kwargs)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-date_joined']
        default_permissions = ('add', 'change', 'view', )
        

    def __str_(self):
        return self.username



class PatientManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.PATIENT)


class Patient(User):
    base_role = User.Role.PATIENT
    patient = PatientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Patient User"


class DoctorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.DOCTOR)


class Doctor(User):
    base_role = User.Role.DOCTOR
    doctor = DoctorManager()

    class Meta:
        proxy = True

    def welcome(slef):
        return "Doctor User"
