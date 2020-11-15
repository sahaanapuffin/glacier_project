import json
import requests

#The API End-point that is to be used
API_URL = 'https://production.eazyml.com/ez_api'

#Login Credentials
username = 'api_demo'
password = 'api_demo'

#File paths for training and test data
filepath_train = "BBC_train.csv"
filepath_test = "BBC_test.csv"

outcome = "category"
global auth_token
global dataset_id
global model_id
global prediction_dataset_id

def ez_auth():

    '''
    This function calls the API which allows the user to authenticate with EazyML and returns a token
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_auth"
        global auth_token

        #The request payload
        payload = {
            "username": username,
            "password": password
        }

        #The request header
        headers = {
            "Content-Type": "application/json"
        }

        #The REST API request to authenticate
        response = requests.request(
            "POST", 
            API_REQUEST_URL, 
            headers = headers, 
            data = json.dumps(payload)
        )

        response_json = response.json()
        auth_token = response_json["token"]
        print("Response of ez_auth api is", response_json)
    except Exception as e:
        print('The function ez_auth was not executed properly', e)


def ez_load():

    '''
    This function calls the API which allows the user to upload training data in a file.
    The accepted file formats are .csv and .xlsx.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_load"
        global dataset_id

        #The file that is to be uploaded
        filename = filepath_train
        
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {"accelerate":"no"}
        
        #The request payload
        payload = {
            "options": json.dumps(options)
        }

        #The file parameter
        files = [("filename", open(filename, "rb"))] 

        #The request header
        headers = {
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to load
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, 
            data = payload, files = files 
        )
        
        response_json = response.json()        
        print("Response of ez_load api is", response_json)
        dataset_id = response_json["dataset_id"]
    except Exception as e:
         print('The function ez_load was not executed properly', e)

def ez_impute():

    '''
    This function calls the API which allows you to impute missing values in the 
    training dataset and then optionally fetch all those records with values imputed.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_impute"
        global dataset_id                                                                                                                                                                                                      
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}
        
        #The request payload
        payload = {
            "dataset_id": dataset_id,
            "options": options 
        }

        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to impute
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, 
            data = json.dumps(payload)
        )

        response_json = response.json()
        print("Response of ez_impute api is", response_json)
    except Exception as e:
        print('The function ez_impute was not executed properly', e)


def ez_outlier():
    
    '''
    This function calls the API which allows you to detect and remove outliers in the 
    training dataset and then optionally fetch all those outlier records
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_outlier"                      
        global dataset_id                                                                                                                                                                               
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}

        #The request payload
        payload = {
            "dataset_id": dataset_id,
            "options": options
        }
        
        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }
        
        #The REST API request to remove outliers
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_outlier api is", response_json)
    except Exception as e:
        print('The function ez_impute was not executed properly', e)


def ez_set_outcome():

    '''
    This function calls the API which allows you to specify the outcome
    variable and optionally it's data type
    '''
    try: 
        API_REQUEST_URL = API_URL + "/ez_set_outcome"
        global dataset_id

        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}

        #The request payload
        payload = {
            "dataset_id": dataset_id,
            "outcome"   : outcome,
            "options": options
        }
        
        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to set outcome
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )

        response_json = response.json()
        print("Response of ez_set_outcome api is", response_json)
    except Exception as e:
        print('The function ez_set_outcome was not executed properly', e)


def ez_init_model():
    
    '''
    This function calls the API which allows you to initialize machine learning 
    model parameters. It provides the user with various options on model building 
    such as type of the model, dependency removal, derivation from numeric or 
    text predictors derivations and many more.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_init_model"
        global dataset_id
        global model_id

        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {"accelerate":"no"}                                                                                                                                                                                                      
        #The request payload
        payload = {
            "dataset_id": dataset_id,
            "options": options
        }

        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to initialize the model
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        model_id = response_json['model_id']
        print("Response of ez_init_model api is", response_json)
    except Exception as e:
        print('The function ez_init_model was not executed properly', e)


def ez_remove_dependent():
    
    '''
    This function calls the API which allows users to remove dependent 
    predictors after model initialization.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_remove_dependent"                 
        global model_id

        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}                                                                                                                                                                                    
        #The request payload
        payload = {
            "model_id": model_id,
            "options": options
        }

        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }
        
        #The REST API request to remove dependent predictors
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_remove_dependent api is", response_json)
    except Exception as e:
        print('The function ez_init_model was not executed properly', e)


