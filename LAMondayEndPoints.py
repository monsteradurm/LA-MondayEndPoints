from flask import Flask,request,json,jsonify

app = Flask(__name__)

@app.route('/TestFieldA')
def TestFieldA():
    return jsonify([
        { "title": "Label 1", "value": "label_1" },
        { "title": "Label 2", "value": "label_2" }
    ])

if __name__ == '__main__':
    app.run(debug=True)