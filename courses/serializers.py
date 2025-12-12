from rest_framework import serializers
from .models import Course, Purchase, LiveLessonRequest
from accounts.models import User

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(source="instructor.username", read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'price']
        read_only_fields = ['id', 'instructor']

class PurchaseSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(source="course.title", read_only=True)

    class Meta:
        model = Purchase
        fields = ['id', 'user', 'course', 'payment_id', 'status', 'created_at']
        read_only_fields = ['id', 'user', 'course', 'created_at']

class LiveLessonRequestSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(source="student.username", read_only=True)
    instructor = serializers.StringRelatedField(source="instructor.username", read_only=True)

    class Meta:
        model = LiveLessonRequest
        fields = ['id', 'student', 'instructor', 'status', 'created_at']
        read_only_fields = ['id', 'student', 'instructor', 'created_at']

    