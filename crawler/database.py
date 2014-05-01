# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
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
    title = Column(String)


class CafeBoard(Base):
    __tablename__ = 'cafe_board'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer)
    title = Column(String)

    cafe = relationship('Cafe', backref('boards', order_by=id))


class CafeArticle(Base):
    __tablename__ = 'cafe_article'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    contents = Column(Text)
    crawled_at = Column(DateTime, default=datetime.now())

    board = relationship('CafeBoard')


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance


def instant_session():
    return scoped_session(sessionmaker(db))