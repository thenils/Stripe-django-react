from django.db import models
from django.contrib.auth.models import User


def get_default_json_value_features():
    return {'features': []}


class Subscription(models.Model):
    type = models.CharField(max_length=200)
    price = models.FloatField()
    subscription_id = models.CharField(max_length=255)
    # feature = models.JSONField(default=get_default_json_value_features)

    def __str__(self):
        return self.type


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
