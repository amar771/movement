import pymongo
import logging

from typing import List
from pymongo.collection import Collection

from source.data_store.db_connection import MongoClient
from source.data_store.location_model import Location
from source.data_store.movement_model import Movement
from source.data_processor.movement import MovementModel, LocationModel

logger = logging.getLogger(__name__)


class LocationMongoService:

    def __init__(self, location_collection, movement_collection):
        self.location_operations = []
        self.movement_operations = []
        self.location_collection = location_collection
        self.movement_collection = movement_collection

    @staticmethod
    def build():
        location_collection: Collection = MongoClient().get_mongo_collection('location')
        movement_collection: Collection = MongoClient().get_mongo_collection('location')
        return LocationMongoService(location_collection=location_collection, movement_collection=movement_collection)

    @staticmethod
    def create_location_document(location: LocationModel, file: str):
        return Location.initialize(
            obj_id=location.id,
            geometry=location.geometry,
            display_name=location.display_name,
            file=file,
        )

    @staticmethod
    def create_movement_document(origin: Location, destination: Location, movement: MovementModel, file: str):
        return Movement.initialize(
            file=file,
            origin=origin,
            destination=destination,
            movement=movement
        )

    def run(self, file: str, all_objects: List[MovementModel]):
        for obj in all_objects:
            first_location: Location = self.create_location_document(obj.origin, file)
            second_location: Location = self.create_location_document(obj.destination, file)

            if first_location:
                operation = pymongo.operations.InsertOne(first_location.to_mongo())
                self.location_operations.append(operation)

            if second_location:
                operation = pymongo.operations.InsertOne(second_location.to_mongo())
                self.location_operations.append(operation)

            if first_location and second_location:
                movement: Movement = self.create_movement_document(origin=first_location,
                                                                   destination=second_location,
                                                                   movement=obj,
                                                                   file=file)

                if movement:
                    operation = pymongo.operations.InsertOne(movement.to_mongo())
                    self.movement_operations.append(operation)

        if self.location_operations:
            logger.info(f'Writing locations to database. Number of operations: {len(self.location_operations)}')
            self.location_collection.bulk_write(self.location_operations)

        if self.movement_operations:
            logger.info(f'Writing movement to database. Number of operations: {len(self.movement_operations)}')
            self.movement_collection.bulk_write(self.movement_operations)
