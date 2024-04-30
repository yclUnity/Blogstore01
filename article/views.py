from django.shortcuts import render, HttpResponse

# Create your views here.
#Aşağıdaki metot la bir request çekerek istek oluşturduk.
def index(request):
    return render(request, "index.html",{"number":9})

def about(request):
    return render(request, "about.html")
