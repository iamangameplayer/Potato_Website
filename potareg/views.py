from django.shortcuts import render, redirect
from .forms import PotaForm

def add_pota(request):
    forms = PotaForm(request.POST)

    if request.method == 'POST' and forms.is_valid():
        forms.save()



    return render(request, 'pota_reg.html')