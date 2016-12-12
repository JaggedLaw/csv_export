#!/usr/bin/python
import boto3
import json
import os
import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib
import urllib2
import csv

PORT_NUMBER = 8090

# class myHandler(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#
#         self.wfile.write("Holllaaaa")
#         return
#
# try:
#     server = HTTPServer(('', PORT_NUMBER), myHandler)
#     print server
#     server.serve_forever
#     print 'Started httpserver on port ', PORT_NUMBER
#
#
# except:
#     print 'quit received, shutting down'
#     server.socket.close()

def main():
    url = 'http://localhost:8090/csv_data.json'
    values = {'name' : 'Michael Foord',
              'location' : 'Northampton',
              'language' : 'Python' }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(url)
    json_response = json.loads(response.read())
    f = csv.writer(open('data.csv', 'wb+'))
    f.writerow(["id", "count change", "count", "timestamp", "door id", "door name"])

    for x in json_response:
        results = x["results"]
        for event in results:
            f.writerow([event["timestamp"], event["count_change"], event["count"], event["doorway_name"], event["doorway_id"]])

#     # s3 = boto3.client('s3')
#     #
#     with open('./csv_data.json') as json_data:
#         csv_data = json.load(json_data)
#     #
#     # temp_url = s3.generate_presigned_post(Bucket='test-charissa', Key='csv_data.json', ExpiresIn=3600)
#     # print temp_url
#
#     url = "http://localhost:8090/csv"
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     requests.post(url, data=json.dumps(csv_data), headers=headers)

if __name__ == '__main__':
    main()
