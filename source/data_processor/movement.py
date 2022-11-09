from datetime import datetime


class LocationModel:

    def __init__(self, id, display_name, geometry):
        self.id = id
        self.display_name = display_name
        self.geometry = geometry


class MovementModel:

    def __init__(self, origin, destination, date_range, mean_travel_time, upper_travel_time, lower_travel_time):
        self.mean_travel_time = mean_travel_time
        self.upper_travel_time = upper_travel_time
        self.lower_travel_time = lower_travel_time

        self.origin: LocationModel = origin
        self.destination: LocationModel = destination

        if date_range:
            splitted = [obj.strip() for obj in date_range.split(',', 1)]
            dates = [obj.strip() for obj in splitted[0].split('-', 1)]
            self.start_date = datetime.strptime(dates[0], '%m/%d/%Y')
            self.end_date = datetime.strptime(dates[1], '%m/%d/%Y')
            self.date_range = splitted[1]


class MovementProcessor:

    @staticmethod
    def process_movement(raw_movement):
        origin = LocationModel(
            id=raw_movement.get('Origin Movement ID'),
            display_name=raw_movement.get('Origin Display Name'),
            geometry=raw_movement.get('Origin Geometry', None)
        )
        destination = LocationModel(
            id=raw_movement.get('Destination Movement ID'),
            display_name=raw_movement.get('Destination Display Name'),
            geometry=raw_movement.get('Destination Geometry', None)
        )
        movement = MovementModel(
            origin=origin,
            destination=destination,
            date_range=raw_movement.get('Date Range'),
            mean_travel_time=raw_movement.get('Mean Travel Time (Seconds)'),
            upper_travel_time=raw_movement.get('Range - Upper Bound Travel Time (Seconds)'),
            lower_travel_time=raw_movement.get('Range - Lower Bound Travel Time (Seconds)')
        )
        return movement
