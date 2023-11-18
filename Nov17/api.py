from flask import Flask
from nov17work import assignment_handler

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to my API'

@app.route('/assignments')
def assignment():
    handler = assignment_handler()
    assignments = handler.list_of_assignments
    return assignments

@app.route('/assignments/<int:num>')
def assignments_num(num):
    handler = assignment_handler()
    assignments = handler.grab_assignments_dict(num)
    return assignments
def SportAction():
    print("The Player Scored the cruial goal")


if __name__ =='__main__':
    #app.run(debug=True)
    print(SportAction())
# Installing 


    
   
   

