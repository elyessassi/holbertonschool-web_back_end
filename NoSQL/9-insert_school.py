#!/usr/bin/env python3
"""" Inserting a document """


def insert_school(mongo_collection, **kwargs):
    """ function that inserts the document """

    obj = mongo_collection.insert_one(kwargs)
    return (obj.inserted_id)
