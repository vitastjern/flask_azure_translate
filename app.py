''' 
to run the flask app just type "python app.py" at the terminal prompt... (after first
setting the environment variables described in translate.py) 
'''
from flask import Flask, render_template, jsonify, request
import translate

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
