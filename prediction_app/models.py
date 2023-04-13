from django.db import models
from django.conf import settings
from django.utils import timezone


class DiabetesPrediction(models.Model):
    age = models.IntegerField()
    sex = models.FloatField()
    bmi = models.FloatField()
    bp = models.FloatField()
    tc = models.FloatField()
    ldl = models.FloatField()
    hdl = models.FloatField()
    tch = models.FloatField()
    ltg = models.FloatField()
    glucose = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Diabetes result for {self.user}"
