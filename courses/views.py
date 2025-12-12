from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Course, Purchase, LiveLessonRequest
from .serializers import CourseSerializer, PurchaseSerializer, LiveLessonRequestSerializer
from .payments import mock_payment_processing
from .services import assign_instructor, notify_instructor



# Create your views here.
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class PurchaseCourseView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

        payment_result = mock_payment_processing(user.id, course.id, float(course.price))

        if payment_result["status"] == "success":
            purchase = Purchase.objects.create(
                user=user,
                course=course,
                payment_id=payment_result["payment_id"],
                status="completed"
            )
            serializer = PurchaseSerializer(purchase)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Payment failed."}, status=status.HTTP_400_BAD_REQUEST)
        
class UserPurchasesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(user=user)
    

class LiveLessonRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        instructor = assign_instructor()
        if not instructor:
            return Response({"error": "No instructors available."}, status=status.HTTP_400_BAD_REQUEST)

        lesson_request = LiveLessonRequest.objects.create(
            student=user,
            instructor=instructor,
            status="assigned"
        )

        notify_instructor(instructor, user)

        serializer = LiveLessonRequestSerializer(lesson_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MyLessonRequestsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveLessonRequestSerializer

    def get(self, request):
        query_set = LiveLessonRequest.objects.filter(student=request.user)
        serializer = LiveLessonRequestSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class InstructorAssignedLessonsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveLessonRequestSerializer

    def get(self, request):
        if not request.user.role == 'instructor':
            return Response({"error": "Only instructors can access this."}, status=status.HTTP_403_FORBIDDEN)
        query_set = LiveLessonRequest.objects.filter(instructor=request.user)
        serializer = LiveLessonRequestSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
