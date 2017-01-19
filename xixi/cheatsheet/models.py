# -*- coding: utf-8 -*-
"""Xchange models."""
from datetime import datetime as dt
from app.database import Column, Model, db, reference_col, relationship, SurrogatePK


class Order(SurrogatePK, Model):
    """A order"""

    __tablename__ = 'orders'
    stock_id = Column(db.Integer, unique=True, nullable=True)
    order_type = Column(db.String(20), nullable=True)
    quantity = Column(db.Integer, nullable=True)
    price = Column(db.Integer, nullable=True)
    create_at = Column(db.DateTime, default=dt.utcnow(), nullable=False)
    updated_at = Column(db.DateTime, default=dt.utcnow, nullable=False)
    user_id = reference_col('users', nullable=False)
    fulfilled_at = Column(db.DataTime, nullable=True)
    status = Column(db.String(20), nullable=True)

    def __init__(self, stock_id, order_type, quantity, price, **kwargs):
        """Create instance."""
        db.Model.__init__(stock_id=stock_id, order_type=order_type, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Order({stock_id})>'.format(stock_id=self.stock_id)


class Fill(SurrogatePK, Model):

    __tablename__ = 'fills'
    price = Column(db.Integer, nullable=True)
    quantity = Column(db.Integer, nullable=True)
    create_at = Column(db.DateTime, nullable=False, index=True)
    updated_at = Column(db.DateTime, nullable=False, index=True)
    buy_order_id = Column(db.Integer, nullable=True)
    sell_order_id = Column(db.Integer, nullable=True)

    def __init__(self, price, **kwargs):
        db.Model.__init__(price=price, **kwargs)


class Stock(SurrogatePK, Model):

    __tablename__ = 'stocks'
    name = Column(db.String(20), nullable=True)
    symbol = Column(db.String(20), nullable=True)
    create_at = Column(db.DateTime, nullable=False)
    updated_at = Column(db.DateTime, nullable=False)

    def __init__(self, name, **kwargs):
        db.Model.__init__(name=name, **kwargs)
