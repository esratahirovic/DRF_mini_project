from django.db import models
from accounts.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.status}"
    
class LiveLessonRequest(models.Model):
    student = models.ForeignKey("accounts.User", on_delete=models.CASCADE, limit_choices_to={'role': 'user'}, related_name="lessons_requests")
    instructor = models.ForeignKey("accounts.User", on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'}, related_name="assigned_lessons")

    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lesson Request from {self.student.username} to {self.instructor.username} - {self.status}"
