import eazyml


#Login Credentials
username = 'sahaanasankaran@gmail.com'
password = 'Cupcake13'

#File paths for training and test data
##filepath_train = "Titanic - Training Data.csv"
filepath_test = "book1.csv"

##huh?
global outcome
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
        response = eazyml.ez_auth(username, password)
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
        ##global auth_token
        ##global model_id
        #WHAT IS THIS ID??????####
        global prediction_dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for prediction
        #put exact values here
        response = eazyml.ez_predict(auth_token, model_id = 12411, filepath_test="C:\Users\csankar1\Downloads\eazyml-client-mastercsankar1\Downloads\eazyml-client-master\book1.csv", options)
        ##prediction_dataset_id = response['predict_dataset_id']
        print(response)
    except Exception as e:
        print('The function ez_predict was not executed properly', e)


if __name__ == '__main__':
    ez_auth()

    ez_predict()



