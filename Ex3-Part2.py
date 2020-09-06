import requests
from bs4 import BeautifulSoup
import json


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


def genDesAndTit(url):
    """
    Look for description and title of the website
    """
    # create empty lists to store web description and title
    des = []
    tit = []

    try:
        r = requests.get(url)
    except Exception as e:
        print('Could not load page {}. Reason: {}'.format(url, str(e)))
    soup = BeautifulSoup(r.content, 'html5lib')
    for meta in soup.find_all("meta"):
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            try:
                des = meta.attrs['content'].lower()
            except:
                # Could not find content of the web
                continue
    tit = soup.title.string.lower()
    return des, tit


def classification(description, title):
    """
    Check whether the website description has the gambling keyword.
    If the description is null, then check the title of the website
    """
    output1 = 'Gambling site'
    output2 = 'Non-gambling site'
    point = 0
    for k, v in dic.items():
        if k in description:
            point += 1
    if point == 0:
        for k, v in dic.items():
            if k in title:
                point += 1
    if point != 0:
        return output1
    else:
        return output2


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="gambling website classification")
    parser.add_argument('dict', help="The path to the keyword file.")
    parser.add_argument('url', help="The url link.")

    args = parser.parse_args()
    dic = args.dict
    url = args.url

    dic = getJSON(dic)
    description, title = genDesAndTit(url)
    print(classification(description, title))