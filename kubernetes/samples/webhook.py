import http.server
import json
import requests
import base64
import os
import logging
from kubernetes import client, config

dir_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the request body
        length = int(self.headers['Content-Length'])
        if length is not None:
            length = int(length)
            body = self.rfile.read(length)
        else:
            body = None

        # Process the notification
        json_data = json.loads(body)
        object_name = json_data[0]['data']['ObjectName']
        secret_version = json_data[0]['data']['Version']

        logging.info(object_name)
        logging.info(secret_version)
        with open(dir_path + '/' + 'data.json', 'r') as f:
            depdata = json.load(f)
        # depdata = {
        #     "test1": [
        #         {
        #         "deployments": ["nginx-deployment", "nginx-deployment"],
        #         "namespace": "default"
        #         },
        #         {
        #         "deployments": ["nginx-deployment", "nginx-deployment"],
        #         "namespace": "default2"
        #         },
        #     ],
        #     "test2": [
        #         {
        #         "deployments": ["nginx-deployment", "nginx-deployment"],
        #         "namespace": "default3"
        #         },
        #         {
        #         "deployments": ["nginx-deployment", "nginx-deployment"],
        #         "namespace": "default4"
        #         }
        #     ]
        #     }

        if object_name in depdata:
    # Iterate through the deployments and namespace
            for item in depdata[object_name]:
                deployments = item["deployments"]
                namespace = item["namespace"]
                # Iterate through the deployments and invoke the restart_deployment function
                for deployment in deployments:
                    logging.info(f"Restarting Deployments: {deployments} in namespace {namespace}")
        else:
            logging.info(f"ObjectName {object_name} not found in JSON data")
                # Create a secret
                # Send a response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Webhook received')

if __name__ == '__main__':
    # Start the webhook server
    server = http.server.HTTPServer(('0.0.0.0', 8000), WebhookHandler)
    print('Starting server at http://0.0.0.0:8000')
    server.serve_forever()