#!/usr/bin/env python3
""" Updating documents """


def update_topics(mongo_collection, name, topics):
    """ function to update document """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
