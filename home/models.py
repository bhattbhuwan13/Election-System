from django.db import models
from django.utils.encoding import python_2_unicode_compatible

POST =(('PRE','President'),
       ('VPR','Vice-President'),
       ('SEC', 'Secretary'),
       ('MEM','Member'),
       ('TRE','Treasurer'))

PARTY = (('UML','CPN-UML'),('MAOIST','CPN - MAOIST'),('CONGRESS','NEPALI CONGRESS'),('INDEPENDENT','INDEPENDENT'),
         ('MPRF','Madhesi Pepole\'s Right Forum'))

# POST = ['President','Vice-President','Secretary','Treasurer','Member']

# Create your models here.
# class Voter(models.Model):
#     name = models.CharField(max_length=30)
#
# class Candidate(models.Model):
#     name = models.CharField(max_length=30)
#     post = models.CharField(max_length=3, choices=POST)
#     party = models.CharField(max_length=30,choices = PARTY)
#     votes = models.IntegerField(default=0)
#     image = models.FileField(upload_to='static/candidates/',null = True)
#
#     @python_2_unicode_compatible
#     def __str__(self):
#         return self.name
