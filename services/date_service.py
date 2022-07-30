from datetime import datetime


class DateService:
    @staticmethod
    def get_beginning_of_today():
        current_date = datetime.utcnow().date()
        return datetime(current_date.year, current_date.month, current_date.day)