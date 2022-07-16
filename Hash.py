"""
David Mumford

version 1: I have spent several hours trying to figure out different ways
to do a one-way hash of a string. I have implemented a few encryption methods 
in the hopes that my hash will be secure. So far it uses all of the data in the 
string, and is unique, even with one character changed.

Version 2: I have allowed for a shuffling of the data and having a fixed result length
of 64 hexadecimal digits for each input, regardless of input length. This should still
be a good representation of the whole data
"""
import Hash_Functions

def main():
    hf = Hash_Functions.Hash_Functions()
    print("\nhello world")
    print(hf.hash("hello world"))
    
    print("\nHello World")
    print(hf.hash("Hello World"))

    print("\n123456")
    print(hf.hash("123456"))
    
    print("\n1234567")
    print(hf.hash("1234567"))

    print("\n0")
    print(hf.hash("0"))

    print("\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    print(hf.hash("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))




def test():
    hf = Hash_Functions.Hash_Functions()
    print("\n=========\
        \n Test 1\
        \n=========")
        # See that the hashing function can hash input of any size
    try:
        hf.hash('0')
        hf.hash("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        print("Test 1 Passed")
    except:
        print("Test 1 Failed")
    
    print("\n=========\
        \n Test 2\
        \n=========")
        # See that the output hashes have the same number of characters
    if (len(hf.hash('hello')) == len(hf.hash('longer message that needs to hash the same length of code')) ):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
    print("\n=========\
        \n Test 3\
        \n=========")
        # See that the output hash is not equal to the input
    if hf.hash('test') != 'test':    
        print("Test 3 Passed\n")
    else:
        print("Test 3 Failed\n")

main()
test()