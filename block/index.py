#encoding=utf-8
from flask import Flask,render_template,request,redirect
from datetime import datetime


app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/post',methods=['POST'])
def post():
    name=request.form.get('name','匿名')
    comment=request.form.get('comment','暂无留言')
    create_time=datetime.now()
    save_data(name,comment,create_time)
    return redirect('/')






if __name__ == '__main__':
     app.run()
