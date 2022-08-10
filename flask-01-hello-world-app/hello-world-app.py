from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Iyi aksamlar!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Memleket!!!!'

@app.route('/third/subthird')
def third():
    return 'Guzek bak guzel gor'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True)



