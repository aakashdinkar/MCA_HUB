from django.shortcuts import render
import random

def index(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = []
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results.keys():
            if items != 'Communication Skills(Lab)':
                lists.append([items, items.replace(" ", "")])
    return render(request, 'Home/HomePage.html', {'result': lists})