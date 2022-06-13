import flask
from flask import jsonify

app = flask.Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
books = {
    'data': [
        {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'},
        {'id': 2,
         'title': 'Dhalgren',
         'author': 'Samuel R. Delany',
         'first_sentence': 'to wound the autumnal city.',
         'published': '1975'}
    ]
}


@app.route('/', methods=['GET'])
def home():
    return '''Hello Flask\n'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/books', methods=['GET'])
def books():
    return jsonify({'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'})


if __name__ == "__main___":
    app.run(debug=True, host='0.0.0.0')
