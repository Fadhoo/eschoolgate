from django.urls import path
from django.conf.urls import url
from .views import UserList, UserProfile, Login


urlpatterns = [
    path('users-list/', UserList.as_view()),
    url(r'^users-profile/(?P<pk>[0-9]+)/?$', UserProfile.as_view(), name='user_profile'),
    path('login/', Login.as_view(), name='login'),

]