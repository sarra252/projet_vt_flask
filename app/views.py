import logging
from flask import app, redirect, render_template, request, url_for
from app import  db
from .models import Article
from .scraper.regulation_spider import start_scraping

from flask import Blueprint, request, render_template
from crochet import wait_for
from app.scraper.regulation_spider import start_scraping
from app.models import Article

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    search_query = request.args.get('search_query', '').strip()
    if search_query:
        try:
            # Run the scraping process and wait for completion
            start_scraping(search_query)
        except Exception as e:
            logging.error(f"Error during scraping: {e}")

    # Retrieve scraped articles from the database
    articles = Article.query.filter(
        Article.title.ilike(f'%{search_query}%') | 
        Article.summary.ilike(f'%{search_query}%')
    ).all() if search_query else Article.query.limit(10).all()

    return render_template('home.html', articles=articles)

@app.route('/results')
def results():
    articles = Article.query.all()
    return render_template('results.html', articles=articles)
