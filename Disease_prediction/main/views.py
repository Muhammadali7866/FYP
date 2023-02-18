from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,"main/index.html")


#user signup view
def sign_up(request):
    return render(request,"main/signup.html")

#user login

def user_login(request):
    return render(request,"main/login.html")

#service 
def service(request):
    return render(request,"main/service.html")

#function of about

def about(request):
    return render(request,"main/about.html")

#function of contact

def contact(request):
    return render(request,"main/contact.html")

#appointment function

def appointment(request):
    return render(request,"main/appointment.html")

#blog function

def blog(request):
    return render(request,"main/blog.html")

#price function
def price(request):
    return render(request,"main/price.html")




