from django.urls import path
from django.conf.urls import url
from .views import SubjectList, LessonList, Home


urlpatterns = [
    path('subject-list/', SubjectList.as_view()),
    path('home/', Home.as_view(), name='home'),
    path('lessons-list/', LessonList.as_view()),

    # url(r'^users-profile/(?P<pk>[0-9]+)/?$', UserProfile.as_view(), name='user_profile'),
    # path('users-profile/', UserProfile.as_view()),
]