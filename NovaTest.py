import json
import os.path
import time

from book.book import book
from nova_act import NovaAct

with NovaAct(starting_page="https://www.amazon.com") as nova:
	nova.act("search for a coffee maker")