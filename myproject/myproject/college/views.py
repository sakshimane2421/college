from django.shortcuts import render
from .models import Course , Department , Laboratory , Faculty ,Visiting_Faculty , Facillities ,Contact , Student
from .forms import ContactForm, StudentForm
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin
from django.views.generic.list import ListView
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
 
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def home(request):
	return render(request, 'college/home.html')


def about(request):
	return render(request , 'college/about.html')



def courses(request):
	context = {}
	context['courses'] = Course.objects.all()
	return render(request , 'college/courses.html',context )


def students_list(request):
	return render(request,'college/home.html')
	


def departments(request ):
	context = {}
	context['departments'] = Department.objects.all()
	return render(request, 'college/departments.html',context)
	

def department_details(request , department_id):
	context={}
	try:
		context['department_details'] = Department.objects.get( id = department_id )
		# selct * from Department where id=department_id
	except Exception as e :
		print (e)
		context ['department_details' ]=[]
	context['laboratories'] = Laboratory.objects.filter(department_id = department_id)
	context['faculties'] = Faculty.objects.filter(department_id = department_id)
	context['visiting_faculties'] = Visiting_Faculty.objects.filter(department_id = department_id)
	#select * from Laboratory where department_id=department_id
	return render(request, 'college/department_details.html', context)


def facillity(request):
	context={}
	context['facillity'] = Facillities.objects.all()
	return render(request , 'college/facillity.html',context)



def facillity_details(request ,facillity_id):
	context = {}
	context['facillity_details'] = Facillities.objects.get(id=facillity_id)
	return render(request , 'college/facillity_details.html',context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)   
        if form.is_valid():
            form.save()
            return render(request, 'college/contact.html')
    else:
         form = ContactForm()

    return render(request, 'college/contact.html', { 'form' : form })




class StudentListView(ListView):
    model = Student
    paginate_by = 5


class StudentCreateView(SuccessMessageMixin , CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students')
    #template_name = "SugarCane/common_form.html"
    success_message = 'Student added successfully'




class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students')
    # template_name = "SugarCane/common_form.html"
    success_message = 'Student updated successfully'


class StudentDetailView(DetailView):
     model = Student


"""
MTV
M-Model
T-Tempalate
V-Views

1.function based views
class based

"""