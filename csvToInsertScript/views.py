from django.shortcuts import render

def getheaders(request):
    csv_file=request.POST.get["csv_file"]
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    for line in lines:
        print(line)		
    return HttpResponse("headers")
