from finviz import Screener


class FinvizScreenerFactory:

    @staticmethod
    def create_us_screener():
        return Screener(
            table="Custom",
            filters=["geo_usa"],
            custom=['0', '1', '2', '3', '4', '5', '6', '7', '10', '11', '12', '13', '14', '16', '24', '25', '26',
                    '28', '30', '31', '33', '37', '38', '39', '40', '63', '64', '65', '66', '67'],
        )
