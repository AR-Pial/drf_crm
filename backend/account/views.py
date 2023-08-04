from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from .forms import CustomAuthenticationForm,CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page after login
                return redirect('home')  # Replace 'home' with the URL name of your home page
            
      
        else:
            context = {
                "form":form
            }
    
            return render(request,'login.html',context)



    form = CustomAuthenticationForm()
    context = {
        "form":form
    }
    
    return render(request,'login.html',context)

def registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            if user_type == 'admin':
                user.is_staff = True
            user.save()

            phone = form.cleaned_data['phone']
            department = form.cleaned_data['department']
            designation = form.cleaned_data['designation']
            employee_id = form.cleaned_data['employee_id']
            types = user_type

            profile, created =  UserProfile.objects.update_or_create(user=user,phone=phone,department=department,designation=designation,employee_id=employee_id,types=types)
            group, created = Group.objects.get_or_create(name=user_type)
            user.groups.add(group)
            return redirect('registration')
        else:
            print(form.errors)
            
    form = CustomUserCreationForm()
    user_profiles = UserProfile.objects.all()

    context = {
        "form": form,
        "user_profiles":user_profiles
    }
    return render(request,'user/registration.html',context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

@login_required
def home(request):
    return render(request,'home.html')
