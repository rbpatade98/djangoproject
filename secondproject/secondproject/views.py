from django.shortcuts import HttpResponse
data=f"<hr><a href='/'>Home</a> <a href='/signup'>SignUp</a> <a href='/signin'>SignIn</a>"

def index(request):
   
    return HttpResponse (f"<center><h1>Welcome to My Page{data}</h1></center>")

def signup(request):
    global username
    username=input("enter usename:")
    return HttpResponse(f"<center><h1>SignUp Page{data}</h1></center>")


def signin(request):
    chkusername=input("Enter usename to signin:")
    if chkusername==username:
        next=f"<hr><h1><a href='/'>Logout</a>"
        return HttpResponse(f"<center><h1>Welcome {chkusername}!!!{next}</h1></center>")
    else:
        msg=f"<center><h1>Incorrect username!! Try Again </h1></center>"
        next=f"<hr><h1><a href='/'>Click here to go back</a>"
        return HttpResponse(f"{msg}{next}")