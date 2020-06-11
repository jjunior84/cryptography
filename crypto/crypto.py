import requests, json, hashlib
from requests.exceptions import HTTPError

class JCCrypto:
    """
    Julius Caesar Cryptography class

    :param token: token to be used for HTTP requests 
    :type token: str
    :param url_base: URL base for HTTP requests
    :type url_base: str
    :param url_get_ext: complement for the API address to GET call
    :type url_get_ext: str
    :param url_post_ext: complement for the API address to POST call
    :type url_post_ext: str
    :param file_path: path where the JSON file will be persisted on Disk
    :type file_path: str
    """

    def __init__(
        self, 
        token: str,
        url_base: str,
        url_get_ext: str,
        url_post_ext: str,
        file_path: str
    ):
        self.token = token
        self.url_base = url_base
        self.url_get_ext = url_get_ext
        self.url_post_ext = url_post_ext
        self.file_path = file_path
        self.url_get = url_base + url_get_ext + "?token=" + token
        self.url_post = url_base + url_post_ext + "?token=" + token
        self.cypher_dictionary = None

        

    def get_json_from_url(self):
        '''
        Get json data from a determined URL

        :returns: dictionary with json content from request  
        :rtype: dict
        '''
        try:
            response = requests.get(self.url_get)

            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            print('Success to request URL, Json returned')
            return response.json()


    def persist_to_json(self, data: dict):
        '''
        Persist json to a file in a phisic directory

        :param data: data dictionary to be written in json file
        :type data: dict
        '''
        try:
            with open(self.file_path, 'w') as fp:
                json.dump(data, fp)
        except Exception as err:
            print(f'Error occurred: {err}') 
        else:
            print('Success to write file to path!')


    def get_json_info(self, element: str):
        '''
        Get specific element from Json file

        :param element: element name from json file that you need to get the value
        :type element: str

        :returns: value from json element 
        :rtype: dynamic
        '''
        try:
            with open(self.file_path, 'r') as fp:
                json_d = json.load(fp)
                element_val = json_d[element]
        except Exception as err:
            print(f'Error occurred: {err}') 
        else:
            print('Success to get json element ({})'.format(element))
            return element_val


    def set_json_info(self, element: str, value: str):
        '''
        Set value for a specific element from Json file

        :param element: element name from json file that you need to set the value
        :type element: str
        :param value: value that you need to set from json file 
        :type element: str        
        '''
        try:
            with open(self.file_path, 'r') as fp:
                data = json.load(fp)
                data[element] = value

            with open(self.file_path, 'w') as fp:
                json.dump(data, fp)

        except Exception as err:
            print(f'Error occurred: {err}') 
        else:
            print('Success to set value ({}) to json element ({})'.format(value, element))


    def create_cypher_dict(self, shift_number: int):
        plain_array = list(map(chr, range(97, 123)))
        cypher_array = list(map(chr, range(123-shift_number, 123))) + list(map(chr, range(97, 123-shift_number)))
        self.cypher_dictionary = dict(zip(plain_array, cypher_array))        


    def decrypt(self, cypher: str, shift_number: int):
        '''
        Call the function to create the cypher dictionary using the shift number and
        use function trough a lambda function to convert each character from the plain text  


        :param cypher: message encrypted
        :type cypher: str
        :param shift_number: shift number used to create the cypher dictionary
        :type shift_number: str  

        :returns: decrypted message
        :rtype: str      
        '''        
        #call the function that create the cypher dictionary, created as a separeted function to be able perform unit tests
        self.create_cypher_dict(shift_number)

        #lambda function to return char cypher decrypted against de cypher dictionary
        char_cypher = lambda x: self.cypher_dictionary[x] if x in self.cypher_dictionary else x

        return ''.join([char_cypher(plain_char) for plain_char in cypher])


    def encrypt_summary(self, decrypted_cypher: str):
        '''
        Get decrypted cypher and creates a hash using SHA1 function 

        :param decrypted_cypher: decrypted message
        :type decrypted_cypher: str  

        :returns: decrypted message hashed with SHA1 algorithm
        :rtype: str    
        ''' 
        return hashlib.sha1(decrypted_cypher.encode('utf-8')).hexdigest()


    def send_json_file(self):
        '''
        Send json data to API 
        '''
        try:
            files = {'answer': open(self.file_path, 'rb')}
            response = requests.post(url = self.url_post, files=files)

            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}') 
        else:
            print('Success to POST a request to API url, returned: {}'.format(response.json()))        

