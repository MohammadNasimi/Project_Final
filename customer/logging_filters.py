import logging


class MinLenFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return len(record.getMessage()) > 20
