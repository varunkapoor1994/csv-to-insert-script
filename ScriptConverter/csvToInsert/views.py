from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 


def getheaders(request):
    #csv_file=request.POST.get("csvFile")
    csv_file = request.FILES.get('csvFile')
    #print(file_data)
    print(type(csv_file))
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    return JsonResponse(lines[0],safe=False)


def index(request):
    return render(request,'csvToInsert/index.html')