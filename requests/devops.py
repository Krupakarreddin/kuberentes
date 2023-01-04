from operator import eq
import requests
import base64
import json
import pprint
pat='f6xjstfhft3xjeyitzgum7fo3v2svmdtz62ttaehoiqo2fm52hfq'
organization="shcgravity"
project="DeliveryPipeline"
# print(f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=6.0")
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}
repos = requests.get(f'https://dev.azure.com/{organization}/{project}/_apis/git/repositories?api-version=6.0',headers=headers).json()

for repo in repos['value']:
    name=repo['name']
    if repo['name'] == "PipelineTemplates":
        branches = requests.get(f'https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{name}/refs?api-version=6.0',headers=headers).json()
        for branch in branches['value']:
            print(branch['name'].split('/')[2])
            