from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Todo_table
from .forms import *
from send_mail_app.tasks import send_mail_func
# Create your views here.
def registeration(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm=request.POST.get("confirm")

        if password!=confirm:
            messages.warning(request,"Confirm password does not match the password ")
            return HttpResponseRedirect(request.path_info)
        user_obj=User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request,"user all ready exist")
            return HttpResponseRedirect(request.path_info)
        
        user_obj=User.objects.create(username=email,first_name=name)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,"user created successfully")
        user=authenticate(request,username=email,password=password)
        login(request,user)
        return redirect("/")
    return render(request,"account/register.html")

def login_page(request):
    
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user_obj=User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request,"user not found")
            return HttpResponseRedirect(request.path_info)
        user_obj=authenticate(username=email,password=password)


        if user_obj:
            login(request,user_obj)
            return redirect("/")
        
        messages.warning(request,"Invalid credential")
        return HttpResponseRedirect(request.path_info)
    return render(request,"account/login.html")


def home(request):
    
    if request.user.is_authenticated:
      user_todo=Todo_table.objects.filter(user_id=request.user).values()
      todo_list=list(user_todo)
      return render(request,"account/home.html",context={'todo_list':todo_list})
    return redirect('login')

def logout_page(request):
    return redirect('login')
@login_required

def create_todo(request):
    print(request.method)
    if request.method=="POST":
        form = todo_create_form(request.POST)
        if form.is_valid():
            # This will save the todo with all the data, including the due_date
            todo=form.save(commit=False)
            todo.user_id=request.user
            todo.save()
            messages.success(request, "Successfully created todo!")
            return redirect("/")  # Or to a page that lists todos
    else:
        form = todo_create_form()
         
    return render(request, 'todo_page/create.html', {'form': form})
# views.py

def delete_tod(request, uid):
    if request.method == 'POST':  # Handle deletion only for POST requests
        todo_exists = get_object_or_404(Todo_table, uid=uid)
        todo_exists.delete()
        return redirect('/')  # Redirect to home or wherever you want after deletion

    

def edit_todo(request,uid):
    print(uid)
    todo=get_object_or_404(Todo_table,uid=uid,user_id=request.user)
    if request.method=='POST':
         form = todo_create_form(request.POST, instance=todo)  # Bind form with POST data and existing todo
         if form.is_valid():
            form.save()  # Save the updated todo
            return redirect('/')
    form =todo_create_form(instance=todo)
    return render (request,'todo_page/create.html',{'form':form})

