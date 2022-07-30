from flask import Blueprint, jsonify
from sqlalchemy import desc, nullslast
from main import db

from models.symbol import SymbolStats

bp = Blueprint('symbol-stats', __name__, url_prefix='/symbol-stats')


@bp.route("/")
def index():
    limit = 20
    offset = 0
    #todo - set limit
    #todo - set offset
    #todo - set orderby
    #todo - add other attributes to dataclass
    #todo - add validation

    sub_query = (db.session
                 .query(SymbolStats.id)
                 .distinct(SymbolStats.symbol_id)
                 .order_by(SymbolStats.symbol_id.desc(), SymbolStats.date_create.desc())
                 .subquery())
    result = (db.session
              .query(SymbolStats)
              .join(sub_query, SymbolStats.id == sub_query.c.id)
              .order_by(nullslast(desc('market_cap')))
              .limit(limit)
              .offset(offset)
              .all())

    return jsonify(result)