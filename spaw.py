import requests
import json


class Streamable:
    def __init__(self, email, password):
        '''
        Param
        email: takes in the Streamable account email for  Basic Auth 
        password: takes in the Streamable account password for  Basic Auth 
        '''
        self.email = email
        self.password = password

    def upload(self, file_name):
        '''
        Param
        file_name: File name with full path for the file to upload
        '''
        file_processed = {
            'file': (file_name, open(file_name, 'rb')),
        }
        response = requests.post('https://api.streamable.com/upload', files=file_processed).json()
        result = response

        return result

    def import(self, link):
        '''
        Param
        link: Url link for the video to import/upload onto Streamable
        '''
        response = requests.get('https://api.streamable.com/import?url='+url, auth=(email, password)).json()
        link = 'https://streamable.com/' + str(response['shortcode'])
