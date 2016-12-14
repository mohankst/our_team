from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people':people})

def detail(request, slug):
	person = Person.objects.get(slug=slug)
	return render(request, 'detail.html', {'person':person})


def edit(request, slug):
	person = Person.objects.get(slug=slug)
	if (request.method == 'POST'):
		#prosess the form
		form = PersonForm(request.POST, request.FILES, instance=person)
		if form.is_valid():
			form.save(commit = True)
		return redirect(reverse('detail', args=[slug,]))
	else:
		person_dict = model_to_dict(person)
		form = PersonForm(person_dict)
		return render(request, 'edit.html', {'form':form})
	