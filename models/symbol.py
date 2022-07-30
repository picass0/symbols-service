from dataclasses import dataclass

from main import db
from models.symbol_stats import SymbolStats


@dataclass
class Symbol(db.Model):
    id: int
    ticker: str
    company: str
    sector: str
    industry: str
    country: str

    id=db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(50), index=True)
    company = db.Column(db.String(200))
    sector = db.Column(db.String(200))
    industry = db.Column(db.String(200))
    country = db.Column(db.String(200))

    stats = db.relationship(SymbolStats.__name__, backref='symbol', lazy=True)