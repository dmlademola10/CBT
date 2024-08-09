import datetime, json
from django.http import JsonResponse
from django.urls import reverse
from app import validations
from app.models import Course, Exam, Faculty

def ajax(request):
    return (request.headers.get("X-Requested-With", "") == "XMLHttpRequest")

def create_exam(request):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in! <a href='" + reverse("signin") + "' target='_blank'>Sign in here</a>"
            response["result"] = False

        elif request.method == "POST" and ajax(request):
            output = validations.exam_v(request.POST)
            if output.result is True:
                try:
                    Exam(
                        code=(request.POST["label"].replace(" ", "_") + "_" + datetime.datetime.strftime(datetime.datetime.now(), "%d%m%Y%H%M%S")).lower(),
                        label=request.POST["label"],
                        course=request.POST["course"],
                    ).save()

                except BaseException as e:
                    print(e)
                    response["message"] = "An error occured while saving!"
                    response["result"] = False

                else:
                    response["message"] = output.message
                    response["result"] = output.result

            else:
                response["message"] = output.message
                response["result"] = output.result

        else:
            response = {"message": "An error occured while parsing the request!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def refresh_exam(request):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "GET" and ajax(request):
            exams = list()
            exams_ = Exam.objects.all().values("id", "label", "course").order_by("-time_added")
            for exam in exams_:
                exam["label"] = exam["label"] + " (" + Course.objects.get(code=exam["course"]).name + ")"
                del exam["course"]
                exams.append(exam)
            exams = json.dumps(exams)
            response["message"] = exams
            response["result"] = True

        else:
            response = {"message": "An error occured while contacting the server!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def get_exam(request, id):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "GET" and ajax(request):
            try:
                exam = Exam.objects.get(id=id)
                response["message"] = json.dumps({"label": exam.label, "course": exam.course})
                response["result"] = True
            except Exam.DoesNotExist:
                response["message"] = "Exam does not exist, try reloading the page."
                response["result"] = False

        else:
            response = {"message": "An error occured while contacting the server!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def edit_exam(request):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "POST" and ajax(request):
            u_inputs=dict(id=request.POST["id"], label=request.POST["edit_label"], course=request.POST["edit_course"])
            output = validations.exam_v(u_inputs)
            if output.result is True:
                try:
                    exam = Exam.objects.get(id=u_inputs["id"])

                except Exam.DoesNotExist as e:
                    print(e)
                    response["message"] = "That exam does not exist, try reloading the page!"
                    response["result"] = False

                if exam:
                    try:
                        exam.label = u_inputs["label"]
                        exam.course = u_inputs["course"]
                        exam.save()

                    except BaseException as e:
                        print(e)
                        response["message"] = "An error occured while saving!"
                        response["result"] = False

                    else:
                        response["message"] = output.message
                        response["result"] = output.result

            else:
                response["message"] = output.message
                response["result"] = output.result

        else:
            response = {"message": "An error occured while parsing the request!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def del_exam(request, id):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "GET" and ajax(request):
            if id.isnumeric() is not True:
                response["message"] = "An error occured! Try reloading the page."
                response["result"] = False
            else:
                try:
                    exam = Exam.objects.get(id=id)
                    exam.delete()

                except Exam.DoesNotExist as e:
                    print(e)
                    response["message"] = "That exam does not exist, try reloading the page!"
                    response["result"] = False

                else:
                    response["message"] = "Exam deleted successfully!"
                    response["result"] = True

        else:
            response = {"message": "An error occured while parsing the request!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def create_faculty(request):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in! <a href='" + reverse("signin") + "' target='_blank'>Sign in here</a>"
            response["result"] = False

        elif request.method == "POST" and ajax(request):
            u_inputs = request.POST.dict()
            u_inputs["name"] = u_inputs["name"].removeprefix("Faculty of ")
            print(u_inputs)
            output = validations.faculty_v(u_inputs)
            if output.result is True:
                try:
                    Faculty(
                        code=(u_inputs["name"].replace(" ", "_") + "_" + datetime.datetime.strftime(datetime.datetime.now(), "%d%m%Y%H%M%S")).lower(),
                        name=u_inputs["name"],
                    ).save()

                except BaseException as e:
                    print(e)
                    response["message"] = "An error occured while saving!"
                    response["result"] = False

                else:
                    response["message"] = output.message
                    response["result"] = output.result

            else:
                response["message"] = output.message
                response["result"] = output.result

        else:
            response = {"message": "An error occured while parsing the request!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def get_faculty(request, id):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "GET" and ajax(request):
            try:
                exam = Faculty.objects.get(id=id)
                response["message"] = json.dumps({"name": exam.name, "code": exam.code})
                response["result"] = True
            except Faculty.DoesNotExist:
                response["message"] = "Faculty does not exist, try reloading the page."
                response["result"] = False

        else:
            response = {"message": "An error occured while contacting the server!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)

def edit_faculty(request):
    try:
        response = dict()
        if request.session.get("user", False) is False:
            response["message"] = "You are not signed in!"
            response["result"] = False

        elif request.method == "POST" and ajax(request):
            u_inputs=dict(id=request.POST["id"], name=request.POST["edit_name"].removeprefix("Faculty of "))
            output = validations.faculty_v(u_inputs)
            if output.result is True:
                try:
                    faculty = Faculty.objects.get(id=u_inputs["id"])

                except Faculty.DoesNotExist as e:
                    print(e)
                    response["message"] = "That faculty does not exist, try reloading the page!"
                    response["result"] = False

                if faculty:
                    try:
                        faculty.name = u_inputs["name"]
                        faculty.save()

                    except BaseException as e:
                        print(e)
                        response["message"] = "An error occured while saving!"
                        response["result"] = False

                    else:
                        response["message"] = output.message
                        response["result"] = output.result

            else:
                response["message"] = output.message
                response["result"] = output.result

        else:
            response = {"message": "An error occured while parsing the request!", "result": False}

    except BaseException as e:
        print(str(e))
        return JsonResponse({"message": "An error occured!", "result": False})

    else:
        return JsonResponse(response)
