from .models import Course
from .models import Faculty

def facs():
    faculties=Faculty.objects.all()
    courses=Course.objects.all()
    collection=list()
    for faculty in faculties:
        c=list()
        for course in courses:
            if course.faculty_code == faculty.code:
                c.append({"name": str(course), "code": course.code})

        collection.append({"name": str(faculty), "courses": c})

    return collection
