from typing import Literal
from xml.etree.ElementTree import fromstring as ElementTree_fromstring

from requests import get as request_get

from config import HORO_XML
from loader import logger_guru




async def get_user_horoscope(zodiac: str, when: Literal['today', 'tomorrow']) -> str:
    """
    Parsing XML horoscope by parameters.
    :param zodiac: chosen zodiac
    :param when: horoscope for today or tomorrow
    :return: horoscope-string
    """
    req = request_get(HORO_XML)
    if req.status_code != 200:
        logger_guru.warning(f"{req.status_code=} : Bad request!")
        return 'Что-то пошло не так...попробуй позже.'

    tree = ElementTree_fromstring(req.content)
    generated_msg: str = ''.join(
        msg.text for msg in (chunk.findall(when)[0] for chunk in tree.findall(zodiac))
    )
    return generated_msg