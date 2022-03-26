import logging
import os
from pathlib import Path

def configure_logging(log_file: str, log_level=logging.DEBUG):
    log_file = Path(f'{os.getcwd()}/{log_file}')
    if not os.path.isdir(log_file.parent):
        os.mkdir(log_file.parent)

    file_handler = logging.FileHandler(filename=log_file)
    terminal_handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    terminal_handler.setLevel(log_level)
    terminal_handler.setFormatter(logging.Formatter(
        fmt='[%(levelname)s](%(filename)s@%(lineno)d):%(message)s'
    ))
    logging.basicConfig(
        handlers=(file_handler, terminal_handler),
        level=logging.NOTSET,
        format='%(asctime)-15s [%(levelname)-8s](%(filename)-12s@\
            %(funcName)-12s%(lineno)-4d%(threadName)-10s):%(message)s',
    )
