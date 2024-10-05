#!/usr/bin/env python3
""" file that containes function used
to obstruct the log message and return it """
import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """ function used to obstruct the log message and return it """

    for i in fields:
        message = re.sub(f"(?<={i}=)[^{separator}]+", redaction, message)
    return message
