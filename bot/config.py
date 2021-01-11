import os
import json
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "1570761081:AAFFnTROpNWo6NPrgpc7tiaDyPs100Uqx2A"
GDRIVE_FOLDER_ID = "1BjpZ04did3X3VS8eKCZA9nhe9mmi2Skb"
# Default folder id.
OWNER_ID = 558204588
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [558204588]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
INDEX_URL = "postgres://zluhocpmbqhlnm:f758b938e8b8cf8e68b67b45f4ceafb9e8656a815e62a53b45032ec9dd21ee57@ec2-54-147-98-183.compute-1.amazonaws.com:5432/df382ublqbklsp"
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = True
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
