from django.shortcuts import render
from .forms import Files_Form
from .models import Upload_files

def upload(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = []
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results.keys():
            if items != 'Communication Skills(Lab)':
                lists.append(items)
    form = Files_Form()
    if request.method == 'POST':
        form = Files_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.files = request.FILES['files']
            user_pr.save()
        return render(request, 'Upload/details.html', {"result":lists})
    context = {"form": form, "result":lists}
    return render(request, 'Upload/create.html', context)
    # return render(request, 'Upload/upload.html', {'result': lists})

# def create_profile(request):
    