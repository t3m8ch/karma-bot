import logging
from os import getenv


# Webhook
# WEBHOOK_URL = getenv("WEBHOOK_URL")
# assert WEBHOOK_URL is not None, "WEBHOOK_URL is not set"
#
# WEBAPP_HOST = getenv("WEBAPP_HOST", "localhost")
# WEBAPP_PORT = int(getenv("WEBAPP_PORT", 3000))

# Token
TG_TOKEN = getenv("TG_TOKEN")
assert TG_TOKEN is not None, "TG_TOKEN is not set"

TG_ADMINS = getenv("TG_ADMINS")
assert TG_ADMINS is not None, "TG_ADMINS is not set"

# Messages
PARSE_MODE = "HTML"

# Logging
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
