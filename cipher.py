import os, sys, math, argparse, os.path

# cipher.py
#
# A command-line tool implementing encryption and decryption that include Caesar, Viginère, Monoalphabetic,
# Polyalphabetic, and Route Ciphers.
#
# Usage:
#
# -i: provide input file name
# -c: encryption/decryption options (see -h for options)
# -o: provide an output file name(optional)
#
# Example Usage:
#
# -i test.txt -o encrypted.txt -c 1
#
# Copyright 2018 Emmit Parubrub



def read_input(input_file_name):
    """read in file based on name provided"""
    if not os.path.exists(input_file_name):
        print('The file %s does not exist... Exiting now ...' % (input_file_name))
        sys.exit()
    else:
        input_file = open(input_file_name)
        input_file_content = input_file.read()
        input_file.close()
        return input_file_content



def write_output(output_file_name, output_content):
    """ write the output file based on output name provided and
        output information
    """
    output_file = open(output_file_name, 'w')
    output_file.write(output_content)
    output_file.close()
    return 0

class caesar_cipher:
    def encrypt(content):
        """ encrypt content using the Caesar Cipher method by applying
            chr() and ord() functions and shifting the letters
            by 3 (skips spaces)
        """
        encrypted_data = ""
        for i in content:
            if (chr(ord(i))) == ' ':
                encrypted_data += ' '
            else:
                encrypted_data += (chr(ord(i) + 3))
        return encrypted_data

    def decrypt(content):
        """ decrypt content using a reverse Caesar Cipher method"""
        decrypted_data = ""
        for i in content:
            if (chr(ord(i))) == ' ':
                decrypted_data += ' '
            else:
                decrypted_data += (chr(ord(i) - 3))
        return decrypted_data


class vig_cipher:
    def encrypt(content):
        """ encrypt content using the Viginère Cipher method by shifting
            the letters according to the array index (skips spaces)
        """
        encrypted_data = ""
        vig_index = [3, 20, 7]
        ind = 0
        for i in content:
            if (chr(ord(i))) == ' ':
                encrypted_data += ' '
            else:
                encrypted_data += (chr(ord(i) + vig_index[ind]))
                if ind == len(vig_index)-1:
                    ind = 0
                else:
                    ind += 1
        return encrypted_data

    def decrypt(content):
        """decrypt content using a reverse Viginère Cipher method"""
        decrypted_data = ""
        vig_index = [3, 20, 7]
        ind = 0
        for i in content:
            if (chr(ord(i))) == ' ':
                decrypted_data += ' '
            else:
                decrypted_data += (chr(ord(i) - vig_index[ind]))
                if ind == len(vig_index)-1:
                    ind = 0
                else:
                    ind += 1
        return decrypted_data

class monoalphabetic_cipher:
    key = {
        'a': 'Z',
        'b': 'C',
        'c': 'F',
        'd': 'I',
        'e': 'L',
        'f': 'O',
        'g': 'R',
        'h': 'U',
        'i': 'X',
        'j': 'A',
        'k': 'D',
        'l': 'G',
        'm': 'J',
        'n': 'M',
        'o': 'P',
        'p': 'S',
        'q': 'V',
        'r': 'Y',
        's': 'B',
        't': 'E',
        'u': 'H',
        'v': 'K',
        'w': 'N',
        'x': 'Q',
        'y': 'T',
        'z': 'W',
        ' ': ' ',
    }
    def encrypt(content):
        """ encrypt content using the monoalphabetic cipher
            using a python dictionary. We first make a library
            with the key 1 to 1 pairs and add the key alphabets
            to the encrypted data that is returned
        """
        encrypted_data = ""
        for i in content:
            encrypted_data += monoalphabetic_cipher.key[i]
        return encrypted_data

    def decrypt(content):
        """ decrypt the data by first reversing the key and
            using that key to convert the encrypted text to
            a decrypted text
        """
        encrypted_data = ""
        reverse_key = {}
        for key, value in monoalphabetic_cipher.key.items():
            reverse_key[value] = key
        for i in content:
            encrypted_data += reverse_key[i]
        return encrypted_data

