#!/usr/bin/env python3
"""15. Log stats - new version"""
if __name__ == "__main__":
    from pymongo import MongoClient
    logs = MongoClient().logs.nginx
    print(f"{logs.count_documents({})} logs\nMethods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    print(f"{logs.count_documents({'path': '/status'})} status check\nIPs:")
    ips = logs.aggregate([
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}, {"$limit": 10}])
    for ip in ips:
        print(f"\t{ip['_id']}: {ip['count']}")
