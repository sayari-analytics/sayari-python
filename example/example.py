import sys
sys.path.append("..")

from sdk.main import Connect
from dotenv import load_dotenv
import os

load_dotenv()

client = Connect(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
sources = client.source.list_sources()
print(sources)
