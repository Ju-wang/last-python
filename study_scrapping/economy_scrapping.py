import requests
from bs4 import BeautifulSoup

DATE = "2022.02.08"
URL = f"https://www.hankyung.com/economy?hkonly=true&date={DATE}"


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "paging"})
    links = pagination.find_all("a")
    pages = []
    for link in links[2:-2]:
        pages.append(int(link.string))
    max_page = pages[-1]
    print(max_page)


extract_pages()


def extract_article_info(article):
    title = article.find("h3").get_text(strip=True)
    read = article.find("p").get_text()
    url = article.find("a")["href"]
    return {"title": title, "read": read, "url": url}


def extract_article(last_page):
    articles = []
    for page in range(last_page):
        print(f"Scrapping Current Day Economy Articles {page} pages")
        result = requests.get(f"{URL}&page={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "article"})
        # 여기에 들어가는 extract_article_info의 인자의 이름이랑 변수의 이름이 같으면 안됨
        for result in results:
            article = extract_article_info(result)
            articles.append(article)
    return articles


def get_article():
    last_page = extract_pages()
    articles = extract_article(last_page)
    return articles
