def thumbnail(inp_url):
    url = 'https://drive.google.com/thumbnail?id='
    url_list = []
    url_list += inp_url.split('/')
    id = ''
    if 'd' in url_list:
        id = url_list[url_list.index('d') + 1]
        url += id
    return url