from urllib import parse
from mongoengine import connect

from source import settings


class MongoClient:
    _instance = None

    host = settings.MONGO_HOST
    port = settings.MONGO_PORT
    alias = settings.MONGO_DB
    username = settings.MONGO_USERNAME
    password = settings.MONGO_PASSWORD
    authentication_source = settings.MONGO_AUTH_SOURCE

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance

    def parse_mongodb_url(cls):
        if cls.username and cls.password:
            return f'mongodb://{cls.username}:{parse.quote_plus(cls.password)}@{cls.host}:{cls.port}'
        else:
            return f'mongodb://{cls.host}:{cls.port}'

    def build(self):
        self.connection = connect(
            host=self.parse_mongodb_url(),
            db=self.alias,
            alias=self.alias,
            maxPoolSize=settings.MONGO_MAX_POOL_SIZE,
            connect=False,
            authentication_source=self.authentication_source
        )[self.alias]
        self.collections = dict()

    def get_connection(self):
        return self.connection

    def get_mongo_collection(self, collection_name):
        self.build()
        collection = self.collections.get(collection_name)
        if collection is None:
            collection = self.connection.get_collection(collection_name)
            self.collections.update({collection_name: collection})

        return collection
