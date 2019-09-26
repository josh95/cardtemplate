from django.db import models


class Personality(models.Model):
    def __str__(self):
        return self.name
    personality_id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    persona = models.CharField(max_length=20)
    active_value = models.IntegerField(default=0)
    inactive_value = models.IntegerField(default=0)
    inactive_used = models.BooleanField(default=True)
    effect_text = models.CharField(max_length=400)
    flavour_text = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


class Clothing(models.Model):
    def __str__(self):
        return self.name
    clothing_id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    claim_text = models.CharField(max_length=200)
    special_text = models.CharField(max_length=200)
    lp = models.IntegerField(default=0)
    min_adv = models.IntegerField(default=0)
    image = models.CharField(max_length=200)
