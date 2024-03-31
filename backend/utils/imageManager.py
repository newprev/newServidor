from PIL import Image
from pathlib import Path
from django.conf import settings

from utils.enums.imgManipulacaoEnum import ImgManipulacao


def redimensionarImagem(imgPath: str) -> ImgManipulacao:
    pathProjeto: Path = Path(settings.MEDIA_ROOT).parent
    pathEnviado: Path = Path(imgPath)

    pathImagem: Path = pathProjeto.joinpath(pathEnviado)

    if not pathImagem.exists():
        return ImgManipulacao.erroPath

    if not pathImagem.is_file():
        return ImgManipulacao.erroArquivo

    imagem: Image = Image.open(pathImagem.absolute())
    wImgReal, hImgReal = imagem.size

    hImgFinal = int((hImgReal/wImgReal)*150)

    imgMenor = imagem.resize((150, hImgFinal))
    imgMenor.save(pathImagem.absolute(), 'JPEG')

    return ImgManipulacao.ok
