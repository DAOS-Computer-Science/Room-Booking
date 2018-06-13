#!/usr/bin/env python3

import pandas as pd
from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('K6'))
                    
@app.route('/K6', methods=['POST', 'GET'])
def K6():
    df = pd.read_csv('databases/currentweek.csv')
    if request.method == 'POST':
        #gets all user inputs and converts to variables
        title = request.form['title']
        firstname = request.form['firstName']
        surname = request.form['surname']
        roomnum = request.form['roomNum']
        daychosen = request.form['dayChosen']
        timechosen = request.form['timeChosen']
        reason = request.form['reason']
        
        #df = pd.read_csv('databases/currentweek.csv')
        
        #converts variables to respective number in database
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        daychosen = days.index(daychosen) + 1
        times = ['Registration', 'P1', 'P2', 'P3', 'Lunch', 'P4', 'P5', 'AfterSchool']
        timechosen = times.index(timechosen) 
          
        #converts every cell to a string
        df = df.applymap(str) 
        
        if df.iat[timechosen, daychosen] != "Free" :
          return render_template('failure.html', currentroom = roomnum, message = "Cell is already taken!")
        

        # puts data together as a variable
        #celldata = title + " " + firstname + " " + surname + "\n" + reason
        celldata = title + " " + firstname + " " + surname + " (" + reason + ")"
        # adds the cell data to the relevant cell
        df.iat[timechosen, daychosen] = celldata
        
        #writes to the csv
        df.to_csv('databases/currentweek.csv', index = False)
        
        #return str(df.iat[timechosen, daychosen])
        
        return render_template('success.html', currentroom = roomnum)
      
    else:
        
        df = df.drop(df.columns[0], axis = 1)
        df = df.values
        
        
        return render_template('homeK6.html', df = df)

@app.route('/K5', methods=['POST', 'GET'])
def K5():
    if request.method == 'POST':
        return 'POSTING :D'
    else:
        return render_template('homeK5.html')