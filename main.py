import click

from source.data_store.db_connection import MongoClient
from source.service import UberMovementService


@click.group()
def movement_cli():
    pass


class Main(object):

    @staticmethod
    def main():
        mongo_client = MongoClient()
        mongo_client.build()

    @staticmethod
    @movement_cli.command()
    def ingest_movement():
        uber_movement_service: UberMovementService = UberMovementService.build()
        uber_movement_service.run_all()


if __name__ == '__main__':
    Main().main()
