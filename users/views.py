from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company


#register application only
def register_application(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True  # Ensure your User model has this field
            var.username = var.email  # Only if username is not required separately
            var.save()
            
            # Ensure Resume model exists and is linked to the user
            Resume.objects.create(user=var)  

            messages.success(request, 'Your account has been created. Please login.')
            return redirect('login')  # Ensure 'login' is correctly mapped in urls.py
        else:
            messages.error(request, 'Something went wrong. Please check the form.')
            # Instead of redirecting, return the form with errors
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'users/register_applicant.html', context)

    

#register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True  # Ensure User model has this field
            var.username = var.email  # Set username as email if applicable
            var.save()

            # Ensure the Company model is linked properly
            Company.objects.create(user=var)  

            messages.success(request, 'Your account has been created. Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong. Please check the form.')

    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'users/register_recruiter.html', context)  # Re-render form on error


            
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return render(request, 'users/login.html')

    # Handle GET request by rendering the login page
    return render(request, 'users/login.html')

       
def logout_user(request):
    logout(request)
    messages.info(request, 'Your Session has ended')
    return redirect('login')


