



#importing Flask and other modules
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/marks', methods =["GET", "POST"])
def gfg():
      print("saskjfhjas")
      if request.method == "POST":
         URL = request.form.get("fname")
         #print(first_name)
         #URL="https://ssc.digialm.com//per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O2258/2207O2258S52D342010/16552561125634920/3201007443_2207O2258S52D342010E1.html"


         

         
         
         print(URL)
         r = requests.get(URL)
         soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

         counter=0
         correct_ans=[]
         for name in soup.find_all("td", class_="rightAns"):
            salary = name.parent.find_all('td')[-1]  # last cell in the row
            data=name.get_text()[0]
            correct_ans.append(data)
            counter=counter+1
    
         print(correct_ans)
         m=0
         counter1=0
         your_answer=[]
         for name in soup.find_all("td", class_="bold"):
            m=m+1
            if(m==9):
               ch=name.get_text()
               f=str(ch)
               if(len(f)<=5):
                  your_answer.append(f)
               m=0
            else:
               m=m+1
         marks=0
         mk=0
         for i in range(0,len(correct_ans)):
            if(correct_ans[i]==your_answer[i]):
               marks=marks+1
            if(correct_ans[i]!=your_answer[i] and your_answer[i]!=' -- '):
               marks=marks-0.33
               mk=mk+1
         print("your negative marks is :  -----------------",mk)
         print("your marks is   --->   ",marks)
         print(correct_ans)
         print(your_answer)
         di = {'negative_Number ':mk,'Total_marks_obtained ':marks}
         return render_template('form.html' ,result = di)

if __name__=='__main__':
   app.run(debug=True)




