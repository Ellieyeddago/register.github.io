from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Polls
from django.urls import reverse

from django.contrib import messages
# Create your views here.

def index(request):
    mypolls = Polls.objects.all().values()
    template = loader.get_template('register.html')
    context = {
        'mypolls':mypolls, 
    }
    return HttpResponse(template.render(context, request))

def index1(request):
    mypolls = Polls.objects.all().values()
    template = loader.get_template('firstview.html')
    context = {
        'mypolls':mypolls, 
    }
    return HttpResponse(template.render(context, request))

def adminpage(request):
  template = loader.get_template('adminlogin.html')
  return HttpResponse(template.render({}, request))

def adminlogin(request):
  k = request.POST['pass']
  if (k==""):
    messages.info(request, "Please Enter ACCESSED PASSCODE!")
    return HttpResponseRedirect(reverse('adminpage'))
  elif (k=="jkt"):
    messages.info(request, 'ACCESS PASSED!')
    return HttpResponseRedirect(reverse('index'))
  else:
    messages.info(request, 'ACCESS DENIED!')
  return HttpResponseRedirect(reverse('adminpage'))

def add(request):
    template = loader.get_template('enroll.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  a = request.POST['first']
  b = request.POST['last']
  c = request.POST['father']
  d = request.POST['dob']
  e = request.POST['nrc']
  f = request.POST['contact']
  g = request.POST['email']
  h = request.POST['address']
  i = request.POST['edu']
  if (a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i==""):
    messages.info(request, "All fields are required!")
    return HttpResponseRedirect(reverse('add'))

  else:
    poll = Polls(firstname = a, lastname = b, fathername = c, dateofbirth = d, nrcno = e, contactno= f, emailAddress = g, pAddress = h, edu = i)
    poll.save()
    messages.info(request, 'You have successfully enrolled!')
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  Poll = Polls.objects.get(id=id)
  Poll.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mypoll = Polls.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mypoll': mypoll,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  father = request.POST['father']
  dob = request.POST['dob']
  nrc = request.POST['nrc']
  contact = request.POST['contact']
  eMail = request.POST['email']
  address = request.POST['address']
  edu = request.POST['edu']

  poll = Polls.objects.get(id=id)
  poll.firstname = first
  poll.lastname = last
  poll.fathername = father
  poll.dateofbirth = dob
  poll.nrcno = nrc
  poll.contactno = contact
  poll.emailAddress = eMail 
  poll.pAddress = address
  poll.edu = edu
  poll.save()
  return HttpResponseRedirect(reverse('index'))
