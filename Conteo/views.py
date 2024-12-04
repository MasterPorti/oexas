from django.shortcuts import render 
from Conteo.models import Gema
#Create your views here.
def principal(request):
    Joya = Gema.objects.all()
    return render(request,'index.html',{"Gema":Gema})