class polyalphabetic_cipher:
    key = {
        'a':  u'\u3063',
        'b': 'C',
        'c': 'F',
        'd':  u'\u042E',
        'e': 'L',
        'f': 'O',
        'g':  u'\u3077',
        'h':  u'\u0419',
        'i':  u'\u3071',
        'j':  u'\u042B',
        'k': 'D',
        'l':  u'\u0240',
        'm': 'J',
        'n': 'M',
        'o':  u'\u308D',
        'p':  u'\u0416',
        'q': 'V',
        'r':  u'\u307B',
        's': 'B',
        't':  u'\u0424',
        'u': 'H',
        'v':  u'\u3091',
        'w': 'N',
        'x':  u'\u3092',
        'y':  u'\u0426',
        'z': 'W',
        ' ': ' ',
    }
    def encrypt(content):
        """ encrypt content using the polyalphabetic cipher
            using a python dictionary. We first make a library
            with the key 1 to 1 pairs with American, Japanese,
            and Russian characters using unicode
        """
        encrypted_data = ""
        for i in content:
            encrypted_data += polyalphabetic_cipher.key[i]
        return encrypted_data

    def decrypt(content):
        """ decrypt the data by first reversing the key and
            using that key to convert the encrypted text to
            a decrypted text
        """
        encrypted_data = ""
        reverse_key = {}
        for key, value in polyalphabetic_cipher.key.items():
            reverse_key[value] = key
        for i in content:
            encrypted_data += reverse_key[i]
        return encrypted_data

class route_cipher:
    def encrypt(content):
        """ encrypt content using a route cipher in which the
            content is put into a matrix top to bottom left to
            write then is added to the encrypted matrix from
            right to left top to bottom
        """
        content_list = list(content)
        content_len  = len(content)
        encrypted_data = ""
        w = math.ceil(content_len/3)
        h = 3
        Matrix = [[0 for x in range(w)] for y in range(h)]

        iter = 0
        for x in range(w):
            for y in range(h):
                if iter != content_len:
                    Matrix[y][x] = content_list[iter]
                    iter += 1
                else:
                    Matrix[y][x] = '#'
        print(Matrix)

        for y in (range(h)):
            for x in reversed(range(w)):
                encrypted_data += Matrix[y][x]
        return encrypted_data

    def decrypt(content):
        """ decrypt content using a reverse route method
            by putting content into a matrix, and reading
            the content in the reverse order as the cipher
            had put it
        """
        content_list = list(content)
        content_len  = len(content)
        encrypted_data = ""
        w = math.ceil(content_len/3)
        h = 3
        Matrix = [[0 for x in range(w)] for y in range(h)]
        iter = 0
        for y in range(h):
            for x in reversed(range(w)):
                if iter != content_len:
                    Matrix[y][x] = content_list[iter]
                    iter += 1
                else:
                    Matrix[y][x] = '#'
        print(Matrix)

        for x in (range(w)):
            for y in (range(h)):
                if Matrix[y][x] == "#":
                    encrypted_data += ''
                else:
                    encrypted_data += Matrix[y][x]
        return encrypted_data

# prints all encryption tests
def print_tests(input_file_name, output_file_name):

    print('')

    input_file_content = read_input(input_file_name)
    print('input file content: ', input_file_content)

    print('')

    output_file_content = caesar_cipher.encrypt(input_file_content)
    print('caesar cipher content: ', output_file_content)

    d_output_file_content = caesar_cipher.decrypt(output_file_content)
    print('decrypted caesar cipher: ', d_output_file_content)

    print('')

    output_file_content = vig_cipher.encrypt(input_file_content)
    print('vig cipher content: ', output_file_content)

    d_output_file_content = vig_cipher.decrypt(output_file_content)
    print('decrypted vig cipher: ', d_output_file_content)

    print('')

    output_file_content = monoalphabetic_cipher.encrypt(input_file_content)
    print('substitution cipher content: ', output_file_content)

    d_output_file_content = monoalphabetic_cipher.decrypt(output_file_content)
    print('decrypted substitution cipher: ', d_output_file_content)

    print('')

    output_file_content = polyalphabetic_cipher.encrypt(input_file_content)
    print('polyalphabetic cipher content: ', output_file_content)

    d_output_file_content = polyalphabetic_cipher.decrypt(output_file_content)
    print('decrypted polyalphabetic cipher: ', d_output_file_content)

    print('')

    output_file_content = route_cipher.encrypt(input_file_content)
    print('transposition cipher content: ', output_file_content)

    d_output_file_content = route_cipher.decrypt(output_file_content)
    print('decrypted transposition cipher: ', d_output_file_content)

    print('')

    print("here is your checkmark: " + u'\u2713');

    if write_output(output_file_name, output_file_content) == 0:
        print('encryption success')
    else:
        print('encryption failed')



