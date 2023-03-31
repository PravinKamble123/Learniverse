from django.urls import path

from .views import *

app_name='course'

urlpatterns = [
    path('', get_courses, name='courses'),
    path('create-course/', create_course),
    path('get-author-courses/<int:user_id>', get_author_courses),
    path('categories/', get_categories, name='categories'),
    path('get_frontpage_courses/', get_frontpage_courses),
    path('<slug:slug>/', get_course, name='course'),
    path('<slug:course_slug>/<slug:lesson_slug>/', add_comment, name='add-comment'),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments', get_comment, name='get-comment'),
    path('<slug:course_slug>/<slug:lesson_slug>/get-quiz/', get_quiz, name='get-quiz'),
]