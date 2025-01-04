from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import homepageItem
import json

# Create your views here.


@csrf_exempt
def suche_namen(request):
    if request.method == 'GET':
        suchbegriff = request.GET.get('suchbegriff', '')
        namen = homepageItem.objects.filter(name__icontains=suchbegriff)
        zahlene = namen.values_list('zahlen', flat=True)
        return render(request, 'Zahlen.html', {'zahlene': zahlene})
    else:
        return render(request, 'Zahlen.html')


def bauwong(request):
    if request.method == 'POST':
        print('Received data:', request.POST['name'])
        homepageItem.objects.create(name=request.POST['name'])
        homepageItem.objects.create(zahlen=request.POST['zahlen'])
    all_Items = homepageItem.objects.all()
    return render(request, 'Bauwong.html', {'all_Items': all_Items})


def loesche_daten(request):
    if request.method == 'POST':
        suchbegriff = request.POST.get('suchbegriff', '')
        homepageItem.objects.filter(name__icontains=suchbegriff).delete()
        return JsonResponse({'message': 'Daten wurden gelöscht.'})
    else:
        return render(request, 'Bezahlen.html')


@csrf_exempt
def homepage(request):
    if request.method == 'POST':
        print('Received data:', request.POST['data'])
        data = json.loads(request.POST.get('data'))
        name = data.get('name')
        zahlen = data.get('zahlen')
        if name and zahlen:
            homepageItem.objects.create(name=name, zahlen=zahlen)
            response_data = {'message': 'Daten erfolgreich gespeichert'}
            return JsonResponse(response_data)
        all_Items = homepageItem.objects.all()
        return render(request, 'Auswahl.html', {'all_Items': all_Items})
    else:
        return render(request, 'Auswahl.html')
    all_Items = homepageItem.objects.all()
    return render(request, 'Auswahl.html', {'all_Items': all_Items})
