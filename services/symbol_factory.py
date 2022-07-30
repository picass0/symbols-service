import re
from decimal import Decimal

from exceptions.FinvizParseException import FinvizParseException
from models.symbol import Symbol
from models.symbol_stats import SymbolStats


class SymbolFactory:

    @staticmethod
    def create_symbol_from_finviz(stock_data):
        return Symbol(
            ticker=stock_data['Ticker'],
            company=stock_data['Company'],
            sector=stock_data['Sector'],
            industry=stock_data['Industry'],
            country=stock_data['Country']
        )

    @staticmethod
    def create_stats_from_finviz(stock_data, symbol_id):
        price = SymbolFactory._to_decimal(stock_data['Price'])
        volume = SymbolFactory._to_integer(stock_data['Volume'])
        price_and_volume = None
        if price and volume:
            price_and_volume = int(price * volume / 1000)
        return SymbolStats(
            symbol_id=symbol_id,
            market_cap=SymbolFactory._to_thousands_integer(stock_data['Market Cap']),
            p_e=SymbolFactory._to_decimal(stock_data['P/E']),
            p_s=SymbolFactory._to_decimal(stock_data['P/S']),
            p_b=SymbolFactory._to_decimal(stock_data['P/B']),
            p_cash=SymbolFactory._to_decimal(stock_data['P/C']),
            p_free_cash=SymbolFactory._to_decimal(stock_data['P/FCF']),
            dividend_yield=SymbolFactory._from_percent_to_decimal(stock_data['Dividend']),
            e_p_s=SymbolFactory._to_decimal(stock_data['EPS']),
            shares_outstanding=SymbolFactory._to_thousands_integer(stock_data['Outstanding']),
            shares_float=SymbolFactory._to_thousands_integer(stock_data['Float']),
            insider_ownership=SymbolFactory._from_percent_to_decimal(stock_data['Insider Own']),
            institutional_ownership=SymbolFactory._from_percent_to_decimal(stock_data['Inst Own']),
            float_short=SymbolFactory._from_percent_to_decimal(stock_data['Float Short']),
            short_ratio=SymbolFactory._to_decimal(stock_data['Short Ratio']),
            return_on_equity=SymbolFactory._from_percent_to_decimal(stock_data['ROE']),
            long_term_debt_to_equity=SymbolFactory._to_decimal(stock_data['LTDebt/Eq']),
            total_debt_to_equity=SymbolFactory._to_decimal(stock_data['Debt/Eq']),
            gross_margin=SymbolFactory._from_percent_to_decimal(stock_data['Gross M']),
            operating_margin=SymbolFactory._from_percent_to_decimal(stock_data['Oper M']),
            average_volume=SymbolFactory._to_thousands_integer(stock_data['Avg Volume']),
            relative_volume=SymbolFactory._to_decimal(stock_data['Rel Volume']),
            price=price,
            change=SymbolFactory._from_percent_to_decimal(stock_data['Change']),
            volume=volume,
            price_and_volume=price_and_volume
        )

    @classmethod
    def _to_thousands_integer(cls, value):
        if value == '-':
            return None
        last_char = value[-1]
        rest = value[:-1]

        if last_char == 'B':
            multiplier = 1_000_000
        elif last_char == 'M':
            multiplier = 1_000
        elif last_char == 'K':
            multiplier = 1
        else:
            raise FinvizParseException(
                'cannot convert finviz string to decimal. Unsupported last character',
                {'last_char': last_char}
            )
        value = Decimal(rest)
        return int(value * multiplier)

    @classmethod
    def _to_decimal(cls, value):
        if value == '-':
            return None

        return Decimal(value)

    @classmethod
    def _from_percent_to_decimal(cls, value):
        if value == '-':
            return None

        value = value[:-1]

        return Decimal(value)

    @classmethod
    def _to_integer(cls, value):
        if value == '-':
            return None

        return int(re.sub('\D', '', value))
