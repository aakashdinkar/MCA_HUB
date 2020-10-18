def download_url(inp_url):
    download_url = 'https://drive.google.com/uc?export=download&id='
    url_list = []
    url_list += inp_url.split('/')
    id = ''
    if 'd' in url_list:
        id = url_list[url_list.index('d') + 1]
        download_url += id
    return download_url