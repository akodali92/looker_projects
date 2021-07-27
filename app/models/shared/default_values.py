# python imports
from uuid import uuid4

# project imports


default_uuid = lambda: str(uuid4()).replace('-','')