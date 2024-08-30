"""
_summary_
"""
import datetime
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app import myutils
from . import validations
from .models import Course, Exam, Faculty, User
from django.contrib.auth import hashers

# Create your views here.

def redirect(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        if request:
            pass


    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return HttpResponsePermanentRedirect(reverse("signin"))



def signin(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        context = dict()

        if request.POST:
            output = validations.signin_v(request.POST)
            if output.result is True:
                username=request.POST["username"]
                User.objects.filter(username=username).update(last_accessed=datetime.datetime.now(datetime.UTC))
                request.session["user"]=User.objects.get(username=username).id # type: ignore
                return HttpResponseRedirect(reverse("dashboard"))
            else:
                context["output"] = output

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "signin.html", context) if len(context) != 0 else render(request, "signin.html")



def signup(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        context = dict()
        context["collection"] = myutils.facs()

        if request.POST:
            output = validations.signup_v(request.POST)
            if output.result is True:
                try:
                    User(
                        firstname=request.POST["firstname"],
                        lastname=request.POST["lastname"],
                        othername=request.POST["othername"],
                        course=request.POST["course"],
                        matric_number=request.POST["matric_number"],
                        email=request.POST["email"],
                        username=request.POST["username"],
                        password=hashers.make_password(request.POST["password"]),
                    ).save()

                except BaseException as e:
                    print(e)
                    output.message = "An error occured while registering you!"
                    output.result = False
                    context["output"] = output
                    context["inputs"] = request.POST


                else:
                    username=request.POST["username"]
                    request.session["user"]=User.objects.get(username=username).id # type: ignore
                    return HttpResponseRedirect(reverse("dashboard"))

            else:
                context["output"] = output
                context["inputs"] = request.POST

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "signup.html", context)



def dashboard(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """

    try:
        if request.session.get("user", False) is False:
            return HttpResponseRedirect(reverse("signin") + "?proceed=" + reverse("exams"))

        else:
            print(request.session["user"])

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "dashboard.html")



def exams(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        if request.session.get("user", False) is False:
            return HttpResponseRedirect(reverse("signin") + "?proceed=" + reverse("exams"))

        context = dict()
        context["collection"] = myutils.facs()

        exams = Exam.objects.all().values().order_by("-time_added")
        for exam in exams:
            exam["label"] = exam["label"] + " (" + Course.objects.get(code=exam["course"]).name + ")"

        context["exams"] = exams

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "exams.html", context)

def faculties(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        if request.session.get("user", False) is False:
            return HttpResponseRedirect(reverse("signin") + "?proceed=" + reverse("faculties"))

        context = dict()
        context["faculties"] = Faculty.objects.all()

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "faculties.html", context)

def courses(request):
    """
    _summary_

    Args:
        request (_type_): _description_
    """
    try:
        if request.session.get("user", False) is False:
            return HttpResponseRedirect(reverse("signin") + "?proceed=" + reverse("courses"))

        context = dict()
        context["courses"] = Course.objects.all()

    except BaseException as e:
        print(str(e))
        return HttpResponse("An error occured!")

    else:
        return render(request, "courses.html", context)
