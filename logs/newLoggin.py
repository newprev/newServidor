import os
from logging import basicConfig, LogRecord
from logging import DEBUG, INFO
from logging import FileHandler
from logging import Formatter, Filter

from datetime import datetime
from typing import List, Tuple, Set


class NewLogging:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NewLogging, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.apiLog: FileHandler
        self.bancoLog: FileHandler
        self.syncLog: FileHandler

        self.iniciaConfiguracao()

    def iniciaConfiguracao(self):
        apiFormatter = Formatter("[%(asctime)s] l:%(lineno)s  %(levelname)s --> %(message)s")
        apiLogPath: str = os.path.join(os.curdir, 'logs', 'historicoLogs', f'{datetime.now().date()}_REST.txt')

        self.apiLog = FileHandler(apiLogPath, 'a')
        self.apiLog.setFormatter(apiFormatter)
        self.apiLog.setLevel(INFO)
        self.apiLog.addFilter(FiltroSistema())

        basicConfig(
            level=DEBUG,
            encoding='utf-8',
            handlers=[self.apiLog],
        )


class FiltroSistema(Filter):
    def filter(self, record: LogRecord) -> bool:
        arquivosSemInteresse: Set[str] = {
            'selector_events.py',
            'base.py',
            'autoreload.py',
            'log.py'
        }
        return record.filename not in arquivosSemInteresse

