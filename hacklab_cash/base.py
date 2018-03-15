# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config as cfg

engine = create_engine(cfg.db, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
