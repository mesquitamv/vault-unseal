#!/usr/bin/python3

# Imports
import argparse
import requests
import json

def main():

  # Get parameters
  parser = argparse.ArgumentParser()
  parser.add_argument("-u","--url",
                      action="store",
                      dest="arg_vault_url",
                      default="",
                      help="Url of Vault. Must be https://<dns-vault-server>/")
  parser.add_argument("-t", "--token",
                      action="store",
                      dest="arg_unseal_token",
                      default="",
                      help="Unseal token of Vault")
  args = parser.parse_args()

  vault_url = str(args.arg_vault_url)+"v1/sys/unseal"
  vault_unseal_token = str(args.arg_unseal_token)

  payload = {}
  payload["key"] = vault_unseal_token

  try:
    request = requests.post(vault_url, data = json.dumps(payload))
  except:
    print("An error occurred with request: RC: " + request.status_code)
    raise Exception

  print(request.text)

if __name__ == '__main__':
  main()