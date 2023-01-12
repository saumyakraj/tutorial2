from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

from application import app

db = SQLAlchemy(app)

from sqlalchemy import Column, Integer, Float, Enum, DateTime, JSON


class Payments(db.Model):

    __tablename__ = 'payments'

    orderid = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(DateTime,  default=datetime.datetime.now)
    amount = Column(Float, default = 0)
    status = Column(Enum("ordered", "paid", "cancelled", "completed", name="statusEnum"), default='ordered')
    items = Column(JSON)

    # def __repr__(self):
    #     return self.orderId