

def read_names(names_file):
    names_file=open("names2.txt","r")
    names_list=[]
    for name in names_file:
        name=name.strip()
        name=name.lower()
        names_list.append(name)
    return names_list

ignored_words=["de", "los", "don", "del", "dona", "y", "dn", "sn", "fra", "frai", "sto", "Señor", "la"]

def word_is_ignored(word):
    if word in ignored_words:
        return True
    if word.startswith("("):
        return True
    if word.endswith(")"):
        return True
    return False   

def ID_letters(name):
    ID=""
    name=name.split()
    meaningful_name=[]
    for word in name:
        if not word_is_ignored(word):
            meaningful_name.append(word)         
    for i in range (len(meaningful_name) - 1):
        ID += meaningful_name[i][0]
    ID += meaningful_name[len(meaningful_name) - 1]
    ID = first_letters(ID)
    return ID
    
    
#     ID=ID + meaningful_name[0][0]
#     if len(meaningful_name) > 2: #there are names of length 4 too
#         ID=ID + meaningful_name[1][0]
#         first_letters(meaningful_name[2])
#         #add placeholder variable here
#     elif len(meaningful_name) == 2:
#         if len(meaningful_name[1]) >= 4:
#             ID=ID + meaningful_name[1][0:3]
#         else:
#             ID=ID + meaningful_name[1]
#             #add placeholder variable here
#     elif len(name) == 1:
#         if len(meaningful_name[0]) >= 4:
#             ID=ID + meaningful_name[0][0:3]
#         else:
#             ID=ID + meaningful_name[0]
#             #add placeholder variable here
#     return ID

def first_letters(name):
    num_letters = 5
    return name[0:num_letters]

def make_letters_list (names_file):
    final_IDs=[]
    names_list = read_names(names_file)
    for line in names_list:
        name_ID = ID_letters(line)
        final_IDs.append(name_ID)
    return final_IDs
    
def make_ID_list(names_file):
    letters_counts = {}
    letters_list = make_letters_list(names_file)
    ID_list = []
    for letters in letters_list:
        if letters not in letters_counts:
            #add to dictionary with initial value 1
            letters_counts[letters] = 1
        else:
            #increment the value wherever it is
            letters_counts[letters] += 1
        letters += str(letters_counts[letters])
        ID_list.append(letters)
    return ID_list
    

 
ID_list = make_ID_list("names2.txt")
for ID in ID_list:
    print(ID)
    
    
    
    



