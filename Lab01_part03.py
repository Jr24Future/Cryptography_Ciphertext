#Part 03

#This program will provide cryptanalysis on a Shift by N cipher using an exhaustive key search
#You can either hard code the ciphertext into the program (easy) or you can prompt for 
#a text file or character input from the command line.
#You will need a function called analyze that will read in the ciphertext and then conduct an 
#exhaustive key search that outputs its key (the N) and the answer in each trial)
#
#Example output:

#Testing shift by:  0
#qefpzixppfpsbovzlli

#Testing shift by:  1
#rfgqajyqqgqtcpwammj

#Testing shift by:  2
#sghrbkzrrhrudqxbnnk

#Look back at parts 01 and 02.  They provide clues on how to implement this.  


def analyze(ciphertext):

    for shift in range(26):
        decrypted_message = ""
        

        for char in ciphertext:
            if char.isalpha():
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                decrypted_message += shifted_char
            else:
                decrypted_message += char  
        

        print(f"Testing shift by: {shift}")
        print(decrypted_message)
        print()


def main():

    ciphertext = "OMBBWBPMKPWXXI"
    

    analyze(ciphertext)

if __name__ == "__main__":
    main()


