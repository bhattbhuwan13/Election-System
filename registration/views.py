from operator import itemgetter, attrgetter

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from .fusioncharts import FusionCharts



from home.forms import CandidateForm,StudentForm,PartyForm,CollegeForm,PostForm,ElectionForm
from .models import Candidate,Student,Party,College,Post,Election

from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def homeView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Invalid Login')

        cd = form.cleaned_data
        user = authenticate(request,username = cd['username'],password = cd['password'])

        if user is not None:
            if user.is_active:
                login(request,user)
                # candidates = Candidate.objects.order_by('name')
                return render(request, 'registration/reg-links.html',)
            else:
                return HttpResponse('Account Disabled')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def register(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Invalid Login')

        cd = form.cleaned_data
        user = authenticate(request,username = cd['username'],password = cd['password'])

        if user is not None:
            if user.is_active:
                login(request,user)
                # candidates = Candidate.objects.order_by('name')
                return render(request, 'registration/reg-links.html',)
            else:
                return HttpResponse('Account Disabled')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

# @login_required
def simple(request):
    return render(request,'registration/reg-links.html')


# The Create Views

class CandidateCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('registration:homeView')
    # login_url = reverse_lazy('registration:register')
    model = Candidate
    # fields = '__all__'
    form_class = CandidateForm

    template_name = 'registration/candidate_form.html'
    success_url = reverse_lazy('registration:candidate_list')


class ElectionCreate(LoginRequiredMixin,CreateView):
    login_url = 'registration/'
    # login_url = 'registration/register'
    model = Election
    # fields = '__all__'
    form_class = ElectionForm

    template_name = 'registration/election_form.html'
    success_url = reverse_lazy('registration:election_list')


class PartyCreate(LoginRequiredMixin,CreateView):
    login_url = 'registration/'
    # login_url = 'registration/'
    model = Party
    # fields = '__all__'
    form_class = PartyForm

    template_name = 'registration/party_form.html'
    # success_url = reverse_lazy('registration:party_list')

class PostCreate(LoginRequiredMixin,CreateView):
    login_url = 'registration/'
    model = Post
    # fields = '__all__'
    form_class = PostForm

    template_name = 'registration/post_form.html'
    success_url = reverse_lazy('registration:post_list')

class CollegeCreate(LoginRequiredMixin,CreateView):
    login_url = 'registration/'
    model = College
    # fields = '__all__'
    form_class = CollegeForm

    template_name = 'registration/college_form.html'
    success_url = reverse_lazy('registration:college_list')

class StudentCreate(LoginRequiredMixin,CreateView):
    login_url = 'registration/'
    model = Student
    # fields = '__all__'
    form_class = StudentForm

    template_name = 'registration/student_form.html'
    success_url = reverse_lazy('registration:student_list')



# Views for updating the models are here

class CandidateUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = Candidate
    fields = '__all__'

    template_name = 'registration/candidate_update.html'
    success_url = reverse_lazy('registration:candidate_list')

class ElectionUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = Election
    fields = '__all__'

    template_name = 'registration/election_update.html'
    success_url = reverse_lazy('registration:election_list')


class PartyUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = Party
    fields = '__all__'

    template_name = 'registration/party_update.html'
    success_url = reverse_lazy('registration:party_list')

class PostUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = Post
    fields = '__all__'

    template_name = 'registration/post_update.html'
    success_url = reverse_lazy('registration:post_list')

class CollegeUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = College
    fields = '__all__'

    template_name = 'registration/college_update.html'
    success_url = reverse_lazy('registration:college_list')


class StudentUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'registration/'
    model = Student
    fields = '__all__'

    template_name = 'registration/party_update.html'
    success_url = reverse_lazy('registration:student_list')


# Views for reading the data from the model

class CandidateList(ListView):
    model = Candidate
    context_object_name = 'candidate_list'

    def get_queryset(self):
        return Candidate.objects.all()

class ElectionList(ListView):
    model = Election
    context_object_name = 'election_list'

    def get_queryset(self):
        return Election.objects.all()

class PartyList(ListView):
    model = Party
    context_object_name = 'party_list'

    def get_queryset(self):
        return Party.objects.all()

class PostList(ListView):
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()

class CollegeList(ListView):
    model = College
    context_object_name = 'college_list'

    def get_queryset(self):
        return College.objects.all()

class StudentList(ListView):
    model = Student
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.all()


# Generic Views for deleting

class CandidateDelete(DeleteView):
    login_url = 'registration/'
    model = Candidate
    template_name = "registration/candidate_delete.html"
    success_url = reverse_lazy('registration:candidate_list')


class ElectionDelete(DeleteView):
    login_url = 'registration/'
    model = Election
    template_name = "registration/election_delete.html"
    success_url = reverse_lazy('registration:election_list')

class PartyDelete(DeleteView):
    login_url = 'registration/'
    model = Party
    template_name = "registration/party_delete.html"
    success_url = reverse_lazy('registration:party_list')

class PostDelete(DeleteView):
    login_url = 'registration/'
    model = Post
    template_name = "registration/post_delete.html"
    success_url = reverse_lazy('registration:post_list')

class CollegeDelete(DeleteView):
    login_url = 'registration/'
    model = College
    template_name = "registration/college_delete.html"
    success_url = reverse_lazy('registration:college_list')

class StudentDelete(DeleteView):
    login_url = 'registration/'
    model = Student
    template_name = "registration/student_delete.html"
    success_url = reverse_lazy('registration:student_list')

def logout_view(request):
    logout(request)
    return redirect('home:log-in')

@login_required(login_url='/registration/')
def winnerList(request):
    candidate_list = Candidate.objects.all()
    VicePresident = []
    Member = []
    Treasurer = []
    Secretary = []
    President = []
    for candidate in candidate_list:
        if candidate.post.post_name == 'Member':
            Member.append(candidate)
        elif candidate.post.post_name == 'President':
            President.append(candidate)


        elif candidate.post.post_name == 'Secretary':
            Secretary.append(candidate)
        elif candidate.post.post_name == 'Treasurer':
            Treasurer.append(candidate)
        elif candidate.post.post_name == 'Vice President':
            VicePresident.append(candidate)
    VicePresident = sorted(VicePresident,key=attrgetter('votes'))
    President = sorted(President,key=attrgetter('votes'))
    Secretary = sorted(Secretary,key=attrgetter('votes'))
    Treasurer = sorted(Treasurer,key=attrgetter('votes'))
    Member = sorted(Member,key=attrgetter('votes'))

    winners = [
        VicePresident[-1],
        President[-1],
        Secretary[-1],
        Treasurer[-1],
        Member[-1],
    ]

    # global winning
    # winning= []
    # winning = winners

    party_list = Party.objects.all()
    print(party_list)
    candidate_list = Candidate.objects.all()

    # print(winners)

    # for winner in winners:
    #     winnerObj=WinnerReport.objects.create(post = winner.post,
    #                                         candidate_id = winner.candidate_id,
    #                                         votes = winner.votes,
    #                                         election_id = winner.election_id)

    return render(request, 'registration/winnerlist.html', {'winners': winners,
                                                            'party_list':party_list,
                                                            'candidate_list':candidate_list,})



# def viewresult(request):
#     bar2 = bar3 = bar4 = bar5 = bar6 = FusionCharts("","","","","","","")
#     ex = ["ex2", "ex3", "ex4", "ex5", "ex6"]
#     bar = [bar2, bar3, bar4, bar5, bar6]
#     chart = ["chart2", "chart3", "chart4", "chart5", "chart6"]
#     color = ["#FFD904", "#D2100A", "#13BB0D", "#0D79BB", "#B51DDA"]
#     #red, yellow, green, blue, purple
#
#     colleges = College.objects.all()
#     posts = Post.objects.all()
#     parties = Party.objects.all()
#
#     for college in colleges:
#         query = 'SELECT s.name,s.voter_id, q.post, q.party_id_id, q.name as partyname FROM student s INNER JOIN (SELECT c.voter_id, c.party_id_id, w.votes, w.post, c.name FROM (SELECT p.name, d.* FROM party p INNER JOIN candidate d ON p.party_id = d.party_id_id)c INNER JOIN winner_report w ON c.candidate_id = w.candidate_id)q ON s.voter_id = q.voter_id'
#         dataSource = {}
#         dataSource['chart'] = {
#     		"caption": "FSU Election - 2017",
#     		"subCaption": college.name,
#     		"xAxisName": "Candidates",
#     		"yAxisName": "Votes",
#     		"theme": "fint",
#     		"bgColor": "#ffffff",
#     		"borderAlpha": "0",
#     		"showLegend" : "1",
#     		"placevaluesInside": "0",
#     		"rotatevalues": "0",
# 	    }
#
#         dataSource['data'] = []
#         for key in WinnerReport.objects.raw(query):
#             data = {}
#             data['label'] = str(key.name)+' ('+str(key.post) +') '
#             data['value'] = key.votes
#             data['color'] = color[key.party_id_id-1]
#             data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
#             dataSource['data'].append(data)
#             party = key.party_id_id
#
#         column2D = FusionCharts("column2D", "ex1" , "500", "250", "chart1", "json", dataSource)
#
#         for i in range(5):
# 	        for post in Post.objects.raw('SELECT id,post_name FROM post WHERE id=%s',[i+1]):
# 		        dataSource = {}
# 		        dataSource['chart'] = {
#         		    "caption": "FSU Election - 2017" + ' (' + college.name + ' )',
#         		    "subCaption": post.post_name,
#         		    "xAxisName": "Candidates",
#         		    "yAxisName": "Votes",
#         		    "theme": "fint",
#         		    "bgColor": "#ffffff",
#         		    "borderAlpha": "0",
#         		    "showLegend" : "1",
#         		    "placevaluesInside": "0",
#         		    "rotatevalues": "0",
#                 }
#             dataSource['data'] = []
#     	    for key in Candidate.objects.raw('SELECT s.name, q.votes, q.candidate_id, q.party_id_id, q.partyname FROM student s INNER JOIN (SELECT c.*, p.name as partyname FROM candidate c INNER JOIN party p ON c.party_id_id = p.party_id WHERE c.post_id=%s order by c.votes desc limit 3)q ON s.voter_id = q.voter_id',[i+1]):
#         	    data = {}
#         	    data['label'] = key.name
#         	    data['value'] = key.votes
#         	    data['color'] = color[key.party_id_id-1]
#         	    data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
#         	    dataSource['data'].append(data)
#     	    bar[i] = FusionCharts("bar2D", ex[i] , "500", "250", chart[i], "json", dataSource)
#
#
#     return render(request, 'viewResult.html', {'output1': column2D.render(), 'output2':bar[0].render(), 'output3':bar[1].render()
#         , 'output4':bar[2].render(), 'output5':bar[3].render(), 'output6':bar[4].render(), 'zipped':zip(parties,color)})


# def viewresult(request):
#     # global winning
#     bar2 = bar3 = bar4 = bar5 = bar6 = FusionCharts("","","","","","","")
#     ex = ["ex2", "ex3", "ex4", "ex5", "ex6"]
#     bar = [bar2, bar3, bar4, bar5, bar6]
#     chart = ["chart2", "chart3", "chart4", "chart5", "chart6"]
#     color = ["#FFD904", "#D2100A", "#13BB0D", "#0D79BB", "#B51DDA"]
#     #red, yellow, green, blue, purple
#
#     colleges = College.objects.all()
#     posts = Post.objects.all()
#     parties = Party.objects.all()
#
#     for college in colleges:
#         # global winning
#         query = 'SELECT s.name,s.voter_id, q.post, q.party_id_id, q.name as partyname FROM student s INNER JOIN (SELECT c.voter_id, c.party_id_id, w.votes, w.post, c.name FROM (SELECT p.name, d.* FROM party p INNER JOIN candidate d ON p.party_id = d.party_id_id)c INNER JOIN winner_report w ON c.candidate_id = w.candidate_id)q ON s.voter_id = q.voter_id'
#         # dataSource = {}
#         # dataSource['chart'] = {
#         #     "caption": "FSU Election - 2017",
#         #     "subCaption": college.name,
#         #     "xAxisName": "Candidates",
#         #     "yAxisName": "Votes",
#         #     "theme": "fint",
#         #     "bgColor": "#ffffff",
#         #     "borderAlpha": "0",
#         #     "showLegend" : "1",
#         #     "placevaluesInside": "0",
#         #     "rotatevalues": "0",
#         #     }
#         #
#         # dataSource['data'] = []
#         # for key in WinnerReport.objects.raw(query):
#         # # global winning
#         # # for key in winning:
#         #     data = {}
#         #     data['label'] = str(key.name)+' ('+str(key.post) +') '
#         #     data['value'] = key.votes
#         #     data['color'] = color[key.party_id_id-1]
#         #     data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
#         #     dataSource['data'].append(data)
#         #     party = key.party_id_id
#
#         # column2D = FusionCharts("column2D", "ex1" , "500", "250", "chart1", "json", dataSource)
#
#         for i in range(5):
#             for post in Post.objects.raw('SELECT id,post_name FROM post WHERE id=%s',[i+1]):
#                 dataSource = {}
#                 # dataSource['data']=[]
#                 # for key in Candidate.objects.raw('SELECT s.name, q.votes, q.candidate_id, q.party_id_id, q.partyname FROM student s INNER JOIN (SELECT c.*, p.name as partyname FROM candidate c INNER JOIN party p ON c.party_id_id = p.party_id WHERE c.post_id=%s order by c.votes desc limit 3)q ON s.voter_id = q.voter_id',[i+1]):
#                 #     data = {}
#                 #     data['label'] = key.name
#                 #     data['value'] = key.votes
#                 #     data['color'] = color[key.party_id_id-1]
#                 #     data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
#                 #     dataSource['data'].append(data)
#                 dataSource['chart'] = {
#                     "caption": "FSU Election - 2017" + ' (' + college.name + ' )',
#                     "subCaption": post.post_name,
#                     "xAxisName": "Candidates",
#                     "yAxisName": "Votes",
#                     "theme": "fint",
#                     "bgColor": "#ffffff",
#                     "borderAlpha": "0",
#                     "showLegend" : "1",
#                     "placevaluesInside": "0",
#                     "rotatevalues": "0",
#                     }
#
#                 dataSource['data']=[]
#                 for key in Candidate.objects.raw('SELECT s.name, q.votes, q.candidate_id, q.party_id_id, q.partyname FROM student s INNER JOIN (SELECT c.*, p.name as partyname FROM candidate c INNER JOIN party p ON c.party_id_id = p.party_id WHERE c.post_id=%s order by c.votes desc limit 3)q ON s.voter_id = q.voter_id',[i+1]):
#                     data = {}
#                     data['label'] = key.name
#                     data['value'] = key.votes
#                     data['color'] = color[key.party_id_id-1]
#                     data['tooltext'] = "<div><b>$label</b><br/>Votes : <b>$value</b><br/>Party : <b>"+ key.partyname +"</b></div>"
#                     dataSource['data'].append(data)
#                 bar[i] = FusionCharts("bar2D", ex[i] , "500", "250", chart[i], "json", dataSource)
#
#
#     return render(request, 'viewResult.html', { 'output2':bar[0].render(), 'output3':bar[1].render()
#         , 'output4':bar[2].render(), 'output5':bar[3].render(), 'output6':bar[4].render(), 'zipped':zip(parties,color)})
