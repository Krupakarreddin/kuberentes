import http.server
import json
import base64
import json
import logging
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import datetime
import os

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

        # Read the request body as JSON
        try:
            webhook_data = json.loads(body)
        except json.decoder.JSONDecodeError as e:
            logging.error("Failed to parse request body as JSON: {}".format(e))
            return
        # Process the data
        process_data(webhook_data)

        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Webhook received')
        except BrokenPipeError:
            pass


def process_data(webhook_data):
    # Your code to process the data goes here
    api_client = client.AppsV1Api()
    logging.info(webhook_data)
    object_name = webhook_data[0]['data']['ObjectName']
    secret_version = webhook_data[0]['data']['Version']
    try:
        with open(dir_path + '/' + 'data.json', 'r') as f:
            deployment_data = json.load(f)
    except FileNotFoundError as e:
        logging.error("Could not find data.json file: {}".format(e))
        return
    
    
    if object_name in deployment_data:
        # Iterate through the deployments and namespace
                for item in deployment_data[object_name]:
                    deployments = item["deployments"]
                    namespace = item["namespace"]
                    # Iterate through the deployments and invoke the restart_deployment function
                    for deployment in deployments:
                        logging.info(f"Restarting Deployment: {deployment} in namespace {namespace}")
                        restart_deployment(api_client, deployment, namespace)
    else:
        logging.info(f"ObjectName/KeyName {object_name} not found in Deployment JSON data")



def restart_deployment(api_client, deployment, namespace):
    now = datetime.datetime.utcnow()
    now = str(now.isoformat("T") + "Z")
    body = {
        'spec': {
            'template':{
                'metadata': {
                    'annotations': {
                        'kubectl.kubernetes.io/restartedAt': now
                    }
                }
            }
        }
    }
    try:
        api_client.patch_namespaced_deployment(deployment, namespace, body, pretty='true')
    except ApiException as e:
        logging.info("Exception when calling AppsV1Api->_namespaced_deployment_status: %s\n" % e)


if __name__ == '__main__':
    # Start the webhook server
    # config.load_kube_config()
    config.load_incluster_config()
    # Enter name of deployment and "namespace"
    server = http.server.HTTPServer(('0.0.0.0', 8000), WebhookHandler)
    logging.info('Starting server at http://0.0.0.0:8000')
    server.serve_forever()
