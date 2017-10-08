from django.conf.urls import url

from . import views
app_name = 'registration'
urlpatterns = [
    url(r'^$', views.homeView, name='homeView'),
    url(r'register/$',views.register,name = 'register'),
    url(r'create/$',views.simple,name = 'simple'),
    url(r'winners/$',views.winnerList,name = 'winners'),
    # url(r'viewresult/$',views.viewresult,name = 'viewresult'),

    # URLs for creating the models are listed here
    url(r'add-candidate/$',views.CandidateCreate.as_view(),name = 'candidate_add'),
    url(r'add-election/$',views.ElectionCreate.as_view(),name = 'election_add'),
    url(r'add-party/$',views.PartyCreate.as_view(),name = 'party_add'),
    url(r'add-post/$',views.PostCreate.as_view(),name = 'post_add'),
    url(r'add-college/$',views.CollegeCreate.as_view(),name = 'college_add'),
    url(r'add-student/$',views.StudentCreate.as_view(),name = 'student_add'),

    # URLs for updating the models are listed her

    url(r'update-candidate/(?P<pk>[0-9]+)$',views.CandidateUpdate.as_view(),name = 'candidate_update'),
    url(r'update-election/(?P<pk>[0-9]+)$',views.ElectionUpdate.as_view(),name = 'election_update'),
    url(r'update-party/(?P<pk>[0-9]+)$',views.PartyUpdate.as_view(),name = 'party_update'),
    url(r'update-post/(?P<pk>[0-9]+)$',views.PostUpdate.as_view(),name = 'post_update'),
    url(r'update-college/(?P<pk>[0-9]+)$',views.CollegeUpdate.as_view(),name = 'college_update'),
    url(r'update-student/(?P<pk>[0-9]+)$',views.StudentUpdate.as_view(),name = 'student_update'),

    # URLs for reading the models are listed below

    url(r'list-candidate/$',views.CandidateList.as_view(),name = 'candidate_list'),
    url(r'list-election/$',views.ElectionList.as_view(),name = 'election_list'), #This one is errorenous
    url(r'list-party/$',views.PartyList.as_view(),name = 'party_list'),
    url(r'list-post/$',views.PostList.as_view(),name = 'post_list'),
    url(r'list-college/$',views.CollegeList.as_view(),name = 'college_list'),
    url(r'list-student/$',views.StudentList.as_view(),name = 'student_list'),


    # URLs for deleting the models are listed below

    url(r'delete-candidate/(?P<pk>[0-9]+)$',views.CandidateDelete.as_view(),name = 'candidate_delete'),
    url(r'delete-election/(?P<pk>[0-9]+)$',views.ElectionDelete.as_view(),name = 'election_delete'), #This one is errorenous
    url(r'delete-party/(?P<pk>[0-9]+)$',views.PartyDelete.as_view(),name = 'party_delete'),
    url(r'delete-post/(?P<pk>[0-9]+)$',views.PostDelete.as_view(),name = 'post_delete'),
    url(r'delete-college/(?P<pk>[0-9]+)$',views.CollegeDelete.as_view(),name = 'college_delete'),
    url(r'delete-student/(?P<pk>[0-9]+)$',views.StudentDelete.as_view(),name = 'student_delete'),


    # URL to log a user out

    url(r'logout/$',views.logout_view,name = 'logout')
]
