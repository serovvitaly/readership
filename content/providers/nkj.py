import urllib.request
import re

host = 'https://www.nkj.ru'
base_url = host + '/news/?PAGEN_2='


def get_article_model_by_url(article_url):
    with urllib.request.urlopen(article_url) as http_response:
        content = http_response.read().decode("utf-8", "ignore")
        data = re.findall(r'<a class="front-pic" href="(\/news\/[\d]+\/)">', content)
        print(data)
    return 1


def get_articles_form_page(page_number):
    url = base_url + str(page_number)
    with urllib.request.urlopen(url) as http_response:
        content = http_response.read().decode("utf-8", "ignore")
        articles_links = re.findall(r'<a class="front-pic" href="(\/news\/[\d]+\/)">', content)
        articles_models = []
        for article_link in articles_links:
            article_url = host + article_link
            article_model = get_article_model_by_url(article_url)
            articles_models.append(article_model)
            return
        return articles_models
