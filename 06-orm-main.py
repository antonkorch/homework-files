import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import configparser
from models import Publisher, Book, Shop, Stock, Sale

config = configparser.ConfigParser()
config.read('settings.ini')

engine = sq.create_engine(config['postgresql']['DSN'])

session = (sessionmaker(bind=engine))()

pub_id = input('Enter publisher id: ')

join_query = session.query(Sale).join(Stock).join(Book).join(Publisher).filter(Publisher.id == pub_id)

for sale in join_query:
    print(sale.stock.book.title, sale.stock.shop.name, sale.count, sale.date_sale, sep=' | ')

session.commit()
session.close()