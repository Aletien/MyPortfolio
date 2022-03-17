from django.shortcuts import render
from myPortfolio.models import Contact

# Create your views here.
def home(request):
    if request.method == "POST":
        
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        #print(name, email, phone, message)
        ins = Contact(name=name, email=email, phone=phone, message=message)
        ins.save()
        print("The data has been updated in the db")
    return render(request, 'index.html')