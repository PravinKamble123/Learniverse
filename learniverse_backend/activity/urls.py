from django.urls import path

from .views import *

app_name = 'activity'

urlpatterns = [
    path('active-courses/', get_active_courses),
    path('track-started/<slug:course_slug>/<slug:lesson_slug>/', track_started),
    path('mark-as-done/<slug:course_slug>/<slug:lesson_slug>/', mark_as_done),
]