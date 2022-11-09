import logging

from datetime import datetime

from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, IntField, DateTimeField, ReferenceField

from source.settings import MONGO_DB
from source.data_processor.movement import MovementModel
from source.data_store.location_model import Location
from source.data_store.db_connection import MongoClient

logger = logging.getLogger(__name__)


class MetadataDocument(EmbeddedDocument):
    created_at = DateTimeField(default=datetime.now())
    file = StringField()


class Movement(Document):
    origin = ReferenceField(Location)
    destination = ReferenceField(Location)
    start_date = DateTimeField()
    end_date = DateTimeField()
    range = StringField()
    mean_travel_time = IntField()
    upper_travel_time = IntField()
    lower_travel_time = IntField()
    metadata = EmbeddedDocument(MetadataDocument)

    meta = {
        'strict': False,
        'collection': 'movement',
        'db_host': MongoClient().parse_mongodb_url(),
        'db_alias': MONGO_DB
    }

    @classmethod
    def initialize(cls, file, origin, destination, movement: MovementModel):
        metadata_obj = MetadataDocument(
            created_at=datetime.now(),
            file=file
        )

        obj = cls(
            origin=origin,
            destination=destination,
            start_date=movement.start_date,
            end_date=movement.end_date,
            range=movement.date_range,
            mean_travel_time=movement.mean_travel_time,
            upper_travel_time=movement.upper_travel_time,
            lower_travel_time=movement.lower_travel_time,
            metadata=metadata_obj
        )

        return obj
