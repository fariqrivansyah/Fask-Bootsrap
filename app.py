import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder=os.path.abspath("template"))

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ""
    message = ""

    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

    return render_template('index.html', name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
