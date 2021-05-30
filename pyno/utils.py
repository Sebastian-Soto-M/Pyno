import json
import logging


def build_url(base_url: str, endpoint: str) -> str:
    return f'{base_url}{endpoint}'


def debug_json(logger: logging.Logger, title: str, data: dict, indent=2):
    logger.debug(f'\n[{title}] {json.dumps(data, indent=indent)}')
