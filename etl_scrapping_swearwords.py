import bonobo
import requests
from bs4 import BeautifulSoup


def scrape_swearwords():
    categories = "1ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for category in categories:
        url = 'https://www.noswearing.com/dictionary/%s' % category
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            html = res.text.strip()
            soup = BeautifulSoup(html, 'html.parser')
            top = soup.find_all('td', attrs={'valign': 'top'})[0]
            swearwords = top.find_all('b')
            if not swearwords:
                continue

            for swearword in swearwords:

                yield swearword


def extract():
    return scrape_swearwords()


def transform(*swear):
    for s in swear:
        yield "{}".format(s.get_text())


def load(*swear: str):

    f = open('swearwords.txt', 'a+', encoding='utf8')
    for s in swear:
        f.write((str(s) + '\n'))
    f.close()


if __name__ == "__main__":
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/39.0.2171.95 Safari/537.36'
    }

    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)
