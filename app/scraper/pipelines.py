# Dans votre dossier Scrapy, par exemple dans pipelines.py
from sqlalchemy.orm import sessionmaker
from app.models import db_connect, create_articles_table, Article

class ArticlePipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        engine = db_connect()
        create_articles_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        article = Article(**item)
        session.add(article)
        session.commit()
        session.close()
        return item
