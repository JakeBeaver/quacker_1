from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
# Create your views here

homepage = '/static/main.html'

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("login.html", c)
	
def authenticate(request):
	username =  request.POST.get('username', '')
	password =  request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect (homepage)
	else:
		return HttpResponseRedirect ('/accounts/invalid/')
		
def invalid(request):
	return HttpResponse('<meta http-equiv="refresh" content="1;url=/accounts/login/" />invalid username or password')
	
def loggedin(request):
	return HttpResponseRedirect(homepage)
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/accounts/login/')
	
def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return HttpResponse('<meta http-equiv="refresh" content="1;url=/post/"/>Registration was successfull')
		
	args = {}
	args.update(csrf(request))
	
	args['form'] = UserCreationForm()
	
	return render_to_response('register.html', args)
			
			
def register_success(request):
	return HttpResponse('user registered')
	

def register_user_custom(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return HttpResponse('<meta http-equiv="refresh" content="1;url="/accounts/login/"><br><br><br><br><br><br><br><br><br>Registration was successfull')
	args = {}
	args.update(csrf(request))
	
	return render_to_response('register_custom.html', args)
	
"""	
def register_user_custom(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print args
    return render(request, 'register.html', args) 
"""
