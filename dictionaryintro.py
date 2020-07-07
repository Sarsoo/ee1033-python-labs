phonebook = {} #empty dictionary, {} for dictionary [] for list
phonebook["Jack"] = "1"
phonebook["Nikos"] = "2"
phonebook ["Fiona"] = "3"

print phonebook["Jack"] #prints phone number of jack

phonebookother = { #other way to open dictionary" 
"jack": "1",
"nikos": "2",
"fiona" : "3"
}

phonebook["John"] = "4" #adds element

for key, value in phonebook.iteritems():
	print key + "'s phone number is " + str(value)

phonebook["Nikos"] = "7" #change number

print phonebook["Nikos"] #reprint

del phonebook["Fiona"] #deletes number

for key, value in phonebook.iteritems():
	print key + "'s phone number is " + str(value)
