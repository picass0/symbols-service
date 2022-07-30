
class FinvizParseException(Exception):

    def __init__(self, message, data):
        self.data = data
        #todo: parent::construct
