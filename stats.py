from datetime import datetime

class Stats(object):
    def __init__(self, command, id):

        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None


    def add_response(self, response):

        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()

    def get_duration(self):

        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):

    