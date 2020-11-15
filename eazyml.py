# TODO changes to be done:
# 1. make REST request headers same in all functions

import requests
import json
import traceback
import configparser  
import os

#read config file
EAZYML_URL = None
config = configparser.ConfigParser() 
config.read('config.ini')
config_error_message = "Unable to load EazML Client Library. " \
                       "Please set the EAZYML_URL in config.ini" 
try:
    EAZYML_URL = config.get("URL", "EAZYML_URL")
    if not EAZYML_URL:
        print(config_error_message)
        exit()
except configparser.NoOptionError as e:
    print(config_error_message)
    exit()

API_URL = EAZYML_URL.rstrip("/") + "/ez_api"

def exception_return(e, status_code):
    return_response = {"success": False, "status_code": status_code}
    try:
        raise(e)
    except requests.exceptions.HTTPError as errh:
        message = e
    except requests.exceptions.Timeout as errto:
        message = "Connection timeout", errto
    except requests.exceptions.TooManyRedirects as errtr:
        message = "Too many redirects", errtr
    except requests.exceptions.ConnectionError as errce:
        message = "Connection error", errce
    except requests.exceptions.RequestException as errre:
        message = "Connection error", errre
    except Exception as erre:
        message = "Exception", erre
    return_response["message"] = message
    return return_response


def ez_auth(username, password= None, api_key= None):
    status_code = 500
    try:
        API_REQUEST_URL = API_URL + "/ez_auth"
        payload = {
            "username": username,
            "password": password,
			"api_key": api_key
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response.raise_for_status()
        response_json["status_code"] = status_code
        return response_json
    except Exception as e:
        print((traceback.print_exc()))
        return exception_return(e, status_code)


def ez_load(auth_token, filename, options = None):

    status_code = 500
    try:
        API_REQUEST_URL = API_URL + "/ez_load"
        payload = {
            "options": json.dumps(options)
        }
        print(filename)
        files = [("filename", open(filename, "rb"))]
        headers = {
            "Authorization": "Bearer " + str(auth_token),
        }
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = payload, files = files
        )
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response.raise_for_status()
        response_json["status_code"] = status_code
        return response_json
    except Exception as e:
        print((traceback.print_exc()))
        return exception_return(e, status_code)


def ez_predict(auth_token, model_id, filename, options = None):
    status_code = 500
    try:
        API_REQUEST_URL = API_URL + "/ez_predict"
        payload = {
                "model_id": model_id, 
                "options": json.dumps(options)
        }
        files = [("filename", open(filename, "rb"))]
        headers = {
            "Authorization": "Bearer " + str(auth_token),
        }
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = payload, files = files
        )
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response.raise_for_status()
        response_json["status_code"] = status_code
        return response_json
    except Exception as e:
        print((traceback.print_exc()))
        return exception_return(e, status_code)