def ez_derive_text():

    '''
    This function calls the API which allows users to derive new predictors from native numeric predictors
    '''
    try:    
        API_REQUEST_URL = API_URL + "/ez_derive_text"         
        global model_id                                                                                                                                                                                            
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        #Here * denotes 'all the columns', so in this case we are deriving sentiments, glove, topics for all the columns
        options = {"text_types": {"*":["sentiments","glove","topic extraction"]},
                   "return_columns":"yes"}

        #The request payload
        payload = {
            "model_id": model_id,
            "options": options
        }

        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to derive numeric predictors
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_derive_text api is", response_json)
    except Exception as e:
        print('The function ez_derive_text was not executed properly', e)


def ez_select_features():
    
    '''
    This function calls the API which allows the users to perform feature selection 
    algorithms on training data and then retrieve all selected features.
    '''
    try: 
        API_REQUEST_URL = API_URL + "/ez_select_features"      
        global model_id                  

        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}                                                                                                                                                                             
        #The request payload
        payload = {
            "model_id": model_id,
            "options": options
        }
        
        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }
        
        #The REST API request to select features
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_select_features api is", response_json)
    except Exception as e:
        print('The function ez_select_features was not executed properly', e)


def ez_build_models():
    
    '''
    This feature calls the API which allows users to build machine learning 
    models after training data has been uploaded and preprocessed.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_build_models"
        global model_id                                                                                                                                                                                                     
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}

        #The request payload
        payload = {
            "model_id": model_id,
            "options": options
        }
        
        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }
        
        #The REST API request to build models
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_build_models api is", response_json)
    except Exception as e:
        print('The function ez_build_models was not executed properly', e)

def ez_predict():

    '''
    This function calls the API which allows you to predict the outcome variable 
    for each record in the given prediction (or test) dataset
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_predict"
        global model_id
        global prediction_dataset_id

        #Provide the path of your file here
        filename = filepath_test
        
        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}
        
        #The request payload
        payload = {
            "model_id": model_id,
            "options": json.dumps(options)
        }


        files = [("filename", open(filename, "rb"))]

        #The request header
        headers = {
            "Authorization": "Bearer " + str(auth_token),
        }
        
        #The REST API request to generate predictions
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, 
            data = payload, files = files 
        )
        
        response_json = response.json()
        prediction_dataset_id = response_json['prediction_dataset_id']
        print("Response of ez_predict api is", response_json)
    except Exception as e:
        print('The function ez_predict was not executed properly', e)


def ez_explain():
    
    '''
    This function calls the API which allows you to fetch an explanation for 
    the predicted outcome for any record or multiple records of the test dataset.
    '''
    try:
        API_REQUEST_URL = API_URL + "/ez_explain"
        global model_id
        global prediction_dataset_id

        #The options dictionary that is to be provided as part of the request payload. Please check the API guide for more parameters
        options = {}

        #The request payload
        payload = {
            "model_id": model_id,
            "prediction_dataset_id": prediction_dataset_id,
            "options": options
        }

        #The request header
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(auth_token),
        }

        #The REST API request to generate explanations for the predictions
        response = requests.request(
            "POST", API_REQUEST_URL, headers = headers, data = json.dumps(payload)
        )
        
        response_json = response.json()
        print("Response of ez_explain api is", response_json)
    except Exception as e:
        print('The function ez_explain was not executed properly', e)

       
if __name__ == '__main__': 
    ez_auth()
    ez_load()
    ez_impute()
    ez_outlier()
    ez_set_outcome()
    ez_init_model()
    ez_remove_dependent()
    ez_derive_text()
    ez_select_features()
    ez_build_models()
    ez_predict()
    ez_explain()         

