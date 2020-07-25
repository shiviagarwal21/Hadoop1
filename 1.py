text = open("paragraph.txt", "r") //Open the text file in reading mode
d = dict()                        // Create a dictionary
for line in text:                 // Loop through the text file
    line = line.strip()           // Remove the extra spaces
    line = line.lower()           // Convert whole text file to lowercase
    words = line.split(" ")       //Split the words
    for word in words:            // Loop through words
        if word in d: 
            d[word] = d[word] + 1   
        else: 
            d[word] = 1
for key in list(d.keys()): 
    print("Count of ",key, ":", d[key])         // Print the word with count
