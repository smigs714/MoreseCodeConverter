
from flask import Flask, render_template_string, request

app = Flask(__name__)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text)

@app.route('/', methods=['GET', 'POST'])
def index():
    morse_code = None
    if request.method == 'POST':
        text = request.form['text']
        morse_code = text_to_morse(text)
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Morse Code Converter</title>
</head>
<body>
    <h1>Text to Morse Code Converter</h1>
    <form method="post">
        <textarea name="text" placeholder="Enter text here..."></textarea>
        <button type="submit">Convert Text</button>
    </form>
    {% if morse_code %}
        <h2>Converted Morse Code:</h2>
        <p>{{ morse_code }}</p>
    {% endif %}
</body>
</html>
''', morse_code=morse_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
