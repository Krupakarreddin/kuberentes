import os

from kubernetes import client, config

def get_pods(namespace):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    api_client = client.CoreV1Api()

    # List the pods in the specified namespace
    pods = api_client.list_namespaced_pod(namespace=namespace, watch=False)
    return pods

if __name__ == '__main__':
    pods = get_pods('default')
    print(pods)
