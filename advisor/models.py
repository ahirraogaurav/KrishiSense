from django.conf import settings
from django.db import models

class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="predictions")
    N = models.FloatField(); P = models.FloatField(); K = models.FloatField()
    temperature = models.FloatField(); humidity = models.FloatField()
    ph = models.FloatField(); rainfall = models.FloatField()
    crop = models.CharField(max_length=40)
    confidence = models.FloatField()
    top3 = models.JSONField(default=list)           # [[crop, probability], ...]
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def values(self):
        return {k: getattr(self, k) for k in ("N", "P", "K", "temperature", "humidity", "ph", "rainfall")}
