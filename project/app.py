#!/usr/bin/env python3

import pandas as pd
from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)


# Universal function
def room(csvfile, homepage):
    df = pd.read_csv(csvfile)
    if request.method == 'POST':
        # gets all user inputs and converts to variables
        title = request.form['title']
        firstname = request.form['firstName']
        surname = request.form['surname']
        roomnum = request.form['roomNum']
        daychosen = request.form['dayChosen']
        timechosen = request.form['timeChosen']
        reason = request.form['reason']
        
        if firstname == '' or surname == '' or reason == '':
            return render_template('failure.html', currentroom = roomnum, message = "Form not filled in!")

        # converts variables to respective number in database
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        daychosen = days.index(daychosen) + 1
        times = ['registration', 'p1', 'p2', 'p3', 'lunch', 'p4', 'p5', 'afterSchool']
        timechosen = times.index(timechosen)

        # converts every cell to a string
        df = df.applymap(str)

        if df.iat[timechosen, daychosen] != "Free":
            return render_template('failure.html', currentroom = roomnum, message = "Cell is already taken!")

        # puts data together as a variable
        # celldata = title + " " + firstname + " " + surname + "\n" + reason
        celldata = title + " " + firstname + " " + surname + " (" + reason + ")"
        # adds the cell data to the relevant cell
        df.iat[timechosen, daychosen] = celldata

        # writes to the csv
        df.to_csv(csvfile, index=False)

        return render_template('success.html', currentroom=roomnum)

    else:

        # converts dataframe to array and outputs array to webpage
        df = df.drop(df.columns[0], axis=1)
        df = df.values

        return render_template(homepage, df=df)


@app.route('/')
def home():
    return redirect(url_for('K6'))

@app.route('/K7', methods=['POST', 'GET'])
def K7():
    return room('databases/currentweekK7.csv', 'homeK7.html')

@app.route('/K6', methods=['POST', 'GET'])
def K6():
    return room('databases/currentweekK6.csv', 'homeK6.html')


@app.route('/K5', methods=['POST', 'GET'])
def K5():
    return room('databases/currentweekK5.csv', 'homeK5.html')
