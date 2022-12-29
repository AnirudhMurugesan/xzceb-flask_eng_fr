from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.englishtoFrench(textToTranslate)
    # frenchText = language_translator.translate(text=textToTranslate, model_id='en-fr').get_result()
    # frenchText = frenchText['translations'][0]['translation']
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.frenchtoEnglish(textToTranslate)
    # englishText = language_translator.translate(text=textToTranslate, model_id='fr-en').get_result()
    # englishText = englishText['translations'][0]['translation']
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
