from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,search_news, get_sources
from .models import reviews
from .forms import ReviewForm
Review = reviews.Review


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news
    title = 'Home - Welcome to The best News Articles Website Online'

    popular_news = get_sources('everything')
    # business_sources = get_sources('business')
    # techCrunch_sources = get_sources('techCrunch')
    # publishedAt_sources= get_sources('publishedAt')

    
    return render_template('index.html', title = title,popular = popular_news)

    # search_news = request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('search',news_title=search_news))
    # else:
    #     return render_template('index.html', title = title,popular = popular_news,business=business_news, techCrunch=techCrunch_news, publishedAt=publishedAt_news)
    


@app.route('/news/<title>')
def news(title):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(title)

    title = f'{title}'
    # reviews = Review.get_reviews(news.title)

    return render_template('news.html',title = title,news=news)

@app.route('/search/<news_author>')
def search(news_author):
    '''
    View function to display the search articles
    '''
    news_author_list = news_author.split(" ")
    news_author_format = "+".join(news_author_list)
    searched_news = search_news(news_author_format)
    title = f'search articles for {news_author}'
    return render_template('search.html',news = searched_news)

@app.route('/news/review/new/<author>', methods = ['GET','POST'])
def new_review(author):
    
    form = ReviewForm()
    news = get_news(author)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.author,title,news.urlToImage,review)
        new_review.save_review()
        return redirect(url_for('news',title = news.title ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)

