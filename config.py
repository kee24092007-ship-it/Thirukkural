import os

THIRUKKURAL_API_BASE_URL = os.getenv(
    "THIRUKKURAL_API_BASE_URL",
    "https://getthirukural.appspot.com/api/2.0"
)

THIRUKKURAL_APP_ID = os.getenv("THIRUKKURAL_APP_ID", "")