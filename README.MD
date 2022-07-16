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

We will have tests in the code to assert several of these parameters

# Future goals for the project

* Allow for reading from a file
* Make the output always the same length of characters, regardless of input length


# Current output of the main function

The below example goes as follows:

* input
* output (hashed)
```
hello world
4d488345ad84facb193895acf91c9bf977ab58878ad8f2cbe27e7681457b5cea

Hello World
39514fe91a7236a319943a787ef8cb824c94ba5a6d51b7dc1658b53dec4823f6

123456
f7d6d9d8b97113dfe9ce8a35c4adb68c83c43e2c77fd55279e47bad64f632d41

1234567
b8ece4cbd16afe8185f94c863fa2559997d5247de8548a78fea9f3d175f36bf7

0
e8b23c2614987df48e64753ad8e3d33bd131a5c3a85e5aff67baa5568798df9d

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
c47d1b6a226be218a573eb7f7c8e7c3d6ebbef1d9cdbbcfca1c71c39ac86be5c
```