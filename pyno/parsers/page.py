from requests import Response

from ..models import PageModel


def parse_page(response: Response) -> PageModel:
    if response.ok:
        return PageModel.parse_raw(response.text)
    else:
        raise ValueError
