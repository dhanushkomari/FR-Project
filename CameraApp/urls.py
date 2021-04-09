from django.urls import path
from .import views

app_name = 'CameraApp'

urlpatterns = [
    ########################   APP URLS   ############################
    path('', views.Index ,name ='index'),
    path('create', views.UserCreateView, name = 'create'),
    path('video_feed', views.video_feed, name = 'video_feed'),

    ########################  APP AUTHENTICATION  ####################
    path('login', views.LoginView, name = 'login'),
    path('logout', views.LogoutView, name = 'logout'),

    ########################   API URLS   ############################
    path('api', views.apiView, name = 'api'),
    path('api/patients', views.recentPatient, name = 'recent_patient'),
    path('api/status-recent', views.recentStatus, name = 'receent_status'),
    path('api/status', views.StatusRest, name = 'status'),
    path('api/all-patients', views.allPatients, name = 'all_patients'),
    path('api/create-status', views.createStatus, name = 'create_status'),
    path('api/create-patient', views.createPatient, name = 'create-patient'),
]
