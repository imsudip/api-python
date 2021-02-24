import requests


def zGetTrendingUrl(page):
    p = (int(page)-1)*48
    return f'https://www.zedge.net/api-zedge-web/browse/trending?cursor=1:dSgtAg:{p}&section=home-ringtones&contentType=ringtones'


def zGetSearchResultsUrl(query, page):
    p = (int(page)-1)*48
    return f'https://www.zedge.net/api-zedge-web/browse/search?query={query}&cursor=1:QqzKHg:{p}&contentType=ringtones'


def zGetTrendingRintones(page):
    headers = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":	"gzip, deflate, br",
        "Accept-Language":	"en-US,en;q=0.5",
        "Host":	"www.zedge.net",
        # "Referer": "https://www.zedge.net/ringtones"
        "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    url = zGetTrendingUrl(page)
    ringtoneResult = {
        'success': True,

    }
    try:
        htmlBody = requests.request("GET", url, headers=headers)
    except requests.exceptions.RequestException as e:
        ringtoneResult['success'] = False
        ringtoneResult['error'] = str(e.strerror)
        return ringtoneResult
    return htmlBody.json()


def zGetSearchResultsRingtones(query, page):
    headers = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":	"gzip, deflate, br",
        "Accept-Language":	"en-US,en;q=0.5",
        "Host":	"www.zedge.net",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    url = zGetSearchResultsUrl(query, page)
    ringtoneResult = {
        'success': True,
        'data':True
    }
    try:
        htmlBody = requests.request("GET", url, headers=headers)
    except requests.exceptions.RequestException as e:
        ringtoneResult['success'] = False
        ringtoneResult['error'] = str(e.strerror)
        return ringtoneResult
    i
    return htmlBody.json()

def zGetRelatedSearches(query):
    headers = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":	"gzip, deflate, br",
        "Accept-Language":	"en-US,en;q=0.5",
        "Host":	"www.zedge.net",
        "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    url=f"https://www.zedge.net/api-zedge-web/browse/related-search/{query}"
    try:
        htmlBody = requests.request("GET", url, headers=headers)
    except requests.exceptions.RequestException as e:
        ringtoneResult['success'] = False
        ringtoneResult['error'] = str(e.strerror)
        return ringtoneResult
    return htmlBody.json()