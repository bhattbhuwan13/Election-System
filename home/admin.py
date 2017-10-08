from django.contrib import admin
# from .models import Voter,Candidate
# # Register your models here.
#
# admin.site.register(Voter)
# admin.site.register(Candidate)

from registration.models import Student,College,Election,Party,Post,Candidate,WinnerReport

admin.site.register(Student)
admin.site.register(College)
admin.site.register(Election)
admin.site.register(Party)
admin.site.register(Post)
admin.site.register(Candidate)
admin.site.register(WinnerReport)
