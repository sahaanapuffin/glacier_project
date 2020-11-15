import eazyml


#Login Credentials

username = 'sahaanasankaran@gmail.com'
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlYzJlMjM4ZS00NzkwLTQ0YWYtOWY0Ny1jYjYwNDc2ZWRiYmUiLCJleHAiOjE2MDU0MTc2ODEsImZyZXNoIjpmYWxzZSwiaWF0IjoxNjA1MzMxMjgxLCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNjA1MzMxMjgxLCJpZGVudGl0eSI6IlNhaGFhbmEgU2Fua2FyYW4ifQ.zqvuBMp9DFWOmOWl1nQxaeuIEvYq5lMQZgWwGzg3E-M'

#File paths for training and test data
##filepath_train = "BBC_train.csv"
filepath_test = "book1.csv"

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
        global auth_token
    
        #Calling the eazyml library function for authentication
        response = eazyml.ez_auth(username, api_key = api_key)
        print(response)
        auth_token = response["token"]
        print("Output of ez_auth function is", response)
    except Exception as e:
        print('The function ez_auth was not executed properly', e)



def ez_predict():

    '''
    This function calls the API which allows you to predict the outcome variable
    for each record in the given prediction (or test) dataset
    '''
    try:
        global auth_token
        global model_id
        model_id = 12411
        filepath_test = "book1.csv"
        global prediction_dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for prediction
        response = eazyml.ez_predict(auth_token, model_id, filepath_test, options)
        ##prediction_dataset_id = response['predict_dataset_id']
        ##print(response)
        return response
    except Exception as e:
        print('The function ez_predict was not executed properly', e)


if __name__ == '__main__':
  ez_predict()
  ez_auth()

