# bulk-schema-setup
Create fields on Zaius objects in bulk via CSV

# Requirements
1. Python3 with `requests` library
3. Private Zaius API Key

# Environment Instructions
1. Go to https://www.python.org/downloads/ and download Python 3
2. Install Python 3
3. Run `pip3 install requests` in terminal

# CSV Format
1. Filename may be whatever you choose, you must supply the filename as an argument to the script and it must be in the same directory as the script
2. CSV supports the following columns: `object`, `name`, `display_name`, `type`, `description`, `api_key`. 

- `object` is the name of the object to create the field on (e.g. `customers`)
- `name` is the field name (e.g. `favorite_band`)
- `display_name` is the pretty field name (e.g. `Favorite Band`)
- `type` is the field data type (e.g. `string`, `number`, `timestamp`, `boolean`)
- `description` is text describing the purpose of the field (e.g. `The favorite band field is the customer's most listened to band`)
- `api_key` is the private API key of the account to create the field on


# Important Notes
1. ALL FIELDS ARE REQUIRED
2. PRIMARY KEYS ARE NOT SUPPORTED AT THIS TIME

# Script Arguments
```
usage: python redact.py [-h] [-l LOGLEVEL] -r REQUESTER -f FILE -a AUTH

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Supply the name of the file with fields to create
```
