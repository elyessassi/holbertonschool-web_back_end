#!/usr/bin/env python3
""" getting documents by certain element in a list """


def schools_by_topic(mongo_collection, topic):
    """ function to find by content """

    return (mongo_collection.find({"topics": topic}))
