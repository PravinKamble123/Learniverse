from random import randint
from django.utils.text import slugify

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
from .serializers import *

from .models import *




@api_view(['POST'])
def create_course(request):
   
    print(request.data)
    course = Course.objects.create(
        title=request.data.get('title'),
        slug='%s-%s' % (slugify(request.data.get('title')), randint(1000, 10000)), 
        short_description=request.data.get('short_description'), 
        long_description=request.data.get('long_description'),
        status=request.data.get('status'),
        created_by = request.user
        )
    
    for id in request.data.get('categories'):
        course.categories.add(id)
    
    course.save()
   
   # Lessons
    for lesson in request.data.get('lessons'):
        temp_lesson = Lessons.objects.create(
            course= course,
            title=lesson.get('title'),
            slug=slugify(lesson.get("title")),
            short_description = lesson.get("short_description"),
            long_description = lesson.get("long_description"),
            status = Lessons.DRAFT
        
        )

    return Response({
        'course_id': course.id
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):

    category_id = request.GET.get('category_id', '')
    course= Course.objects.filter(status=Course.PUBLISHED)

    if category_id:
        course = course.filter(categories__in=[int(category_id)])

    serializer= CourseListSerializer(course, many=True)
    return Response(serializer.data)


# Get all categories

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer= CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_frontpage_courses(request):
    course= Course.objects.filter(status=Course.PUBLISHED)[0:4]

    serializer= CourseListSerializer(course, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_course(request, slug):
    course= Course.objects.filter(status=Course.PUBLISHED).get(slug=slug)
    course_serializer= CourseSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    


   
    return Response({
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    })


@api_view(['POST'])
def add_comment(request,course_slug, lesson_slug):
    data = request.data
    lesson= Lessons.objects.get(slug=lesson_slug)

    comment=Comment.objects.create(course=lesson, name=data.get('name'), content=data.get('content'), created_by=request.user)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['GET'])
def get_comment(request,course_slug, lesson_slug):
    lesson=Lessons.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)

    return Response(serializer.data)



@api_view(['GET'])
def get_quiz(request,course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()

    serializer = QuizSerializer(quiz)
    

    return Response(serializer.data)


@api_view(['GET'])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.filter(status=Course.PUBLISHED)
    user_serializer = UserSerializer(user, many= False)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response({
        'courses': courses_serializer.data,
        'created_by': user_serializer.data
    })