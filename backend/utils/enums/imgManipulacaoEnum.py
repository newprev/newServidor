from enum import Enum


class ImgManipulacao(Enum):
    ok = 0
    erroPath = 1
    erroResize = 2
    erroArquivo = 3
    erroGenerico = 10
