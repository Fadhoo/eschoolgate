from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from eSchoolGateProject import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users/', include('users.urls')),
                  path('subject/', include('subject.urls')),
                  url(r'^rest-auth/', include('rest_auth.urls')),
                  url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
                  # path('signup/', SignUp.as_view(), name='signup'),
                  # path('signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
                  # path('signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
