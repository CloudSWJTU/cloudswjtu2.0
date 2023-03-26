from flask import Flask, render_template, redirect, send_file
app = Flask(__name__,template_folder='templates',static_folder='static')



#old pages
@app.route('/' or 'index.html')
def index():
    return render_template('index.html')


@app.route('/fuwuquzhidao.html',methods=['GET','POST'])
def fuwuquzhidao_page():
    return render_template('fuwuquzhidao.html')


@app.route('/index1.html',methods=['GET','POST'])
def index1_page():
    return render_template('index1.html')

@app.route('/index2.html',methods=['GET','POST'])
def index2_page():
    return render_template('index2.html')

@app.route('/jdhistory.html',methods=['GET','POST'])
def jdhistory_page():
    return render_template('jdhistory.html')

@app.route('/login.html',methods=['GET','POST'])
def login_page():
    return render_template('login.html')

@app.route('/swjtudb.html',methods=['GET','POST'])
def swjtudb_page():
    return render_template('swjtudb.html')


if __name__ == '__main__':
    app.run()