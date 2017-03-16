import requests,json

textToTranslate = raw_input("Please enter what you would like to translate:")
translateTo = raw_input("Language:")
#api_key = 'AI'

payload = {'q':textToTranslate,'target':translateTo,'key':api_key}
resp=requests.get('https://www.googleapis.com/language/translate/v2',params=payload)
#print r.text
#print r.url
response_dict = resp.json()
print response_dict["data"]["translations"][0]["translatedText"]

