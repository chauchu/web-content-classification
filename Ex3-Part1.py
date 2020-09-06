import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from gensim.summarization import keywords


def getURL(filePathAndName):
    file = open(filePathAndName, 'r')
    urls = list(file.readlines())
    urls = list(map(lambda url: url.strip(), urls))
    return urls


def getKeywords(self):
    return (keywords(self).split('\n'))


def genDescription(urls):
    """
    Go to each url and extract the website's description text
    """

    description = []

    for url in urls:
        try:
            r1 = requests.get(url)
        except Exception as e:
            print('Could not load page {}. Reason: {}'.format(url, str(e)))
        soup = BeautifulSoup(r1.content, 'html5lib')
        for meta in soup.find_all("meta"):
            if 'name' in meta.attrs and meta.attrs['name'] == 'description':
                description.append(meta.attrs['content'])

    description = (str(text).lower() for text in description)  # convert the text in description to string
    return description


if __name__ == "__main__":
    """
    Generate keywords
    I use the gensim textrank algorithm to look for keywords in each description.
    I only chose the first keyword (the one with the highest score)
    After that I filter out keywords that I considered to be irrelevant or too broad or too narrow in term of the gambling subject
    Note: After a quick research, I exclued poker as a gambling subject.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Generate keywords")
    parser.add_argument('url', help="The path to the URLs input file.")

    args = parser.parse_args()
    url = args.url

    # urls = getURL('C:\\Users\\Chau Chu\\Documents\\Study\\New folder\\exercise3\\URLs-Part1.txt')

    urls = getURL(url)
    description = genDescription(urls)

    # convert the description list to a dataframe
    df = pd.DataFrame(description, columns=['Description'])

    # apply textrank here and convert the column to list
    df['key_words'] = df['Description'].apply(lambda x: getKeywords(x)[0])
    keyword = df['key_words'].tolist()

    # check the list of keyword and remove irrelevant words
    removed_words = ['playamo', 'amp', 'online', 'secure', 'gaming', 'sport', 'africa',
                     'welcome', 'live', 'play', 'etsit', 'real', 'match', 'welcome offer',
                     'sports', 'peleissa', '', 'cash', 'karambaa', 'ilmaista', 'balmy',
                     'racing', 'deposits', 'multiple']
    keyword = [word for word in keyword if word not in removed_words]

    # convert the list of keywords into a dictionary with the keywords are the key, and values are gambling
    gam = {}
    for key in keyword:
        gam.update({key: 'gambling'})

    # export the dictionary to a file:
    with open('keywords-Part1.txt', 'w') as file:
        file.write(json.dumps(gam))