def parse_args():
    """setsup the argument parser then return correct arguments"""
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt a file')
    parser.add_argument("-i", "--input_file_name", type=str, required=True, dest="input_v",
                        help = 'Please enter an input file name ')
    parser.add_argument("-o", "--output_file_name", type=str, required=False, dest="output_v",
                        default="", help='Please enter an output file name '
                                         '(if you would like the output to be'
                                         'in the input file, leave this blank)')
    parser.add_argument("-c", "--integer_choice", type=int, required=True, dest="choice_v",
                        help='Please enter an integer choice to encrypt/decrypt-----'
                             '0---Caesar encrypt------------------------------------'
                             '1---Viginère encrypt----------------------------------'
                             '2---Substitution encrypt------------------------------'
                             '3---Transposition encrypt-----------------------------'
                             '4---One-Time Pad encrypt------------------------------'
                             '------------------------------------------------------'
                             '5---Caesar decrypt------------------------------------'
                             '6---Viginère decrypt----------------------------------'
                             '7---Substitution decrypt------------------------------'
                             '8---Transposition decrypt-----------------------------'
                             '9---One-Time Pad decrypt------------------------------')

    args = parser.parse_args()
    print(args)
    return args



def check_args(choice, input_file_name, output_file_name,):
    """checks argument validity"""
    if choice > 9 or choice < 0:
        print("error, please pick an integer choice between 0 and 9")
        exit()

    if not os.path.isfile(input_file_name):
        print("error, please input a valid file name (file might "
              "not be in this directory)")
        exit()


def encrypt_write(content, input_file_name, output_file_name, cipher):
    """ writes encrypted content out depending on whether output_file_name is
        empty or not
    """
    if output_file_name == "":
        if write_output(input_file_name, content) == 0:
            print('encryption success: written to', input_file_name, 'with', cipher)
        else:
            print('encryption failed')
    else:
        if write_output(output_file_name, content) == 0:
            print('encryption success: written to', output_file_name, 'with', cipher)
        else:
            print('encryption failed')



def decrypt_write(content, input_file_name, output_file_name, cipher):
    """ writes decrypted content out depending on whether output_file_name is
        empty or not
    """
    if output_file_name == "":
        if write_output(input_file_name, content) == 0:
            print('decryption success: written to', input_file_name, 'with', cipher)
        else:
            print('decryption failed')
    else:
        if write_output(output_file_name, content) == 0:
            print('decryption success: written to', output_file_name, 'with', cipher)
        else:
            print('decryption failed')


def handle_args(choice, input_file_name, output_file_name,):
    if choice == 0:
        input_file_content = read_input(input_file_name)
        output_file_content = caesar_cipher.encrypt(input_file_content)
        encrypt_write(output_file_content, input_file_name, output_file_name, 'Caesar Cipher')
    elif choice == 1:
        input_file_content = read_input(input_file_name)
        output_file_content = vig_cipher.encrypt(input_file_content)
        encrypt_write(output_file_content, input_file_name, output_file_name, 'Viginère Cipher')
    elif choice == 2:
        input_file_content = read_input(input_file_name)
        output_file_content = monoalphabetic_cipher.encrypt(input_file_content)
        encrypt_write(output_file_content, input_file_name, output_file_name, 'Monoalphabetic Cipher')
    elif choice == 3:
        input_file_content = read_input(input_file_name)
        output_file_content = polyalphabetic_cipher.encrypt(input_file_content)
        encrypt_write(output_file_content, input_file_name, output_file_name, 'Polyalphabetic Cipher')
    elif choice == 4:
        input_file_content = read_input(input_file_name)
        output_file_content = route_cipher.encrypt(input_file_content)
        encrypt_write(output_file_content, input_file_name, output_file_name, 'Route Cipher')
    elif choice == 5:
        input_file_content = read_input(input_file_name)
        output_file_content = caesar_cipher.decrypt(input_file_content)
        decrypt_write(output_file_content, input_file_name, output_file_name, 'Caesar Cipher')
    elif choice == 6:
        input_file_content = read_input(input_file_name)
        output_file_content = vig_cipher.decrypt(input_file_content)
        decrypt_write(output_file_content, input_file_name, output_file_name, 'Viginère Cipher')
    elif choice == 7:
        input_file_content = read_input(input_file_name)
        output_file_content = monoalphabetic_cipher.decrypt(input_file_content)
        decrypt_write(output_file_content, input_file_name, output_file_name, 'Monoalphabetic Cipher')
    elif choice == 8:
        input_file_content = read_input(input_file_name)
        output_file_content = polyalphabetic_cipher.decrypt(input_file_content)
        decrypt_write(output_file_content, input_file_name, output_file_name, 'Polyalphabetic Cipher')
    elif choice == 9:
        input_file_content = read_input(input_file_name)
        output_file_content = route_cipher.decrypt(input_file_content)
        decrypt_write(output_file_content, input_file_name, output_file_name, 'Route Cipher')



def main():
    args = parse_args()
    input_file_name = args.input_v
    output_file_name = args.output_v
    choice = args.choice_v
    check_args(choice, input_file_name, output_file_name)
    handle_args(choice, input_file_name, output_file_name)

    #uncomment below to run tests
    #print_tests(input_file_name, output_file_name)



if __name__ == '__main__':
    main()