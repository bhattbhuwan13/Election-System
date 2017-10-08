from django.shortcuts import get_object_or_404, render,redirect,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate,login
# from .models import Candidate
from django.views.generic import View,ListView, DetailView
from django.contrib.auth.models import User
from .forms import LoginForm,CandidateForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.template import loader

from registration.models import Candidate,Student,Party,College,Post,Election

def login(request):

    election_list = Election.objects.all()
    if request.method == 'POST':
        selected_student_name = (request.POST['student_name'])
        selected_student_citizenship = (request.POST['student_citizenship'])
        global selected_election_id
        selected_election_id = request.POST['election']
        # print(selected_election_id)
        # selected_election_id = int(selected_election.election_id)
        party_list = Party.objects.all().order_by('party_id')
        candidate_list = Candidate.objects.all().filter(election_id = selected_election_id ).order_by('party_id')
        student_list = Student.objects.all().filter()

        # return HttpResponse((selected_student_name.upper(),int(selected_student_citizenship)))

        for student in student_list:
            # print("Inside For Loop")
            # print ((student.name).replace(" ", ""))
            # print((selected_student_name.upper()).replace(" ", ""))
            if(student.name.upper().replace(" ", "") == selected_student_name.upper().replace(" ", "") and student.citizenship_no  == selected_student_citizenship) and student.has_voted == False:
                student.has_voted = True
                student.save()
                return render(request,'home/index.html', {'candidate_list': candidate_list,
                                                           'page_number': 0,
                                                           'party_list':party_list})
                # return HttpResponse((selected_student_name.upper(),selected_student_citizenship))
                # print("yes")
                # print(student.name.upper())
                # print(selected_student_name)
                # print(student.citizenship_no)
                # print(selected_student_citizenship)
                # break
            # else:
                # return redirect('home:log-in')
                # return login(request)
        else:
            return render(request,'home/log-in.html',{'election_list':election_list})

        # return render(request,'home/log-in.html')
        # print("NO")

    else:
        # print("GET Method")
        return render(request,'home/log-in.html',{'election_list':election_list})
        # return login(request)




@login_required(login_url='/registration/')
def result(request):
    candidate_list = Candidate.objects.all().order_by('party_id')
    party_list =Party.objects.all()
    return render(request, 'home/result.html', {'candidate_list': candidate_list,
                                                'party_list':party_list,})

class IndexView(generic.ListView):

    template_name = 'home/index.html'
    model = Candidate
    context_object_name = 'candidate_list'

    def get_queryset(self):
        return Candidate.objects.order_by('name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        # context['page_number'] = 0
        context['party_list'] = Party.objects.all().order_by('party_id')
        return context


def voted(request):
    global selected_election_id
    party_list = Party.objects.all().order_by('party_id')
    candidate_list = Candidate.objects.all().filter(election_id =selected_election_id ).order_by('party_id')
    # candidate_list = Candidate.objects.order_by('name')#all()
    page_number = request.POST['page']

    try:
        selected_candidate = Candidate.objects.get(pk = request.POST['candidate'])

    except(KeyError,Candidate.DoesNotExist):
        page_number = int(page_number)
        # page_number = request.POST['page']
        # return render(request, home:voted, {'candidate_list': candidate_list,
        #                                            'page_number': page_number,})

        return render(request,'home/index.html', {'candidate_list': candidate_list,
                                                   'page_number': page_number,
                                                   'party_list':party_list,})
    else:
        selected_candidate.votes += 1
        selected_candidate.save()

        # page_number = request.POST['page']
        page_number = ((int(page_number) + 1))
        if page_number == 5:
            # return render(request, 'home/index.html', {'candidate_list': candidate_list,
            #                                            'page_number': page_number,})
            page_number = 0
            return redirect('home:log-in')


        else:
            # page_number = ((int(page_number)+ 1))
            return render(request, 'home/index.html', {'candidate_list': candidate_list,
                                                       'page_number': page_number,
                                                       'party_list':party_list,})

        # return render(request,'home/index.html', {'candidate_list': candidate_list,
        #                                           'page_number': page_number,})


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])

            if user is not None:
                if user.is_active:
                    login(request)
                    candidates = Candidate.objects.order_by('name')
                    return render(request, 'home/dashboard.html',{'candidates':candidates,
                                                                 })
                else:
                    return HttpResponse('Account Disabled')

        else:
            return HttpResponse('Invalid Login')

    else:
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})
