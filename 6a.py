from flask import Flask,session,url_for,redirect,request,render_template
import re

app=Flask(__name__)
app.secret_key='secret'

@app.route('/',methods=['GET','POST'])
def start():
    if request.method=='GET':
        return render_template('6a.html',msg='',amt='')
    if request.method=='POST':
        if request.form['item1']=='' or request.form['item2']=='' or request.form['item3']=='' or request.form['p1']=='' or request.form['p2']=='' or request.form['p3']=='':
            return render_template('6a.html',msg='fill alla field',amt='')
        pat='[^0-9]'
        if re.match(pat,request.form['p1']) or re.match(pat,request.form['p2']) or re.match(pat,request.form['p3']):
          return render_template('6a.html',msg='enter valid number',amt='')
        if int(request.form['p1'])<0 or int(request.form['p2'])<0 or int(request.form['p3'])<0:
          return render_template('6a.html',amt='',msg='no negative')
        x=int(request.form['p1'])
        y=int(request.form['p2'])
        z=int(request.form['p3'])
        return render_template('6a.html',amt=(x+y+z),msg='your total amount is')    

if __name__=='__main__':
  app.run(debug=True)        