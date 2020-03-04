# Saving filepaths to variables
# makes a smoother transition to the Sandbox
jokes_filepath = "jokes.txt"
answers_filepath = "answers.txt"

# When finished copy all code after this line into the Sandbox

# Open the files as read-only
jokes = open(jokes_filepath, "r")
answers = open(answers_filepath, "r")

# Get the first line and do something with it
jLine = jokes.readline()
aLine = answers.readline()

# Write your program below
run = 0
j = []
a = []
#update lists
j.append(jLine)
a.append(aLine)

while jLine:
	run += 1
	jLine = jokes.readline()
	aLine = answers.readline()
	jLine = jLine.replace("\n", "")
	aLine = aLine.replace("\n", "")
	j.append(jLine)
	a.append(aLine)
  
print("There are " + str(run) + " jokes")
jChoice = int(input("Which joke would you like to see? "))
print("Joke #" + str(jChoice))
#output
print(j[jChoice - 1] + "\n")
print(a[jChoice - 1])