"""Module include required configs."""
import os

DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

DB_URI = os.environ['DB_URI']

API_KEY = os.environ.get('API_KEY', '')

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '5000'))
