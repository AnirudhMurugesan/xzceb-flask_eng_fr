import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'k_exhdnOc4F7P_0UeHkW7SjLbH-5Ngek5td32XDCB38M'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/1c9b648a-a49b-4c66-98fa-8b6af0e07bda'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtoFrench(englishText):
    if englishText != '':
        frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
        frenchText = frenchText['translations'][0]['translation']
        return frenchText
    return None

def frenchtoEnglish(frenchText):
    if frenchText != '':
        englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
        englishText = englishText['translations'][0]['translation']
        return englishText
    return None


