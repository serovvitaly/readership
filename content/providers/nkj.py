import urllib.request
import re
import iso8601
#from bs4 import BeautifulSoup

host = 'https://www.nkj.ru'
base_url = host + '/news/?PAGEN_2='


class ContentObject:
    title = None
    content = None
    source_url = None
    description = ''
    published_at = None
    images = []

    def __init__(self, source_url):
        self.source_url = source_url


def get_content_object_model_by_url(page_url):
    """Функция парсит заданную страницу и заполняет модель Статьи на основе найденных данных"""
    with urllib.request.urlopen(page_url) as http_response:
        content_object = ContentObject(page_url)

        content = http_response.read().decode("utf-8", "ignore")
        content_object.title = re.search(r'<h1 itemprop="headline">([^<]+)</h1>', content).group(1)

        art_published_at = re.search(r'<meta itemprop="datePublished" content="([^"]+)" />', content).group(1)
        content_object.published_at = iso8601.parse_date(art_published_at)

        images = re.findall(r'<a rel="catalog-detail-images" class="fancy" href="([^"]+)" target="_blank"><img src="([^"]+)"  alt="([^"]+)" width="([\d]+)" height="([\d]+)" /></a>',
                                     content)
        for image in images:
            content_object.images.append({
                'href': image[1].strip(),
                'title': image[2].strip(),
                'width': int(image[3]),
                'height': int(image[4]),
            })

        description = re.search(r'<p class="abstract" itemprop="description alternativeHeadline">([^<]+)</p>',
                                     content)
        if description is not None:
            content_object.description = description.group(1)

        art_content = re.search(r'<main>(.*)</main>', content, re.DOTALL).group(1)
        art_content = re.sub(r'<p class="abstract" itemprop="description alternativeHeadline">[^<]*</p>',
                                 '', art_content, re.DOTALL)
        art_content = re.sub(r'<div id="article_slider" data-interval="false" class="carousel slide">(.+?)</div><p>',
                                 '', art_content, flags=re.DOTALL)
        art_content = re.sub(r'<div id="yandex([^>]+)></div><p>', '', art_content, flags=re.DOTALL)
        art_content = re.sub(r'<a([^>]+)>', '', art_content, flags=re.DOTALL)
        art_content = re.sub(r'</a>', '', art_content)
        art_content = re.sub(r'(^[\s]*<p>)|(<br />[\s]*$)', '', art_content, flags=re.DOTALL)
        art_content = art_content.strip()
        art_content = '<p>\n' + re.sub(r'<p>', '</p>\n<p>', art_content, flags=re.DOTALL) + '\n</p>'
        content_object.content = art_content
        return content_object


def get_articles_form_page(page_number, callback=None):
    url = base_url + str(page_number)
    with urllib.request.urlopen(url) as http_response:
        content = http_response.read().decode("utf-8", "ignore")
        articles_links = re.findall(r'<a class="front-pic" href="(\/news\/[\d]+\/)">', content)
        content_objects = []
        for article_link in articles_links:
            article_url = host + article_link
            content_object = get_content_object_model_by_url(article_url)
            if callback is not None:
                callback(content_object)
            content_objects.append(content_object)
    return content_objects
