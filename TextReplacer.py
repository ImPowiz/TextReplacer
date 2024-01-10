import os
from os import path


mypath = "C:\\Users\kevin\Python\\"

# Check current working directory.
retval = os.getcwd()

print( "Current working directory %s" % retval)
print(" ")

# Retrieving Names of Files
inputfilename = input("What is the name of the input file? (The file with inputs and outputs):")
datafilename = input("What is the name of the data file? (The file to search):")
newfilename = input("What would you like to call the new edited file?:")

# Now change the directory
os.chdir( mypath )

# Check current working directory.
retval = os.getcwd()

# Neutral Starting Points
linecount = 1
text = ""



# Checks if input file exists
while path.exists(inputfilename) == False:
    inputfilename = input("The designated file: '{inputfilename}' does not exist. Please specify an existing file. /n (Did you include the extenstion? Ex. txt, kml, etc.)")

# Retrieves inputs and outputs from input file
with open(inputfilename) as inputfile:
    for line in inputfile:
        if linecount == 1:
            print(" ")
            TextToFind = line.split(',')
            print(f"List of Text To Find: {TextToFind}")
        if linecount == 2:
            TextToReplace = line.split(',')
            print(f"List of Text To Replace: {TextToReplace}")
        print(" ")
        linecount += 1
inputfile.close()


# Checks if data file exists
while path.exists(datafilename) == False:
    datafilename = input("The designated file: '{datafilename}' does not exist. Please specify an existing file. /n (Did you include the extenstion? Ex. txt, kml, etc.)")    


# Copying data.kml
with open(datafilename) as datafile:
    for line in datafile:
        text += line
datafile.close()

# Defining text
EditedData = text

# Replacing inputs with outputs in text
for x in range(0, len(TextToFind)):
    EditedData = EditedData.replace(TextToFind[x], TextToReplace[x])


# Ensures file name is valid
if not "." in newfilename:
    newfilename += (f".{datafilename.split('.')[1]}")

# Create new file with replaced text
f = open(newfilename,"w+")
f.write(EditedData)
f.close()

# Aleart Completion
print(f"New file called: '{newfilename}' has been created.")

    



