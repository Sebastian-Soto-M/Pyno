import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                    format='\t%(levelname)s| %(message)s')
