# Hashing program

As a programmer I am always looking to learn new things and challenge myself. I like taking on new tasks to be able to increase the quality of my work.

In this program, I am trying to make my own hashing function, similar to the SHA256, that can take an input and output a hexadecimal representation of a hash.

I made this practice some of the principles about cybersecurity in the tech industry. I aim to more fully understand how one-way hashing works, and apply that to other security features that I implement.

[Main Hashing Function](Hash.py)

[Video Demonstration](https://youtu.be/5XsRT-CVc4g)

# Development Environment

* Python

* VS Code

* Google Colab

# Goals of the hashing function

To be a good hashing function according to Robbi Rahim in his book [IJSIA](https://www.researchgate.net/publication/313759309_128_Bit_Hash_of_Variable_Length_in_Short_Message_Service_Security), you need the following (Where H is the hashing function):

* H can apply to a block of data of any size. 
* H produces output with a fixed length. 
* It is relatively easy to compute H (x) for any x. 
* Let it x; it can be computational to find y ≠ x with H (y) = H (x).
* Use all of the input data to create the output.

We will have tests in the code to assert several of these parameters

# Future goals for the project

* Do extensive collision testing to be able to find out how secure this hashing function actually is (more than the 460k tests included in the program)
* try to implement this function into a password storing database


# Current output of the main function

The below example goes as follows:

* input
* output (hashed)
```
hello world
2356a458b23d257e574877ecfd885a7f91fa931cf8a48449e7259fcf9711822e

Hello World
116b94c1a89246a95c54368b8e7ec1e841367c8559dd913552f1db434fb497a4

123456
15f6f548bf35c5ca1dc9a715dfeef667ab4329977728c5c13eb7bcdfa4c3db4e

1234567
41eedb3a45ce4c62ed5d7fe938dbdb7f27394529ac193878fd77988c9b96d285

0
ab8f43acc4d3de5a768a7912a7e8d46535ff5bdf87763f2fba3e1ee9d8a55e1d

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
3db65bff1c1ddad26646155a5e4f34f78d332c33b2caf69e37b1cf8e1b3c36ae

=========        
 Test 1        
=========
Test 1 Passed

=========        
 Test 2        
=========
Test 2 Passed

=========        
 Test 3        
=========
Test 3 Passed
```
This final test was to find how many out of 466550 word inputs would have unique hashes
```
number of words
466550

number of unique hashes
466550
```
