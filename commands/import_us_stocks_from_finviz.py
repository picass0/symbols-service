import click
from flask.cli import with_appcontext
from main import db

from models.symbol import Symbol
from models.symbol_stats import SymbolStats
from services.date_service import DateService
from services.finviz_screener_factory import FinvizScreenerFactory
from services.symbol_factory import SymbolFactory


@click.command('import-us-stocks-from-finviz')
@with_appcontext
# todo - somehow make sure, that this command finished at least once a day
def import_us_stocks_from_finviz():
    click.echo("importing from finviz")
    stock_list = FinvizScreenerFactory.create_us_screener()

    for stock_data in stock_list:
        symbol = Symbol.query.filter_by(ticker=stock_data['Ticker']).first()
        if symbol is None:
            symbol = SymbolFactory.create_symbol_from_finviz(stock_data)
            db.session.add(symbol)
            # todo - maybe commit later, see how much time passes between commits and how much performance improves, collect metrics about this data
            db.session.commit()

        beginning_of_today = DateService.get_beginning_of_today()
        stats_for_today_exists = is_stats_for_today_exists(beginning_of_today, symbol.id)

        if not stats_for_today_exists:
            symbol_stats = SymbolFactory.create_stats_from_finviz(stock_data, symbol.id)
            db.session.add(symbol_stats)
            db.session.commit()


def is_stats_for_today_exists(beginning_of_today, symbol_id):
    return db.session.query(
        SymbolStats.query
            .filter_by(symbol_id=symbol_id)
            .filter(SymbolStats.date_create > beginning_of_today)
            .exists()
    ).scalar()
