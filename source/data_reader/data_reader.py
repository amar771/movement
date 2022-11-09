import csv


class DataReader(object):

    def __init__(self):
        pass

    @staticmethod
    def build():
        return DataReader()

    def run(self, raw_file):
        lines = []
        with open(raw_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                lines.append(line)

        return lines
