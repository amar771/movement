# Uber movement

## Ingestion

Ingestion is done through files that are located locally in `raw_data` folder by running command `python main.py ingest-movement`
It's done this way because currently only files are accessible, if in the future we get access to API we would add that
access to `data_collector` and rest of the code would stay pretty much same.

## Data lifecycle

Files can be deleted immediately after ingestion while data that is ingested in lake should be kept there for longer duration.

## Access Control

Access control would be managed on MongoDB side, one option would be to allow write access to mongo only
by this application.

Read access should also only be allowed to other application that use this data.

## Data Quality

Currently there is a lot of data without GeoPoints, we still ingest it and additional data quality
should be done by some middleware between this data and whatever application is using this data.

## Data enrichment

Some points of data enrichment would be calculating distances and converting from geometry to geography.
That is in TODO list.