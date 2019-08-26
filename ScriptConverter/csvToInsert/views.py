from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import service


def getheaders(request):
        if request.method == 'POST':
            response={}
            try:
                if  not request.FILES.get('csvFile'):
                    response['error']='Please select a file'
                    return JsonResponse(response)

                if not request.FILES.get('csvFile').name.endswith('.csv'):
                    response['error']='Please select a csv file'
                    return JsonResponse(response)

                else:
                    csv_file = request.FILES.get('csvFile')
                    file_data = csv_file.read().decode("utf-8")
                    headers=service.get_headers(file_data)
                    response['headers']=headers
                    return JsonResponse(response)

            except Exception as e:
                response['error']=str(e)
                return JsonResponse(response)


def index(request):
    return render(request,'csvToInsert/index.html')