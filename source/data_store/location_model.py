import logging

from datetime import datetime

from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, IntField, DateTimeField, MultiPointField
from mongoengine import DoesNotExist, MultipleObjectsReturned

from source.settings import MONGO_DB
from source.data_store.db_connection import MongoClient

logger = logging.getLogger(__name__)


class MetadataDocument(EmbeddedDocument):
    created_at = DateTimeField(default=datetime.now())
    file = StringField()


class Location(Document):
    id = IntField(primary_key=True, requiredrelated_=True)
    display_name = StringField()
    geometry = MultiPointField()
    metadata = EmbeddedDocument(MetadataDocument)

    meta = {
        'strict': False,
        'collection': 'location',
        'db_host': MongoClient().parse_mongodb_url(),
        'db_alias': MONGO_DB
    }

    @classmethod
    def initialize(cls, obj_id, display_name, geometry, file):
        metadata_obj = MetadataDocument(
            created_at=datetime.now(),
            file=file
        )

        obj = cls(
            id=obj_id,
            display_name=display_name,
            geometry=geometry,
            metadata=metadata_obj
        )

        return obj
