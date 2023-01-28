from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/hai')
def hai():
    return 'this is a flsak string'

@FAI.route('/Wish/<name>')
def Wish(name):
    return f'i am sending the data by using url{name}'




@FAI.route('/first')
def first():
    return render_template('first.html')

if __name__=='__main__':
    FAI.run(debug=True)

