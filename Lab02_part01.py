#Lab 02 Part01:


#readIn function: 
#  Reads a file ether character by character or line-by-line into a list.
#  There are benefits to each method.  You may chose which to use.
#  Returns a list of characters or lines
#  The choice will be up to you.

def readIn(filename):
    #Opens file in read mode
    with open(filename, "r") as file:
 	#we are reading the entire file content as one string and converting into characters								
        content = list(file.read().replace("\n", "").upper())  	#newline characters are removed and converted to uppercase
    return content 						#return the list you generated



#frequency function:
#  You have already written a function that counts the occurence of a 
#  specified character. This time instead of printing the counts,
#  you will be returning the number of occurences for the character.

def frequency(inputs, character):
    count = inputs.count(character)  				#Count how many 'character' pops up in inputs
    return count 				 		#return the count of the character




#substituteAlphabet function:
#  Using the character frequencies and information
#  you have gained from the digrams and trigrams
#  create the monoalphabetic substitution to solve
#  the plaintext message.
#  You may want to modify the list of lists that contains
#  your cipherCharsList or you may want to create a new list
#  of lists

def substituteAlphabet(cipherText):
    cipher_to_plain = {
        'I': 'E',  			# I first matched all of the letters with the english longuage frequency
        'C': 'T', 			# and then change it according to the ciphertext as key words showed
        'R': 'A',  			# them self
        'Q': 'H',  
        'J': 'N',  
        'K': 'O',  
        'X': 'S',  
        'S': 'I',  
        'W': 'R',  			#the cipher_to_plain is where we tell the code to change that letter to a defferent letter
        'U': 'D',  
        'G': 'L',  
        'N': 'W',  
        'V': 'U',  
        'Y': 'C',  
        'T': 'B',  
        'P': 'G',  
        'H': 'M',  
        'Z': 'Y',  
        'L': 'P',  
        'O': 'F',  
        'F': 'K',  
        'B': 'V',  
    }
    plaintext = ""   # a little bad habit from C for memory allegations so creating a emty array called plaintext
    
    for char in cipherText:				#go through cipherText
        if char in cipher_to_plain:			#if that letter we are on in exist in cipher_to_plain 
            plaintext += cipher_to_plain[char]		#then add that new letter to the same location(spaces) in plaintext
        else:
            plaintext += char  				#keep the character unchanged if no mapping is found

    return plaintext  					#return plaintext


# Main
#   This is the list of lists you can use
#   Think of this as being read [row][column]
#   You can loop through the index [i][0] to 
#   pick a specific character, then you can write 
#   back to the index [i][1] for counts and 
#   index [i][2] for percentages

def main():
    import string
    filename = 'cipherText.txt'  # File containing the ciphertext
    
    cipherCharsList = [['A', 0, 0], ['B', 0, 0], ['C', 0, 0], ['D', 0, 0], ['E', 0, 0],
                       ['F', 0, 0], ['G', 0, 0], ['H', 0, 0], ['I', 0, 0], ['J', 0, 0],
                       ['K', 0, 0], ['L', 0, 0], ['M', 0, 0], ['N', 0, 0], ['O', 0, 0],
                       ['P', 0, 0], ['Q', 0, 0], ['R', 0, 0], ['S', 0, 0], ['T', 0, 0],
                       ['U', 0, 0], ['V', 0, 0], ['W', 0, 0], ['X', 0, 0], ['Y', 0, 0], 
                       ['Z', 0, 0]]
	
    cipherText = readIn(filename)  #Call readIn function
    total_chars = len(cipherText)  #Count chacters in the list  # Total number of characters in the ciphertext
    
    
    
    #Count frequency of each character
    #TODO: Loop through the list of lists, use your frequency function, write back to your second column in your list of lists.   
    #Example frequency(inputs,character)
    
    for i in range(len(cipherCharsList)):
        char = cipherCharsList[i][0]  #character to count
        cipherCharsList[i][1] = frequency(cipherText, char)  #store in the second column





    #Calculate the percentage for each letter in the ciphertext
    #TODO: Loop through the list of lists, calculate the percentage each (count of char/total char)*100, write back to your third column in your list of lists. 
    
    for i in range(len(cipherCharsList)):
        count = cipherCharsList[i][1]	#same logic as the second column
        cipherCharsList[i][2] = (count / total_chars) * 100  # Calculate percentage and store in the third column
        
        
        
        
        
        
    #Sort the list of lists based upon the percentages in descending order
    #TODO: Sort through the list of lists, print the character, count, percentage in descending order
    #HINT:  There is a method called .sort(), you can select which index to sort on and you can reverse the sort to achieve descending order.
    #Example is below
    #myList.sort(key=lambda myList: myList[indextosorton],reverse=True)
    #print("Character ","\t", "Count ","\t", "Percentage","\n")
    
    cipherCharsList.sort(key=lambda myList: myList[2], reverse=True)	#from the exmaple but im still confused on how it runs I can 
    									#understand what it does but ... note to self look into how this runs 		
									#in order
    # Printing the sorted characters with the for loop and counts and percentages for tags
    print("Character\tCount\tPercentage")
    for char_info in cipherCharsList:
        print(f"{char_info[0]}\t\t{char_info[1]}\t\t{char_info[2]:.2f}%")






    #Based upon the frequencies, digrams, trigrams try your sustitution
    #substituteAlphabet(cipherText)
    #print(your plaintext message)

    
    
    plaintext = substituteAlphabet(cipherText)	#copys the outcome of the function substituteAlphabet(the deciphered text) into plaintext 
    print("\n----> ", plaintext)  #prints it out

if __name__ == "__main__":
    main()
