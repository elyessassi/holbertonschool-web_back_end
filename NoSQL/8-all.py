#!/usr/bin/env python3
""" Listing all documents in a collection """

import pymongo


def list_all(mongo_collection):
    """ function to list all documents in a collection """
    list_of_docs = []

    num_of_docs = mongo_collection.find()
    if (num_of_docs == 0):
        return (list_of_docs)
    else:
        for doc in mongo_collection.find():
            list_of_docs.append(doc)
    return (list_of_docs)


if (__name__ == "__main__"):
    list_all()
