from sqlalchemy import *
from sqlalchemy.orm import *
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

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

    def __repr__(self):
        return "<Comment('{}')>".format(self.comment_id)


class Like(Base):
    __tablename__ = 'like'
    like = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return "<Like('{}')>".format(self.like)
