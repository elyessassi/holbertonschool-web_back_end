#!/usr/bin/env python3
""" file that containes function used
to obstruct the log message and return it """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ function used to obstruct the log message and return it """

    for i in fields:
        message = re.sub(f"(?<={i}=)[^{separator}]+", redaction, message)
    return message

import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        logging.basicConfig(format=self.FORMAT, level=logging.INFO)
        message = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        message = logging.info(message)
        print("****** ",message,"*****")
        return message
