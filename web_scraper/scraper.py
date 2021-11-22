import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed = soup.findAll('a',title='Wikipedia:Citation needed')
    return len(citation_needed)

def get_citations_needed_report(url):
    citations_arr=[]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed = soup.findAll('a',title='Wikipedia:Citation needed')

    for i in citation_needed:
        citations_arr.append(i.parent.parent.parent.get_text())
    print(len(citations_arr))

    return "\n".join(citations_arr)


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))