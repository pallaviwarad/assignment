from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import QuesModel
from .forms import addQuestionform

def index(request):
    return render(request, "index.html")


def Signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            return redirect('/register')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')
    return render(request, "signup.html")


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
    return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect('/')

def quiz(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            questions=QuesModel.objects.all()
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                print(request.POST.get(q.question))
                # s
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = score/(total*10) *100
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            return render(request,'result.html',context)
        else:
            questions=QuesModel.objects.all()
            context = {
                'questions':questions
            }
            return render(request,'quiz.html',context)
    else:
        return redirect('/login')

def addQuestion(request):
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else:
        return redirect('home')
