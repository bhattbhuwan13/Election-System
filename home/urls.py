from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.login, name='log-in'),
    # /index/
    url(r'index/$', views.IndexView.as_view(), name='index'),
    # /home/<candidate_id>/voted
    url(r'index/voted/$', views.voted, name='voted'),
    # /result/
    url(r'result/$', views.result, name='result'),

    # for login
    # url(r'login/$', views.user_login, name='login'),

    # url(r'candidate/(?P<pk>[0-9]+)/detail/$', views.CandidateDetail.as_view(), name='candidate_detail'),
    #
    # # for adding candidate
    #
    # # url(r'^candidate/add/$',views.add_candidate,name = 'add_candidate'),
    #
    # url(r'candidate/add/$',views.CandidateCreate.as_view(),name = 'add_candidate'),
    #
    # url(r'candidate/(?P<pk>[0-9]+)/delete/$', views.CandidateDelete.as_view(), name='candidate_delete'),
    #
    # url(r'candidate/(?P<pk>[0-9]+)/update/$', views.CandidateUpdate.as_view(), name='candidate_update'),
    # for admin dashboard
    # url(r'admin/$',views.home, name='myadmin'),
    # display the list of candidates

]
