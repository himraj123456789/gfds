from flask import Flask, render_template,request
from bs4 import BeautifulSoup


import requests

def get_marks(URL):
   
   r = requests.get(URL)
   
   soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

   counter=0
   correct_ans=[]
   for name in soup.find_all("td", class_="rightAns"):
       salary = name.parent.find_all('td')[-1]  # last cell in the row
       data=name.get_text()[0]
       correct_ans.append(data)
       counter=counter+1
    

# Your answer 
   m=0
   counter1=0
   your_answer=[]
   for name in soup.find_all("td", class_="bold"):
    
    #time.sleep(1)
    
       if(m==5):
           your_answer.append(name.get_text())
           m=0
           counter1=counter1+1

       else:
        
           m=m+1



   marks=0
   for i in range(0,len(correct_ans)):

       if(correct_ans[i]==your_answer[i]):
           marks=marks+2
       if(correct_ans[i]!=your_answer[i] and your_answer[i]!=' -- '):
           marks=marks-0.5
   return marks

   
   


app = Flask(__name__)

@app.route('/')
def student():
   return "hello"

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['Name']
      re=get_marks(result)
      try:
         if(re/2):
            re=re
      except:
         re ="sorry give correct url"
      print(re)
      return render_template("result.html",result = re)

if __name__ == '__main__':
   #app.secret_key='himalaya'
   app.run(debug = False,host='0.0.0.0')

   
   
