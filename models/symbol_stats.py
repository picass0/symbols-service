import datetime
from dataclasses import dataclass
from decimal import Decimal

from sqlalchemy import func

from main import db


@dataclass
class SymbolStats(db.Model):
    id: int
    date_create: datetime.datetime
    symbol_id: int
    market_cap: int
    p_e: Decimal
    p_s: Decimal
    p_b: Decimal
    p_cash: Decimal
    p_free_cash: Decimal
    dividend_yield: Decimal
    e_p_s: Decimal
    shares_outstanding: int
    shares_float: int
    insider_ownership: Decimal
    institutional_ownership: Decimal
    float_short: Decimal
    short_ratio: Decimal
    return_on_equity: Decimal
    long_term_debt_to_equity: Decimal
    total_debt_to_equity: Decimal
    gross_margin: Decimal
    operating_margin: Decimal
    average_volume: int
    relative_volume: Decimal
    price: Decimal
    change: Decimal
    volume: int
    price_and_volume: int

    id = db.Column(db.BigInteger, primary_key=True)
    date_create = db.Column(db.DateTime, index=True, default=func.now())
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'), nullable=False)
    market_cap = db.Column(db.BigInteger, index=True)
    p_e = db.Column(db.DECIMAL(scale=2))
    p_s = db.Column(db.DECIMAL(scale=2))
    p_b = db.Column(db.DECIMAL(scale=2))
    p_cash = db.Column(db.DECIMAL(scale=2))
    p_free_cash = db.Column(db.DECIMAL(scale=2))
    dividend_yield = db.Column(db.DECIMAL(precision=5, scale=2))
    e_p_s = db.Column(db.DECIMAL(scale=2))
    shares_outstanding = db.Column(db.Integer)
    shares_float = db.Column(db.Integer)
    insider_ownership = db.Column(db.DECIMAL(precision=5, scale=2))
    institutional_ownership = db.Column(db.DECIMAL(precision=5, scale=2))
    float_short = db.Column(db.DECIMAL(precision=5, scale=2))
    short_ratio = db.Column(db.DECIMAL(precision=5, scale=2))
    return_on_equity = db.Column(db.DECIMAL(precision=7, scale=2))
    long_term_debt_to_equity = db.Column(db.DECIMAL(precision=7, scale=2))
    total_debt_to_equity = db.Column(db.DECIMAL(precision=7, scale=2))
    gross_margin = db.Column(db.DECIMAL(precision=7, scale=2))
    operating_margin = db.Column(db.DECIMAL(precision=7, scale=2))
    average_volume = db.Column(db.Integer, index=True)
    relative_volume = db.Column(db.DECIMAL(precision=7, scale=2))
    price = db.Column(db.DECIMAL(precision=10, scale=2), index=True)
    change = db.Column(db.DECIMAL(precision=5, scale=2))
    volume = db.Column(db.Integer, index=True)
    price_and_volume = db.Column(db.Integer, index=True)
