import pathlib


class DataCollector(object):

    def __init__(self, data_location: str):
        self.data_location: str = data_location

    @staticmethod
    def build(data_location: str = './raw_data/'):
        return DataCollector(data_location=data_location)

    def run_all(self):
        for raw_file in pathlib.Path(self.data_location).glob('**/*'):
            yield raw_file

    def run_single(self, file: str):
        """
        Run data collection for single file
        :param file:
        :return:
        """
        if file.startswith('/'):
            return file
        else:
            return f'{self.data_location}{file}'
