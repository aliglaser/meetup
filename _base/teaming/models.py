import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# class Room( models.Model ):
#     id =models.PositiveIntegerField()
#     users =models.ManyToManyField(User)
#     user_limit =models.PositiveIntegerField()
#     tags =models.CharField( max_length =256)
#     age_limit =models.CharField( max_length =16 )
#     date =models.CharField( max_length =64 )
#     location =models.CharField( max_length =128 )
# 
# class TeamingUser( User ):
#     pass
