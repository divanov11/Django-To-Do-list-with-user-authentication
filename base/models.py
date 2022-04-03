from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    #description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    day1 = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)
    day8 = models.BooleanField(default=False)
    day9 = models.BooleanField(default=False)
    day10 = models.BooleanField(default=False)
    day11 = models.BooleanField(default=False)
    day12 = models.BooleanField(default=False)
    day13 = models.BooleanField(default=False)
    day14 = models.BooleanField(default=False)
    day15 = models.BooleanField(default=False)
    day16 = models.BooleanField(default=False)
    day17 = models.BooleanField(default=False)
    day18 = models.BooleanField(default=False)
    day19 = models.BooleanField(default=False)
    day20 = models.BooleanField(default=False)
    day21 = models.BooleanField(default=False)
    day22 = models.BooleanField(default=False)
    day23 = models.BooleanField(default=False)
    day24 = models.BooleanField(default=False)
    day25 = models.BooleanField(default=False)
    day26 = models.BooleanField(default=False)
    day27 = models.BooleanField(default=False)
    day28 = models.BooleanField(default=False)
    day29 = models.BooleanField(default=False)
    day30 = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

#['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day30']