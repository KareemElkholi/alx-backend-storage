#!/usr/bin/env python3
"""12. Log stats"""
from pymongo import MongoClient
logs = MongoClient().logs.nginx
print(f"{logs.count_documents({})} logs\nMethods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print(f"    method {method}: {logs.count_documents({'method': method})}")
print(f"{logs.count_documents({'path': '/status'})} status check")
