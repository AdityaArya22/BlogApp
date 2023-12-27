from django.shortcuts import render, redirect
from home.models import *
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# Create your views here.
def index(request):
    return render(request ,'index.html')
def registerpage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Already Taken.", extra_tags="danger")
            return redirect('registerpage/')


        user = User.objects.create  (
            email = email,
            username  = username
        )
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account Created Sucessfully!")

        return redirect('/feed/')
    return render(request, "register.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():  # Fix: added ()
            messages.error(request, 'Invalid Username')
            return redirect('/loginpage/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            # messages.error(request, 'Invalid Password')
            return redirect('/feed/')
        else:
            login(request, user)
            return redirect('/feed/')


        


    return render(request, "login.html")

def homepage(request):
    return render(request, 'index.html')

def createpost(request):
    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        desc = data.get('desc')
        pic = request.FILES.get('pic')
        en = userData(
            username = username,
            desc = desc,
            pic = pic
        )
        print(username)
        print(desc)
        en.save()
        return redirect('/feed/')
    
    queryset = userData.objects.all()
    context = {'userData': queryset}
    return render(request, 'create.html', context)



def feed(request):
    user = userData.objects.all().order_by('-id')
    comments = Comment.objects.all() 
    return render(request, "feed.html", {'userData': user, 'comments': comments})


def comment_view(request, user_id):
    user_data = userData.objects.get(id=user_id)

    if request.method == "POST":
        username = request.POST.get('username')
        comment_text = request.POST.get('desc')

        # Check if comment_text is not empty before creating a new comment
        if comment_text:
            comment = Comment.objects.create(
                user_data=user_data,
                author=username,
                body=comment_text
            )

    # Get existing comments for the user_data
    comments = user_data.comments.all()

    return render(request, 'comment.html', {'user_data': user_data, 'comments': comments})




def deletepost(request,id):
    queryset = userData.objects.get(id=id)
    queryset.delete()
    return redirect('/feed/')

def edit(request,id):
    queryset = userData.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        desc = data.get('desc')
        pic = request.FILES.get('pic')

        queryset.username = username
        queryset.desc = desc

        if pic:
            queryset.pic = pic

        queryset.save()
        return redirect('/feed/')

    context = {'userData':queryset}
    return render(request,'edit.html',context)

