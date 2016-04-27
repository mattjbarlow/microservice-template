import logging
import json


LOG = logging.getLogger()
logging.basicConfig()
LOG.setLevel(logging.INFO)

def lambda_handler(event, context):
    LOG.info(json.dumps(event, indent=1))
