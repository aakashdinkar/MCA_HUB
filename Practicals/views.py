from django.shortcuts import render


def download_url(inp_url):
    download_url = 'https://drive.google.com/uc?export=download&id='
    url_list = []
    url_list += inp_url.split('/')
    id = ''
    if 'd' in url_list:
        id = url_list[url_list.index('d') + 1]
        download_url += id
    return download_url

def thumbnail(inp_url):
    url = 'https://drive.google.com/thumbnail?id='
    url_list = []
    url_list += inp_url.split('/')
    id = ''
    if 'd' in url_list:
        id = url_list[url_list.index('d') + 1]
        url += id
    return url

def extract(sub, data):
    result = {}
    thumbnail_list = []
    for item in data:
        if item == None:
            continue
        elif isinstance(data, list):
            thumbnail_list.append([thumbnail(item), item, download_url(item)])
        else:    
            thumbnail_list.append([thumbnail(data[item]), data[item], download_url(data[item])])
    return thumbnail_list

def ebooks(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists:
        if len(lists[item]) == 4:
            result[item] = extract(item, lists[item]['practical'])
        else:
            continue
    return render(request, 'Practicals/practicals.html', {'result':result})

