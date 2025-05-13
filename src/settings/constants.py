import os

import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

MAX_TERRITORY = int(os.getenv("MAX_TERRITORY"))
DB_URL = os.getenv("DB_URL")

if os.getenv("PROD") == "True":
    PROD = True
else:
    PROD = False
