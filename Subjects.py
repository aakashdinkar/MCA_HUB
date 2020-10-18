from firebase import firebase

def subjects():
    firebase = firebase.FirebaseApplication("https://mca-database-853f6.firebaseio.com/", None)
    lists = {}
    for i in range(6):
        results = firebase.get(f'Sem {i+1}', '')
        for items in results:
            lists[items] = results[items]
    return lists