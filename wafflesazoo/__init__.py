from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

TRACKED_STATS=["Hunger", "Sleepiness", "Loneliness", "Happiness"]
class Status(models.Model):
	need = models.CharField(max_length=10, choices=TRACKED_STATS, default='Hunger')
	fulfillment = models.IntegerField(
        default=50,
        validators=[MaxValueValidator(100), MinValueValidator(1)])

MOODS = ["Hungry", "Tired", "Lonely", "Playful", "Content", "Annoyed", "Vengeful"]
class Mood(models.Model):
	mood = models.CharField(max_length=8, choices=MOODS, default='Content')

LOCATIONS = ["Deep Goodale", "Shallow Goodale", "Glounge", "Bemis", "Walounge", "Shallow Walcott", "Deep Walcott"]
class Cur_Location(models.Model):
	cur_loc = models.CharField(max_length=15, choices=LOCATIONS, default='Deep Goodale')

class Des_Location(models.Model):
	des_loc = models.CharField(max_length=15, choices=LOCATIONS, default='Deep Goodale')