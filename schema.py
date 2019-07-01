import requests
import csv
import argparse
import time
import json

class ZaiusSchema():

    def __init__(self):
        
        parser = argparse.ArgumentParser(
            description='A script to create fields on objects for a Zaius account.'
        )

        parser.add_argument('-l', '--log', dest='loglevel', required=False, help='Supply the name of the file with the identifiers to process. Supported columns are: email, vuid, phone')
        parser.add_argument('-f', '--file', dest='file', required=True, help='Supply the name of the file with the identifiers to process. Supported columns are: email, vuid, phone')
        #parser.add_argument('-a', '--auth', dest='auth', required=True, help='Supply the private API key for the account that contains the identifiers to be processed')

        args = parser.parse_args()

        self.file = args.file

        self.create_fields()    

    def read_file(self):

        try:
            with open(self.file, 'r') as csvfile:
                file = csv.DictReader(csvfile)         
                for row in file:
                    yield row

        except FileNotFoundError as fe:
            print("Cannot find the file by the name you have provided. Ensure it is in the same directory as this script and you have included the extension if it exists.")

    def create_fields(self):

        row_number = 1

        for row in self.read_file():
            
            #print(row['name'])

            api_key = row['api_key']

            spec = {
                "name": row['name'],
                "type": row['type'],
                "display_name": row['display_name'],
                "primary_key": False,
                "description": row['description']
            }

            api_payload = {
                "fields": [spec]
            }

            api_key = api_key.strip()

            api_headers = {
                "x-api-key": api_key
            }

            zaius_object = row['object']

            url = "https://api.zaius.com/v3/schema/objects/" + zaius_object + "/fields"

            print(api_payload)

            try:
                response = requests.post(url, json=spec, headers=api_headers)

                if response.status_code == 202:
                    print("Successfully created field: " + row['name'])
                else:
                    print("Failed to create field: " + row['name'] + "\n" + response.text)

            except Exception as e:
                print(str(e))

ZaiusSchema()