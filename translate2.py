import collections
import requests,json

class dbReader():
    def __init__(self):
        self.translateApiKey = ""
    def getTranslateKey(self):
        return self.translateApiKey
    def setTranslateKey(self,keyValue):
        self.translateApiKey = keyValue

class TranslationObj():
    def __init_(self,text,language):
        self.text = text
        self.targetLang = language
    def getText(self):
        return self.text
    def getTargetLang(self):
        return self.targetLang


class translate():
    def __init__(self,dbReader,translateObj):
        self.apiKey = dbReader.getKey()
        self.origText = translateObj.getText()
        self.targetLang = translateObj.getTargetLang()
        self.translatedText = ""
        self.responseCode = ""

    def getTranslation(self):
        payload = {'q':self.origText, 'target':self.targetLang, 'key':self.apiKey}
        resp = requests.get('https://www.googleapis.com/language/translate/v2',params=payload)
        response_dict = resp.json()
        try:
            self.translatedText = response_dict['data']['translations'][0]['translatedText']
            print "%s ---> %s\n"%(self.origText,response_dict["data"]["translations"][0]["translatedText"])
        except KeyError:
            if "error" in response_dict.keys():
                print "Error Code:%s Message:%s Reason:%s"%(response_dict["error"]["code"],response_dict["error"]["message"],response_dict["error"]["errors"][0]["reason"])
                self.responseCode = response_dict["error"]["code"]

