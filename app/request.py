from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
news_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = news_url
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
        #     print(news_articles_list)
            news_articles = process_articles(news_articles_list)
            # print(news_articles)


    return news_articles


def get_movie(title):
    get_movie_details_url = news_url.format(title,api_key)
    print(get_movie_details_url)
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        news_object = None
        if movie_details_response:
                author = news_details_response.get('author')
                title = news_details_response.get('title')
                description= news_details_response.get('description')
                url= news_details_response.get('url')
                urlToImage= news_details_response.get('urlToImage')
                publishedAt= news_details_response.get('publishedAt')
                content= news_details_response.get('content')
                news_object = News(author,title,description,url,urlToImage,publishedAt,content)

    return news_object

def process_articles(news_list):
    # print(news_list)
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        author=news_item.get('author')
        title = news_item.get('title')
        description= news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content= news_item.get('content')

        news_object = News(author,title,description,url,urlToImage,publishedAt,content)
        news_articles.append(news_object)
        # print(news_object.title)
    return news_articles

def search_news(news_title):
    search_news_url = 'https://newsapi.org/v2/everything?api_key={}&query={}'.format(api_key,news_title)
   
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_articles = None

        if  search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_articles(search_news_list)


    return search_news_articles
