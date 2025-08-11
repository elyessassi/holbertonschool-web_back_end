#!/usr/bin/env python3
""" show stats about Nginx logs """

from pymongo import MongoClient


def get_stats():
    """ show stats about Nginx logs """

    client = MongoClient('mongodb://127.0.0.1:27017')
    get_filter = {'method': 'GET'}
    post_filter = {'method': 'POST'}
    put_filter = {'method': 'PUT'}
    patch_filter = {"method": "PATCH"}
    delete_filter = {"method": "DELETE"}

    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents(get_filter)}")
    print(f"\tmethod POST: {collection.count_documents(post_filter)}")
    print(f"\tmethod PUT: {collection.count_documents(put_filter)}")
    print(f"\tmethod PATCH: {collection.count_documents(patch_filter)}")
    print(f"\tmethod DELETE: {collection.count_documents(delete_filter)}")
    filter = {"method": "GET", "path": "/status"}
    print(f"{collection.count_documents(filter)} status check")


if (__name__ == "__main__"):
    get_stats()
