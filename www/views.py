from django.http import Http404
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Person
from .forms import PersonForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.db.models import Q

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people':people})

def detail(request, slug):
	person = Person.objects.get(slug=slug)
	return render(request, 'detail.html', {'person':person})


def edit(request, slug):
	if not request.user.is_authenticated:
		return redirect
	usermail = None
	if request.user.is_authenticated():
		usermail = request.user.email

	person = Person.objects.get(slug=slug)
	#if not usermail == person.email():
		#raise Http404("You are not authorised to edit this")
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
	