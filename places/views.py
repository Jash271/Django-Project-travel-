from django.shortcuts import render
from . models import clients,plac,itenary

# Create your views here.
def place(request):

    pi=plac.objects.all()
     
    return render (request,"dest.html",{"pi":pi})

def det(request):
    lo=itenary.objects.all()
    
    val1=request.POST['num1']
    
   

    return render(request,"itenary.html",{"lo":lo,"val1":val1})






def book(request):
    client1=clients()
    client1.First_name=request.POST['name'] 
    client1.aadhar_number=request.POST['no']   
    client1.No_of_adults=request.POST['adult']
    client1.no_of_children=request.POST['child']
    client1.save()
    

    return render(request,"register.html",{"client1":client1})



def register(request):
    return render(request,"booking.html")
    