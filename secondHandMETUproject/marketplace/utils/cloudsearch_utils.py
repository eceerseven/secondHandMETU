# marketplace/utils/cloudsearch_utils.py
import boto3

def perform_cloudsearch(query):
    cloudsearch_domain = 'search-secondhand-maq5eq722nglglhjt4fxvwiyuy.us-east-1.cloudsearch.amazonaws.com'
    cloudsearch = boto3.client('secondhand', endpoint_url=cloudsearch_domain)
    response = cloudsearch(queryParser='structured', query=query)
    return response['hits']['hit']

