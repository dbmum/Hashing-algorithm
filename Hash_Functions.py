import Constants
class Hash_Functions:
    
    def hex_step(self,data, number_of_steps):
        """
        Input a hexadecimal string, return a 'stepped string' where letters remain as letters,
        numbers remain as numbers, but they 'increase; in value by one, if they go over range,
        they go back to the beginning, staying as hexadecimal code. the more times you step,
        the more randomized the values become, as long as you step less than 30 times you will
        get new patterns.
        """
        hex_step_table = {
            'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'e',
            'e': 'f',
            'f': 'a',
            '1': '2',
            '2': '3',
            '3': '4',
            '4': '5',
            '5': '6',
            '6': '7',
            '7': '8',
            '8': '9',
            '9': '1'}

        stepped_data = ""
        for char in data:
            if char in hex_step_table:

                for _ in range(number_of_steps):
                    char = hex_step_table[char]

                stepped_data += char
        
        return stepped_data

    """
    Removed Symbolize string, while this could be useful for more variance and encoding
    It is not neccessary because usually a hash is displayed in hexadecimal as a representation
    of binary
    """
    
    def hash(self,data):
        """
        This function inputs a string and outputs a hash in hexadecimal that represents
        the original string. This should meet all of the hash requirements explained in
        the README file. 
        """
        
        c = Constants.Constants()

        # turn a string into its corresponding ascii value
        ascii_string = ""
        for character in str(data):
            char = ord(character)
            ascii_string += str(char)

        # to binary
        binary = bin(int(ascii_string) + c.num_1)

        # invert binary (replace 1's and 0's)
        inverted = ""
        for num in binary:
            if num == "1":
                inverted += "0"
            else:
                inverted +="1"
        
        # change binary to a different base number
        dif_base = int(inverted, c.num_2)

        # make a copy and and do operations, mainly division
        copy = dif_base

        for num in str(copy):
            if num == '0':
                dif_base += c.num_3
            elif num == '1':
                dif_base = dif_base * c.num_4 - c.num_5
            else:
                dif_base = dif_base // int(num) + c.num_6
            
        # Convert to hexadecimal
        hexed = hex(dif_base)
        reverse = hexed[::-1]

        stepped = self.hex_step(reverse, c.num_7)


        return stepped

    def standardize_length(self):
        def make_longer():
            pass
        def make_shorter():
            pass
        pass
        