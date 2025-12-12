import os
import sys
import django
import random
from faker import Faker

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

# Django ayarlarını yükle
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from accounts.models import User
from courses.models import Course

fake = Faker("tr_TR")

def create_instructors(n=5):
    instructors = []
    for i in range(n):
        username = f"instructor{i+1}"
        u = User.objects.create_user(
            username=username,
            password="123456",
            role="instructor"
        )
        instructors.append(u)
        print(f"[OK] Instructor created → {username}")
    return instructors


def create_users(n=10):
    users = []
    for i in range(n):
        username = f"user{i+1}"
        u = User.objects.create_user(
            username=username,
            password="123456",
            role="user"
        )
        users.append(u)
        print(f"[OK] User created → {username}")
    return users


def create_courses(instructors, n=8):
    courses = []
    for i in range(n):
        instructor = random.choice(instructors)
        title = fake.sentence(nb_words=4)
        description = fake.text()
        price = round(random.uniform(50, 500), 2)

        c = Course.objects.create(
            title=title,
            description=description,
            instructor=instructor,
            price=price
        )
        courses.append(c)
        print(f"[OK] Course created → {title} ({instructor.username})")
    return courses


def run():
    print("=== MOCK DATA SEED STARTING ===")

    # Temizlik (opsiyonel)
    User.objects.exclude(is_superuser=True).delete()
    Course.objects.all().delete()

    instructors = create_instructors()
    users = create_users()
    create_courses(instructors)

    print("=== MOCK DATA SEED COMPLETED ===")


if __name__ == "__main__":
    run()
