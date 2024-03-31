from enum import Enum


class TipoLog(Enum):
    rest = 0
    cache = 1
    banco = 2
    sync = 3
    erro = 4
