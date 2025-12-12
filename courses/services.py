from accounts.models import User

def assign_instructor():
    instructors = User.objects.filter(role='instructor').order_by("id").first()
    return instructors

def notify_instructor(instructor, student):
    print(f"Notification: Instructor {instructor.username}, you have a new lesson request from {student.username}.")