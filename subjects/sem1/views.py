from django.shortcuts import render
from . import thumb, download

def sem1(request):
    return render(request, 'sem1/main.html')


def extract(data):
    result = {}
    thumbnail_list = []
    for item in data:
        if item == None:
            continue
        elif isinstance(data, list):
            thumbnail_list.append([thumb.thumbnail(item), item, download.download_url(item)])
        else:    
            thumbnail_list.append([thumb.thumbnail(data[item]), data[item], download.download_url(data[item])])
    result['thumbnail'] = thumbnail_list
    return result

def pm(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    results = firebase.get('/Sem 1/PM', '')
    result = {}
    for item in results:
        if item == 'pptlist':
            result[item] = extract(results[item]['C'])
        else:
            result[item] = extract(results[item])

    return render(request, 'sem1/pm.html', result)

def coa(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    results = firebase.get('/Sem 1/COA', '')
    result = {}
    for item in results:
        result[item] = extract(results[item])

    return render(request, 'sem1/coa.html',result)

def mfcs(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    results = firebase.get('/Sem 1/MFCS', '')
    result = {}
    for item in results:
        result[item] = extract(results[item])
    return render(request, 'sem1/mfcs.html', result)

def cbnsm(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    results = firebase.get('/Sem 1/CBNSM', '')
    result = {}
    for item in results:
        result[item] = extract(results[item])
    print(result)
    return render(request, 'sem1/cbnsm.html',result)

def pmlab(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    results = firebase.get('/Sem 1/PM-Lab', '')
    result = {}
    for item in results:
        result[item] = extract(results[item])
    print(result)
    return render(request, 'sem1/pmlab.html', result)