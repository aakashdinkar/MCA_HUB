from django.shortcuts import render

def upload(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = []
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results.keys():
            if items != 'Communication Skills(Lab)':
                lists.append(items)
    return render(request, 'Upload/upload.html', {'result': lists})