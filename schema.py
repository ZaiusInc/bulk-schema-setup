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

        parser.add_argument('-f', '--file', dest='file', required=True, help='Supply the name of the file with the identifiers to process. Supported columns are: email, vuid, phone')

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

        for row in self.read_file():
            
            api_headers = {
                "x-api-key": row['api_key'].strip()
            }

            spec = {
                "name": row['name'],
                "type": row['type'],
                "display_name": row['display_name'],
                "primary_key": False,
                "description": row['description']
            }

            url = "https://api.zaius.com/v3/schema/objects/" + row['object'] + "/fields"

            try:
                response = requests.post(url, json=spec, headers=api_headers)

                if response.status_code == 200:
                    print("Successfully created field: " + row['name'])
                else:
                    print("Failed to create field: " + row['name'] + "\n" + response.text)

            except Exception as e:
                print(str(e))

ZaiusSchema()
