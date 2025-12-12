from django.urls import path
from .views import CourseListView, PurchaseCourseView, UserPurchasesView, MyLessonRequestsView, LiveLessonRequestView, InstructorAssignedLessonsView


urlpatterns = [
    path("", CourseListView.as_view(), name="course-list"),
    path("purchase/", PurchaseCourseView.as_view(), name="purchase-course"),
    path("purchases/", UserPurchasesView.as_view(), name="user-purchases"),
    path('live/request/', LiveLessonRequestView.as_view(), name='create-live-request'),
    path('live/my/', MyLessonRequestsView.as_view(), name='my-live-requests'),
    path('live/instructor/', InstructorAssignedLessonsView.as_view(), name='instructor-live-requests'),
]
