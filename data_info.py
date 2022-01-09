import json

from pydantic import BaseModel


class DataClass(BaseModel):

    urls: list
    header: dict
    params: dict

