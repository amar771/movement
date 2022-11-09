import os
import logging.config

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = int(os.environ.get('MONGO_PORT', '27017'))
MONGO_DB = os.environ.get('MONGO_DB')
MONGO_AUTH_SOURCE = os.environ.get('MONGO_AUTHENTICATION_SOURCE', 'admin')
MONGO_MAX_POOL_SIZE = int(os.environ.get('MONGO_MAX_POOL_SIZE', 1000))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '[%(asctime)s %(levelname)s/%(processName)s/%(threadName)s] [%(name)s(%(funcName)s)(%(lineno)d)] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'uber-movement.log',
            'formatter': 'default',
        },
        'errors_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'uber-movement-errors.log',
            'formatter': 'default',
        }
    },
    'loggers': {
        'shs.watcher': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        },
    }
}
logging.config.dictConfig(LOGGING)
