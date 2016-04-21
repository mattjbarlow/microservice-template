import logging
import pprint


LOG = logging.getLogger()
logging.basicConfig()
LOG.setLevel(logging.INFO)
pp = pprint.PrettyPrinter(indent=4)


def lambda_handler(event, context):
    pp.pprint(event)
