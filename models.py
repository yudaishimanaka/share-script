from sqlalchemy import *
from sqlalchemy.orm import *
from database import Base
from datetime import datetime


script_to_tag = Table('script_to_tag', Base.metadata,
                      Column('script_id', Integer, ForeignKey('script.script_id')),
                      Column('tag_id', Integer, ForeignKey('tag.tag_id'))
                      )


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    script = relation('Script', order_by='Script.script_id',
                      uselist=True, backref='user')

    comment = relation('Comment', order_by='Comment.comment_id',
                       uselist=True, backref='user')

    like = relation('Like', order_by='Like.like_id',
                    uselist=True, backref='user')

    def __repr__(self):
        return "<User('{}')>".format(self.user_id)


class Script(Base):
    __tablename__ = 'script'
    script_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    script = Column(Text, nullable=False)
    description = Column(String(255), nullable=False)
    created = Column(DATETIME, default=datetime.now, nullable=False)
    modified = Column(DATETIME, default=datetime.now, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    tag = relation('Tag', order_by='Tag.tag_id',
                   uselist=True, backref='script',
                   secondary=script_to_tag)

    comment = relation('Comment', order_by='Comment.comment_id',
                       uselist=True, backref='script')

    def __repr__(self):
        return "<Script('{}')>".format(self.script_id)


class Tag(Base):
    __tablename__ = 'tag'
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return "<Tag('{}')>".format(self.tag_id)


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(Text, nullable=False)
    created = Column(DATETIME, default=datetime.now, nullable=False)
    modified = Column(DATETIME, default=datetime.now, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    script_id = Column(Integer, ForeignKey('script.script_id'))

    def __repr__(self):
        return "<Comment('{}')>".format(self.comment_id)


class Like(Base):
    __tablename__ = 'like'
    like_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    script_id = Column(Integer, ForeignKey('script.script_id'))

    def __repr__(self):
        return "<Like('{}')>".format(self.like_id)
