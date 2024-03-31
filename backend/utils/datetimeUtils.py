import datetime
from typing import List


def strToDatetime(data: str) -> datetime.datetime:
    if not isinstance(data, str):
        data = data.strftime('%Y-%m-%d %H:%M')

    dateFormats: List[str] = ['%Y-%m-%d %H:%M', '%d/%m/%Y', '%m/%Y', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S']
    for formato in dateFormats:
        try:
            dataRetorno = datetime.datetime.strptime(data, formato)
            return dataRetorno
        except ValueError as err:
            pass


def datetimeToStr(dataEnviada: datetime.datetime) -> str:
    if not isinstance(dataEnviada, datetime.datetime):
        return f"erro dataEnviada ({type(dataEnviada)}): {dataEnviada}"

    return dataEnviada.strftime('%d/%m/%Y %H:%M:%S')

range()