#Part 02 

#This program has a list of lists that will be searched.
#The program will prompt the user for a character and output
#the number of times the character appears in each of the lists.

#Frequency function:
#  There are two input variables used by this function: the name of
#  the list of lists and the character for which you are searching.
#  The function prints (not returns) the number of occurrences of 
#  that character in each of the lists.

def frequency(inputs, character):
   for i, lst in enumerate(inputs):
     count = lst.count(character)
     print (f"Input [ {i} ]: {count}")



#Main
def main():
    #A list of lists
    inputs = [list("AOLSLAALYJJVVRPLZBHYABDPAOBSLAZAOBURBMVAOLYAOPUNZ"),
              list("ZCXNSMCPROCTYDGHCSUIRYTEBHHCJSMECWTQZCHDKRILLMSJS"),
              list("WSCVKAUSAUDJAUUEAOPLAHSMACDGHAUUSGABXHAGEHASGDARU")]

    charToCount = input("What character do you want to check?  ")
    frequency(inputs, charToCount)


if __name__ == "__main__":
    main()

