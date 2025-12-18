from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import SchoolView,ClassView,StudentView

router = DefaultRouter()

router.register('school',SchoolView,basename='school_get_or_post')
router.register('class',ClassView,basename='class_get_or_post')
router.register('student',StudentView,basename='student_get_or_post')



urlpatterns = [
    path('',include(router.urls)),
]
