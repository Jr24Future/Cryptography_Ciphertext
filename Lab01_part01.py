#Part 01:

#This program will prompt the user for a sentence.
#The program passes the sentence to a function named modify().
#The function modify() returns a string that shifts the characters
#in the sentence three characters to the left.


#Modify function:
#  Takes in a list and then
#  iterates through it shifting the
#  characters three to the left 
#  and returns a string.
def modify(sentence):
    shift = 3
    length = len(sentence)
    shifted_sentence = sentence[shift:] + sentence[:shift]
    return (shifted_sentence)



#Main
def main():
    sentence = input("Write a sentence without spaces: ")
    modified_sentence = modify(sentence)
    print(modified_sentence)

if __name__ == "__main__":
    main()
