import json

import decimal

import datetime

import time

import base64

import boto3

client = boto3.client('kinesis', region_name="eu-west-1")

with open("FILEPATH/FILENAME") as json_file:

    jq = json.load(json_file, parse_float=decimal.Decimal)

# print jq

for i in jq:

    val = i['value']

    print val

    if val is None:

        val = '$0'

    data = json.dumps(i)

    # print data

    # print base64.b64encode(data)

    response = client.put_record(

        StreamName='MyStream',

        Data=data,

        PartitionKey=val

    )