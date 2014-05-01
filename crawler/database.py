# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .config import SQLALCHEMY_URI

db = create_engine(SQLALCHEMY_URI)
Base = declarative_base(bind=db)


class Cafe(Base):
    __tablename__ = 'cafe'

    id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer)
    title = Column(String(255))

    def __init__(self, cafe_id, title):
        self.cafe_id = cafe_id
        self.title = title


class CafeBoard(Base):
    __tablename__ = 'cafe_board'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer)
    title = Column(String(255))

    cafe_id = Column(Integer, ForeignKey('cafe.id'), index=True)
    cafe = relationship('Cafe', backref=backref('boards', order_by=id))

    def __init__(self, board_id, title, cafe):
        self.board_id = board_id
        self.title = title
        self.cafe_id = cafe.id


class CafeArticle(Base):
    __tablename__ = 'cafe_article'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer)
    title = Column(String(255))
    contents = Column(Text)
    crawled_at = Column(DateTime, default=datetime.now())

    cafe_id = Column(Integer, ForeignKey('cafe.id'), index=True)
    cafe = relationship('Cafe', backref=backref('articles', order_by=id))

    board_id = Column(Integer, ForeignKey('cafe_board.id'), index=True)
    board = relationship('CafeBoard', backref=backref('articles', order_by=id))

    def __init__(self, article_id, title, contents, cafe, board):
        self.article_id = article_id
        self.title = title
        self.contents = contents
        if isinstance(cafe, Cafe):
            self.cafe_id = cafe.id
        else:
            self.cafe_id = cafe

        if isinstance(board, CafeBoard):
            self.board_id = board.id
        else:
            self.board_id = board


def get_or_create(session, model, **kwargs):
    result = session.query(model).filter_by(**kwargs).first()
    if result:
        return result, False
    else:
        data = model(**kwargs)
        session.add(data)
        session.commit()
        return data, True


def instant_session():
    return scoped_session(sessionmaker(db))