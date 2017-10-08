from django import forms
# from .models import Candidate

from registration.models import Candidate,Student,Party,College,Post,Election

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class CandidateForm(forms.ModelForm):
#     class Meta:
#         model = Candidate
#         exclude = ['votes']


class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['voter_id','name','sex','dob','disability','college_id','college_name','citizenship_no','photo']


class CandidateForm(forms.ModelForm):
	class Meta:
		model=Candidate
		fields=['voter_id','party_id','post','college_id','candidate_id','election_id']


class PartyForm (forms.ModelForm):
	class Meta:
		model=Party
		fields=['name','registration_no','symbol']


class CollegeForm (forms.ModelForm):
	class Meta:
		model=College
		fields=['name','location','registration_no']


class PostForm (forms.ModelForm):
	class Meta:
		model=Post
		fields=['post_name','post_election']

class ElectionForm (forms.ModelForm):
	class Meta:
		model=Election
		fields=['name','year']
