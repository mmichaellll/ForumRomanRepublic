from sqlalchemy import create_engine, text, Column, String, Integer, ForeignKey, DateTime, or_, desc, func
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///forum.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()
