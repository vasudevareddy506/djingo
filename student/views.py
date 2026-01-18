from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>wellcome to student portal</h1>')
def contact_us(request):
    return HttpResponse('<h1>Contact us at: example@email.com</h1>')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        usn= request.POST['usn']
        mob= request.POST['mob']
        email = request.POST['email']
        college = request.POST['college']
        degree = request.POST['degree']
        sem= request.POST['sem']
        branch= request.POST['branch']

        Dept=["cse","aiml","ece","mech","civil","eee"]

        return render(request, 'student/display.html', {'name': name,'mobile':mob,'usn':usn,'email': email, 'college': college, 'degree': degree, 'sem':sem,'branch':branch,'dept':Dept})



    return render(request, 'student/register.html')