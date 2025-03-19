from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    home=f"<a href='/'>home</a>"
    library=f"<a href='/library/'>library</a>"
    exam=f"<a href='/exam/'>exam</a>"
    events=f"<a href='/events/'>events</a>"
    return HttpResponse(f"<center><h1>welcome to my first app<hr>{home} {library} {exam} {events}</h1></center>")
