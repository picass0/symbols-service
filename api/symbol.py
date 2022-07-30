from flask import Blueprint, abort, jsonify

from models.symbol import Symbol

bp = Blueprint('symbol', __name__, url_prefix='/symbol')


@bp.route('/<int:id>')
def get(id):
    symbol = Symbol.query.get(id)

    if symbol is None:
        abort(404, description='symbol not found')

    return jsonify(symbol)