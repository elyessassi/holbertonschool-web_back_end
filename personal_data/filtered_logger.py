#!/usr/bin/env python3

""" file that containes function used
to obstruct the log message and return it """


import re


def filter_datum(fields: list, redaction: str, msg: str, separator: str)->str:
    """ function used to obstruct the log message and return it """

    for i in fields:
        msg = re.sub(f"(?<={i}=)[^{separator}]+", redaction, msg)
    return msg
