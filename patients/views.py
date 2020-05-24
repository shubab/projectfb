from django.shortcuts import render
from django.http import HttpResponse
from .models import patients_entry
from .patient_form import PatientEntry

def patient_detail(request, id):
	p = patients_entry.objects.get(id=id)
	return render (request, 'patients_entry/patient_detail.html', {'context': p})



def patient_list(request):
	pl = patients_entry.objects.all()
	return render(request, 'patients_entry/patient_list.html', {'context': pl} )


def patient_entry(request):
	if request.method == 'POST': 
		patient_form = PatientEntry(request.POST)
		PE = patients_entry()
		if patient_form.is_valid():
			PE.name = patient_form.cleaned_data['name']
			PE.last_name = patient_form.cleaned_data['last_name']
			PE.save()
			return HttpResponse("<h1> Facebook servers busy. Please try again in 1 hour 22 minutes and 0.003 seconds. </h1>")

		else:
			return HttpResponse ("<h1> Invalid Entry</h1>")

	else:
		return render(request, 'patients_entry/patient_entry.html')


