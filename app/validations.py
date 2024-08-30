"""_summary_
"""
from django.contrib.auth import hashers
import regex
from .models import Course, Exam, User, Faculty



class Output:
    """This object contains a message to be passed to the user and a boolean to indicate
    whether they can proceed or not
    """
    message: str
    result: bool
    def __init__(self, message:str, result:bool = False) -> None:
        self.message = message
        self.result = result


def signin_v(u_input):
    """This function validates the signin page after the user must have inputted
    their signin details and returns an object indicating whether user details
    are valid or not, alongside a message to pass to the user

    Args:
        u_input (object): This contains the signin details(username and password)
    """
    try:
        if not u_input["username"]:
            return Output("Input your username.")

        if not u_input["password"]:
            return Output("Input your password.")

        try:
            user = User.objects.get(username=u_input["username"])
        except User.DoesNotExist:
            return Output("User does not exist.")

        if not hashers.check_password(u_input["password"], user.password):
            return Output("Password is incorrect!")

        if user.suspended is True:
            return Output("You can't access the CBT at the moment, contact admin!")


    except BaseException as e:
        print(str(e))
        return Output("An unknown error occured!")

    else:
        return Output("Signed in successfully!", True)


def signup_v(u_input):
    """This function validates the signup page after the user must have inputted
    their details and returns an object indicating whether user details
    are valid or not, alongside a message to pass to the user

    Args:
        u_input (object): This contains the user details
    """
    try:
        #firstname
        if not u_input["firstname"]:
            return Output("Input your firstname.")

        if len(u_input["firstname"]) < 2:
            return Output("Firstname should be more than 2 characters.")

        if len(u_input["firstname"]) > 50:
            return Output("Firstname should not be more than 50 characters.")

        if not regex.fullmatch(r"^[a-zA-Z]+$", u_input["firstname"]):
            return Output("Firstname should only contain alphabets.")
        #endlastname

        #lastname
        if not u_input["lastname"]:
            return Output("Input your lastname.")

        if len(u_input["lastname"]) < 3:
            return Output("Lastname should be more than 3 characters.")

        if len(u_input["lastname"]) > 50:
            return Output("Lastname should not be more than 50 characters.")

        if not regex.fullmatch(r"^[a-zA-Z]+$", u_input["lastname"]):
            return Output("Lastname should only contain alphabets.")
        #endlastname

        #othername
        if u_input["othername"]:
            if len(u_input["othername"]) < 3:
                return Output("Other name should be more than 3 characters.")

            if len(u_input["othername"]) > 50:
                return Output("Other name should not be more than 50 characters.")

            if not regex.fullmatch(r"^[a-zA-Z]+$", u_input["othername"]):
                return Output("Other name should only contain alphabets.")
        #endothername

        #course
        if not u_input["course"]:
            return Output("Select your course.")

        courses = Course.objects.all().values("code")
        for course in courses:
            if u_input["course"] in course["code"]:
                break
        else:
            return Output("An error occured.")
        #endcourse

        #matric_number
        if not u_input["matric_number"]:
            return Output("Input your matric number.")

        if len(u_input["matric_number"]) < 5:
            return Output("Matric number can't have less than 5 characters.")

        if User.objects.filter(matric_number=u_input["matric_number"]).exists():
            return Output("Matric number is taken or already exists.")
        #endmatric_number

        #email
        if not u_input["email"]:
            return Output("Input your email.")

        if not regex.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", u_input["email"]):
            return Output("Invalid email provided")

        if User.objects.filter(email=u_input["email"]).exists():
            return Output("Email is taken or already exists.")
        #endemail

        #username
        if not u_input["username"]:
            return Output("Input your username.")

        if not regex.fullmatch(r"^[a-zA-Z]+([0-9]+[a-zA-Z]*)*$", u_input["username"]):
            return Output("Invalid username provided.")

        if User.objects.filter(username=u_input["username"]).exists():
            return Output("Username is taken or already exists.")
        #endusername

        #passwords
        if not u_input["password"]:
            return Output("Input your password.")

        if not regex.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)(?:\S+\s?)*$", u_input["password"]):
            return Output("Password must contain at least a lowercase & uppercase letter, a number and a symbol.")

        if len(u_input["password"]) < 8:
            return Output("Password can't have lesser than 8 characters.")

        if len(u_input["password"]) > 20:
            return Output("Password can't have more than 20 characters.")

        if not u_input["cpassword"]:
            return Output("Confirm your password.")

        if (u_input["password"] == u_input["cpassword"]) is not True:
            return Output("Password mismatch.")
        #endpasswords


    except BaseException as e:
        print(str(e))
        return Output("An unknown error occured!")

    else:
        return Output("Signed up successfully!", True)


def exam_v(u_input):
    """_summary_

    Args:
        u_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        if u_input.get("id", False) is not False and not u_input["id"].isnumeric():
            return Output("An error occured, try reloading the page.")

        if not u_input["label"]:
            return Output("Input exam label.")

        if len(u_input["label"]) < 4:
            return Output("Exam label should not have lesser than 4 characters.")

        if len(u_input["label"]) > 50:
            return Output("Exam label should not have more than 50 characters.")

        if not regex.fullmatch(r"^[a-zA-Z0-9()\s]+$", u_input["label"]):
            return Output("Exam label should only contain alphabets, parentheses, and numeric characters.")

        if Exam.objects.filter(label=u_input["label"], course=u_input["course"]).exists():
            return Output("Exam with same label and course already exists.")


        if not u_input["course"]:
            return Output("Select exam course.")

        courses = Course.objects.all().values("code")
        for course in courses:
            if u_input["course"] in course["code"]:
                break

        else:
            print("Invalid or no course selected")
            return Output("An error occured, try reloading page.")


    except BaseException as e:
        print(e)
        return Output("An unknown error occured!")

    else:
        return Output("Exam saved successfully!", True)


def faculty_v(u_input):
    try:
        if u_input.get("id", False) is not False and not u_input["id"].isnumeric():
            return Output("An error occured, try reloading the page.")

        if not u_input["name"]:
            return Output("Input Faculty name.")

        if len(u_input["name"]) < 4:
            return Output("Faculty name should not have lesser than 4 characters.")

        if len(u_input["name"]) > 100:
            return Output("Faculty name should not have more than 100 characters.")

        if not regex.fullmatch(r"^[a-zA-Z0-9()\s]+$", u_input["name"]):
            return Output("Faculty name should only contain alphabets, parentheses, and numeric characters.")

        if Faculty.objects.filter(name=u_input["name"]).exists():
            return Output("Faculty with same name already exists.")

    except BaseException as e:
        print(e)
        return Output("An unknown error occured!")

    else:
        return Output("Faculty saved successfully!", True)
