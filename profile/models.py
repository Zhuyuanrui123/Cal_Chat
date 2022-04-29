from django.contrib.auth.models import User
from django.db import models

NICKNAME_CHOICES = (
    ('Poet', 'Poet'),
    ('Scale', 'Scale'),
    ('Gear', 'Gear'),
    ('Calc', 'Calc'),
    ('Beaker', 'Beaker'),
    ('Helix', 'Helix'),
    ('Mouse', 'Mouse'),
    ('Atom', 'Atom'),
    ('Alice', 'Alice'),
    ('Bob', 'Bob'),
    ('Jones', 'Jones'),
    ('Evans', 'Evans'),
    ('White', 'White'),
    ('Black', 'Black'),
    ('Jackson', 'Jackson'),
    ('Hill', 'Hill'),
    ('Clark', 'Clark'),
    ('Lee', 'Lee'),
    ('Mills', 'Mills'),
    ('Jerry', 'Jerry'),
    ('Tom', 'Tom'),
    ('Sam', 'Sam'),
    ('Amy', 'Amy'),
    ('Allen', 'Allen'),
    ('Anna', 'Anna'),
    ('Young', 'Young'),
    ('Ken', 'Ken'),
    ('Sara', 'Sara'),
    ('Shirley', 'Shirley'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=False)
    nickname = models.CharField(max_length=12, null=False, choices=NICKNAME_CHOICES)

    def __str__(self):
        return f'{self.user.username} - Anonymous {self.nickname}'
