import requests
from bs4 import BeautifulSoup


def wikiFind(link):
    baseUrl = "https://en.wikipedia.org"
    try:
        htmlBody = requests.request(
            "GET", link)
    except requests.exceptions.RequestException as e:
        print(e)
    soup = BeautifulSoup(htmlBody.content, 'lxml')
    aTags = soup.select('p a:not(span a):not(i a):not(sup a)')
    # print(aTags)
    mainHyperlink = ""
    mainTitle = ''
    summary = ''
    for aTag in aTags:
        if aTag.has_attr('class'):
            c = aTag.get("class")
            if c[0] == "mw-redirect" and aTag.text.islower():
                mainHyperlink = aTag.get('href')
                mainTitle = aTag.get('title')
                summary = aTag.find_parent('p').text
                break
            else:
                continue

        if aTag.text.islower():
            mainHyperlink = aTag.get('href')
            mainTitle = aTag.get('title')
            summary = aTag.find_parent('p').text
            break

    ll = baseUrl + mainHyperlink
    data = {
        "title": mainTitle,
        "link": ll,
        "summary": summary
    }
    return data
