import pandas as pd

#reads the csv file
df = pd.read_csv(csvfile)

#variables that the website gets from the user (You can change them for testing purposes)
title = "Mr"
firstname = "Rushin"
surname = "Shah"
roomnum = "K6"
daychosen = "Monday"
timechosen = "Registration"
reason = "Test reason"
        
        #converts variables to respective number in database
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
daychosen = days.index(daychosen) + 1
times = ['registration', 'p1', 'p2', 'p3', 'lunch', 'p4', 'p5', 'afterSchool']
timechosen = times.index(timechosen)

#converts every cell to a string
df = df.applymap(str) 
        
if df.iat[timechosen, daychosen] != "Free" :
    print("Error message!")
    #Below is what would actually happen in the website
    #return render_template('failure.html', currentroom = roomnum, message = "Cell is already taken!")
        
else:
    # puts data together as a variable
    #celldata = title + " " + firstname + " " + surname + "\n" + reason
    celldata = title + " " + firstname + " " + surname + " (" + reason + ")"
    # adds the cell data to the relevant cell
    df.iat[timechosen, daychosen] = celldata

    #writes to the csv
    df.to_csv(csvfile, index = False)
    print("Success!")
    #Below is what would actually happen in the website
    #return render_template('success.html', currentroom = roomnum)