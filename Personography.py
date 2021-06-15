#Reads a text file of names and converts each name into its own unique ID

ignored_words=["de", "los", "don", "del", "dona", "y", "dn", "sn", "fra", "frai", "sto", "Señor", "la"]

#reads a file and adds each line as an element in a list of names
def read_names(names_file):
    names_file=open("names2.txt","r")
    names_list=[]
    for name in names_file:
        name=name.strip()
        name=name.lower()
        names_list.append(name)
    return names_list

#returns True if a word is in the ignored_words list, begins with "(", or ends with ")".
#Returns false otherwise
def word_is_ignored(word):
    if word in ignored_words:
        return True
    if word.startswith("("):
        return True
    if word.endswith(")"):
        return True
    return False   

#Creates the part of an individual's ID composed of letters from their name
def ID_letters(name):
    ID=""
    name=name.split()
    meaningful_name=[]
    for word in name:
        #if the word is not a word to be ignored, add it to the meaningful_name list
        if not word_is_ignored(word):
            meaningful_name.append(word)
    #for each name but the person's last name, add the first letter of the name to the person's ID
    for i in range (len(meaningful_name) - 1):
        ID += meaningful_name[i][0]
    #add the person's entire last name to their ID
    ID += meaningful_name[len(meaningful_name) - 1]
    #truncate any extra letters from the ID such that the ID has 5 letters
    ID = first_letters(ID)
    return ID

#returns the first 5 letters of a name
def first_letters(name):
    num_letters = 5
    return name[0:num_letters]

#returns a list of the letters in each person's ID 
def make_letters_list (names_file):
    final_IDs=[]
    names_list = read_names(names_file)
    #for each name in the file, create a list of the letters in each person's ID
    for line in names_list:
        name_ID = ID_letters(line)
        final_IDs.append(name_ID)
    return final_IDs
    
#creates complete unique IDs by adding numbers to each grouping of letters to distinguish any identical groupings of letters
def make_ID_list(names_file):
    letters_counts = {}
    letters_list = make_letters_list(names_file)
    ID_list = []
    for letters in letters_list:
        if letters not in letters_counts:
            #add to dictionary with initial value 1
            letters_counts[letters] = 1
        else:
            #increment the current value for that entry by 1
            letters_counts[letters] += 1
        #add numbers to the grouping of letters from the person's name(s) to distinguish any duplicates
        letters += str(letters_counts[letters])
        ID_list.append(letters)
    return ID_list
    
ID_list = make_ID_list("names2.txt")

for ID in ID_list:
    print(ID)
    
    
    
    



