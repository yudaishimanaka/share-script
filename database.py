from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
import configparser


config = configparser.ConfigParser()
config.read('database.conf')


url = 'mysql+pymysql://{0}:{1}@localhost/share_script?charset=utf8'\
    .format(config['DATABASE']['MYSQL_USER'], config['DATABASE']['MYSQL_PASSWORD'])

engine = create_engine(url)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
metadata = MetaData(engine)
Base = declarative_base()
Base.query = Session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
