import requests,json


def main():
    textToTranslate = raw_input("Please enter what you would like to translate:")
    translateTo = raw_input("Language:")
    #api_key = 'AI'
    
    payload = {'q':textToTranslate,'target':translateTo,'key':api_key}
    resp=requests.get('https://www.googleapis.com/language/translate/v2',params=payload)
    response_dict = resp.json()
    print response_dict["data"]["translations"][0]["translatedText"]

if __name__ == "__main__":
    main()
