import json
import logging

FORMAT = '%-20s\t=>\t%-30s[%.3f]'


def debug_json(logger: logging.Logger, title: str, data: dict, indent=2):
    logger.debug(f'\n[{title}] {json.dumps(data, indent=indent)}')
