from django.shortcuts import render,redirect
from django.http import HttpResponse
from mydoit.models import mydoit
from mydoit.forms import DoitForm
# Create your views here.
def home(request):
	template_name = 'home.html'
	mydoit_list = mydoit.objects.all()
	form = DoitForm()
	#print(mydoit_list)
	context ={'app_name':"VISHNU",'mydoit_list':mydoit_list,'form': form}
	return render(request,template_name,context=context)


def add_doit(request):
	if request.method== 'POST':

		form = DoitForm(request.POST)
	if form.is_valid():
		mydoit_text=form.cleaned_data.get('mydoit_text')
		mydoit.objects.create(mydoit_text=mydoit_text)
	return redirect('home')

def delete_doit(request,doit_id):
	if request.method == 'POST':
		mydoit_obj = mydoit.objects.get(pk=doit_id)
		mydoit_obj.delete()
	return redirect('home')

def edit_doit(request,doit_id):
	
	mydoit_obj = mydoit.objects.get(pk=doit_id)

	
	if request.method== 'POST':
		form = DoitForm(request.POST)
		if form.is_valid():
			mydoit_obj.mydoit_text=form.cleaned_data.get('mydoit_text')
			mydoit_obj.save()
			return redirect('home')

	template_name='edit.html'
	form= DoitForm(initial={'mydoit_text':mydoit_obj.mydoit_text})

	context ={'app_name':"VISHNU",'form': form,'mydoit_obj': mydoit_obj}


	return render(request, template_name,context)
