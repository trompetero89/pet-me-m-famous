from django.urls import path
from . import views

app_name = 'society'

urlpatterns = [
    path('', views.ListSocieties.as_view(), name="all"),
    path("new/", views.CreateSociety.as_view(), name="create"),
    path("petsposts/in/<slug>/",views.SingleSociety.as_view(),name="single"),
    path("join/<slug>/",views.JoinSociety.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveSociety.as_view(),name="leave"),
]
