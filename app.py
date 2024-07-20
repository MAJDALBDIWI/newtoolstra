from flask import Flask, request, jsonify
from libretranslate import LibreTranslate

app = Flask(__name__)

libretranslate = LibreTranslate()

@app.route('/translate', methods=['POST'])
def translate():
    german_text = request.json['germanText']
    language = request.json['language']
    translation = libretranslate.translate(german_text, language)
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True)
