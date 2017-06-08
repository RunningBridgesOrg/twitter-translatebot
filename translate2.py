import collections
import requests,json

global fName 
fName = "apiKey.txt"

class DBReader():
    def __init__(self):
        self.translateApiKey = ""
    def getTranslateKey(self):
        return self.translateApiKey
    def setTranslateKey(self):
        try:
            with open(fName,"r") as f:
                self.translateApiKey = ""
                for line in f:
                    self.translateApiKey = line.strip()
                    print self.translateApiKey
                
                #Error condition checking for existing key.
                if not self.translateApiKey:
                    print "No api key is found"
        except IOError:
            print "Could not read file: '%s'"%(fName)

class TranslationObj():
    def __init__(self,text,language):
        self.text = text
        self.targetLang = language
    def getText(self):
        return self.text
    def getTargetLang(self):
        return self.targetLang


class Translate():
    def __init__(self,dbReader,translateObj):
        self.apiKey = dbReader.getTranslateKey()
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


def main():
    db = DBReader()
    db.setTranslateKey()
    tweet1 = TranslationObj("Let them eat cake","fr")
    tweet2 = TranslationObj("Doing demonstration is hard","ko")
    tweet3 = TranslationObj("I hope this works","zh-TW")
    tweet4 = TranslationObj("We are moving on Friday","es")

    translate1 = Translate(db,tweet1)
    translate2 = Translate(db,tweet2)
    translate3 = Translate(db,tweet3)
    translate4 = Translate(db,tweet4)

    translate1.getTranslation()
    translate2.getTranslation()
    translate3.getTranslation()
    translate4.getTranslation()

    
if __name__ == "__main__":
    main()
