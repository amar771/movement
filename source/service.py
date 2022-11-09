from source.data_collector.data_collector import DataCollector
from source.data_reader.data_reader import DataReader
from source.data_processor.movement import MovementProcessor


class UberMovementService(object):

    def __init__(self,
                 data_collector: DataCollector,
                 data_reader: DataReader):
        self.data_collector: DataCollector = data_collector
        self.data_reader: DataReader = data_reader

    @staticmethod
    def build():
        data_collector: DataCollector = DataCollector.build(data_location='./raw_data/')
        data_reader: DataReader = DataReader.build()
        return UberMovementService(data_collector=data_collector,
                                   data_reader=data_reader)

    def run_all(self):
        raw_data = []
        processed_data = []
        for file in self.data_collector.run_all():
            raw_data = self.data_reader.run(raw_file=file)

        for data in raw_data:
            processed_data.append(MovementProcessor.process_movement(data))

        print(len(raw_data))
        print(len(processed_data))