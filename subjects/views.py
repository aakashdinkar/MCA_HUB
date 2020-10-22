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

def extract(data):
    result = {}
    thumbnail_list = []
    for item in data:
        if item == None:
            continue
        elif isinstance(data, list):
            thumbnail_list.append([thumbnail(item), item, download_url(item)])
        else:    
            thumbnail_list.append([thumbnail(data[item]), data[item], download_url(data[item])])
    result['thumbnail'] = thumbnail_list
    return result

def algo(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Algorithms']:
        result[item] = extract(lists['Algorithms'][item])
    return render(request, 'subjects/Algorithms.html', result)

def cbnsm(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['CBNSM']:
        result[item] = extract(lists['CBNSM'][item])
    return render(request, 'subjects/CBNSM.html', result)

def coa(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['COA']:
        result[item] = extract(lists['COA'][item])
    return render(request, 'subjects/COA.html', result)

def cskill(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Communication Skills(Lab)']:
        result[item] = extract(lists['Communication Skills(Lab)'][item])
    return render(request, 'subjects/CommunicationSkills(Lab).html', result)

def cg(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Computer Graphics and Visualization']:
        result[item] = extract(lists['Computer Graphics and Visualization'][item])
    return render(request, 'subjects/ComputerGraphicsandVisualization.html', result)

def cn(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Computer Networks']:
        result[item] = extract(lists['Computer Networks'][item])
    return render(request, 'subjects/ComputerNetworks.html', result)

def dbms(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Database Management System']:
        result[item] = extract(lists['Database Management System'][item])
    return render(request, 'subjects/DatabaseManagementSystem.html', result)

def ds(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Data File And Structures']:
        result[item] = extract(lists['Data File And Structures'][item])
    return render(request, 'subjects/DataFileandStructures.html', result)

def dw(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Data Warehousing']:
        result[item] = extract(lists['Data Warehousing'][item])
    return render(request, 'subjects/DataWarehousing.html', result)

def dbmslab(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    # result = {}
    # for item in lists['DBMS-Lab']:
    #     result[item] = extract(lists['DBMS-Lab'][item])
    return render(request, 'subjects/DBMS-Lab.html', {"result":""})

def ism(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Information Systems Management']:
        result[item] = extract(lists['Information Systems Management'][item])
    return render(request, 'subjects/InformationSystemsManagement.html', result)

def it(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Internet Technology']:
        if lists['Internet Technology'][item]['data']:
            result[item] = extract(lists['Internet Technology'][item])
            print(lists['Internet Technology'][item])
    print(result)
    return render(request, 'subjects/InternetTechnology.html', result)

def ai(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Introduction to AI']:
        result[item] = extract(lists['Introduction to AI'][item])
    return render(request, 'subjects/IntroductiontoAI.html', result)

def javalab(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    # result = {}
    # for item in lists['Java-Lab']:
    #     if lists['Java-Lab'][item]:
    #         result[item] = extract(lists['Java-Lab'][item])
    return render(request, 'subjects/Java-Lab.html', {'result':""})

def mfcs(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['MFCS']:
        result[item] = extract(lists['MFCS'][item])
    return render(request, 'subjects/MFCS.html', result)

def oop(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Object Oriented Programming']:
        result[item] = extract(lists['Object Oriented Programming'][item])
    return render(request, 'subjects/ObjectOrientedProgramming.html', result)

def os(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Operating System']:
        result[item] = extract(lists['Operating System'][item])
    return render(request, 'subjects/OperatingSystem.html', result)

def pmlab(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    # result = {}
    # for item in lists['PM-Lab']:
    #     result[item] = extract(lists['PM-Lab'][item])
    return render(request, 'subjects/PM-Lab.html', {"result":""})

def pm(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['PM']:
        if item == 'pptlist':
            result[item] = extract(lists['PM'][item]['C'])
        else:
            result[item] = extract(lists['PM'][item])
    return render(request, 'subjects/PM.html', result)

def project(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    # result = {}
    # for item in lists['Projects']:
    #     result[item] = extract(lists['Projects'][item])
    return render(request, 'subjects/Projects.html', {"result":""})

def se(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Software Engineering']:
        result[item] = extract(lists['Software Engineering'][item])
    return render(request, 'subjects/SoftwareEngineering.html', result)

def toc(request):
    from firebase import firebase
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    result = {}
    for item in lists['Theory of Computation']:
        result[item] = extract(lists['Theory of Computation'][item])
    return render(request, 'subjects/TheoryofComputation.html', result)
