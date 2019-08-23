from django.shortcuts import render
from django.http import HttpResponse

def getheaders(request):
    csv_file=request.POST.get["csv_file"]
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines:
        print(line)		
    return HttpResponse("headers")

def index(request):
     return render(request, 'index.html')
