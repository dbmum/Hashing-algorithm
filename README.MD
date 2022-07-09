# Hashing program

As a programmer I am always looking to learn new things and challenge myself. I like taking on new tasks to be able to increase the quality of my work.

In this program, I am trying to make my own hashing function, similar to the SHA256, that can take an input and output a hexadecimal representation of a hash.

I made this practice some of the principles about cybersecurity in the tech industry. I aim to more fully understand how one-way hashing works, and apply that to other security features that I implement

[Main Hashing Function](Hash.py)

# Development Environment

* Python

* VS Code

# Goals of the hashing function

To be a good hashing function according to Robbi Rahim in his book [IJSIA](https://www.researchgate.net/publication/313759309_128_Bit_Hash_of_Variable_Length_in_Short_Message_Service_Security), you need the following (Where H is the hashing function):

* H can apply to a block of data of any size. 
* H produces output with a fixed length. 
* It is relatively easy to compute H (x) for any x. 
* Let it x; it can be computational to find y ≠ x with H (y) = H (x).
* Use all of the input data to create the output.

We will have tests in the code to assert several of these parameters

# Future goals for the project

* Allow for reading from a file
* Make the output always the same length of characters, regardless of input length
