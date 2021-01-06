import re


def main():
    print_intro()
    print_menu()
    session = True
    while session:
        user_input = input("[sesh] >> ")
        text = ""
        if bool(re.search(r"\s", user_input)):
            cmd, text = strip_text(user_input)
            # print(text)
        else:
            cmd = user_input
        # print(cmd)
        # print(text)
        if cmd.lower() == "auto" or cmd.lower() == "autokey":
            tableau("auto", text)
            # print("auto key")
        elif cmd.lower() == "at" or cmd.lower() == "atbash":
            atbash(text)
        elif cmd.lower() == "bac" or cmd.lower() == "bacon" or cmd.lower() == "baconian":
            baconian(text)
        elif cmd.lower() == "beau" or cmd.lower == "beaufort":
            tableau("beau", text)
        elif cmd.lower() == "cae" or cmd.lower() == "caesar":
            caesar(text)
        elif cmd.lower() == "run" or cmd.lower() == "running":
            tableau("run", text)
        elif cmd.lower() == "rot13" or cmd.lower() == "rot":
            rot13(text)
        elif cmd.lower() == "vig" or cmd.lower() == "vignere":
            tableau("vg", text)
        elif (
            cmd.lower() == "q"
            or cmd.lower() == "quit"
            or cmd.lower() == "e"
            or cmd.lower() == "exit"
        ):
            session = False
            print("[sesh] cypher unknown.")
        elif cmd == "?":
            print("")
            print_menu()
        else:
            print("[sesh] enter a valid command.")
    


def strip_text(user_input):
    input_arry = (str(i) for i in user_input.split(" ", 1))
    cmd_or_key = next(input_arry)

    text = next(input_arry)
    text.strip()
    return cmd_or_key, text


def print_intro():
    print(" ▄▄·  ▄· ▄▌ ▄▄▄· ▄ .▄▄▄▄ .▄▄▄      .▄▄ · ▄▄▄ ..▄▄ · .▄▄ · ▪         ▐ ▄ ")
    print("▐█ ▌▪▐█▪██▌▐█ ▄███▪▐█▀▄.▀·▀▄ █·    ▐█ ▀. ▀▄.▀·▐█ ▀. ▐█ ▀. ██ ▪     •█▌▐█")
    print("██ ▄▄▐█▌▐█▪ ██▀·██▀▐█▐▀▀▪▄▐▀▀▄     ▄▀▀▀█▄▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌")
    print("▐███▌ ▐█▀·.▐█▪·•██▌▐▀▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌")
    print("·▀▀▀   ▀ • .▀   ▀▀▀ · ▀▀▀ .▀  ▀     ▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪")
    print("                                                        [cypher session]\n")


def print_menu():
    print("[?] prints menu")
    print("[auto]key -e (or -d) key text")
    print("[at]bash text")
    print("[bac]onian -e (or -d) text")
    print("[beau]fort key text")
    print("[cae]sar -e (or -d) shift text")
    print("[rot]13 text")
    print("[run]ning -e (or -d) text")
    print("[vig]nere -e (or -d) key text")
    print("[q]uit")
    print("[ type in the full command or the letters in the brackets ]")
    print("[ use the -e flag to encrypt, -d to decrypt ]\n")


def atbash(text):
    cypher_str = ""

    def get_atbash_char(text_char):
        if text_char == "a":
            return "z"
        elif text_char == "b":
            return "y"
        elif text_char == "c":
            return "x"
        elif text_char == "d":
            return "w"
        elif text_char == "e":
            return "v"
        elif text_char == "f":
            return "u"
        elif text_char == "g":
            return "t"
        elif text_char == "h":
            return "s"
        elif text_char == "i":
            return "r"
        elif text_char == "j":
            return "q"
        elif text_char == "k":
            return "p"
        elif text_char == "l":
            return "o"
        elif text_char == "m":
            return "n"
        elif text_char == "n":
            return "m"
        elif text_char == "o":
            return "l"
        elif text_char == "p":
            return "k"
        elif text_char == "q":
            return "j"
        elif text_char == "r":
            return "i"
        elif text_char == "s":
            return "h"
        elif text_char == "t":
            return "g"
        elif text_char == "u":
            return "f"
        elif text_char == "v":
            return "e"
        elif text_char == "w":
            return "d"
        elif text_char == "x":
            return "c"
        elif text_char == "y":
            return "b"
        elif text_char == "z":
            return "a"
        else:
            return text_char

    for i in text:
        cypher_str += get_atbash_char(i)
    print("[atbash] {} >> {}".format(text, cypher_str))


def baconian(text):
    cypher_str = ""

    def decrypt_bacon(text_char):
        if text_char == "aaaaa":
            return "a"
        elif text_char == "aaaab":
            return "b"
        elif text_char == "aaaba":
            return "c"
        elif text_char == "aaabb":
            return "d"
        elif text_char == "aabaa":
            return "e"
        elif text_char == "aabab":
            return "f"
        elif text_char == "aabba":
            return "g"
        elif text_char == "aabbb":
            return "h"
        elif text_char == "abaaa":
            return "i"
        elif text_char == "abaab":
            return "j"
        elif text_char == "ababa":
            return "k"
        elif text_char == "ababb":
            return "l"
        elif text_char == "abbaa":
            return "m"
        elif text_char == "abbab":
            return "n"
        elif text_char == "abbba":
            return "o"
        elif text_char == "abbbb":
            return "p"
        elif text_char == "baaaa":
            return "q"
        elif text_char == "baaab":
            return "r"
        elif text_char == "baaba":
            return "s"
        elif text_char == "baabb":
            return "t"
        elif text_char == "babaa":
            return "u"
        elif text_char == "babab":
            return "v"
        elif text_char == "babba":
            return "w"
        elif text_char == "babbb":
            return "x"
        elif text_char == "bbaaa":
            return "y"
        elif text_char == "bbaab":
            return "z"
        else:
            return text_char

    def makin_bacon(text_char):
        if text_char == "a":
            return "aaaaa"
        elif text_char == "b":
            return "aaaab"
        elif text_char == "c":
            return "aaaba"
        elif text_char == "d":
            return "aaabb"
        elif text_char == "e":
            return "aabaa"
        elif text_char == "f":
            return "aabab"
        elif text_char == "g":
            return "aabba"
        elif text_char == "h":
            return "aabbb"
        elif text_char == "i":
            return "abaaa"
        elif text_char == "j":
            return "abaab"
        elif text_char == "k":
            return "ababa"
        elif text_char == "l":
            return "ababb"
        elif text_char == "m":
            return "abbaa"
        elif text_char == "n":
            return "abbab"
        elif text_char == "o":
            return "abbba"
        elif text_char == "p":
            return "abbbb"
        elif text_char == "q":
            return "baaaa"
        elif text_char == "r":
            return "baaab"
        elif text_char == "s":
            return "baaba"
        elif text_char == "t":
            return "baabb"
        elif text_char == "u":
            return "babaa"
        elif text_char == "v":
            return "babab"
        elif text_char == "w":
            return "babba"
        elif text_char == "x":
            return "babbb"
        elif text_char == "y":
            return "bbaaa"
        elif text_char == "z":
            return "bbaab"
        else:
            return text_char

    if bool(re.search(r"-e", text)):
        text_arry = (str(i) for i in text.split("-e", 1))
        choice = next(text_arry)
        text = next(text_arry)

        for i in text:
            cypher_str += makin_bacon(i)
    else:
        text_arry = (str(i) for i in text.split("-d", 1))
        choice = next(text_arry)
        text = next(text_arry)
        n = 5
        bacon_strings = []
        text = text.replace(" ", "")
        text.strip()
        # print(text)

        for i in range(0, len(text), n):
            bacon_strings.append(text[i: i + n])

        # print(bacon_strings)

        for i in bacon_strings:
            cypher_str += decrypt_bacon(i)

    print("[bacon] {} >> {}".format(text, cypher_str))


def caesar(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cypher_str = ""

    def strip_caesar_arg(text):

        if bool(re.search(r"-e", text)):
            text_arry = (str(i) for i in text.split("-e ", 1))
            blank = next(text_arry)
            text = next(text_arry)
            text = text.strip()
        else:
            text_arry = (str(i) for i in text.split("-d ", 1))
            blank = next(text_arry)
            text = next(text_arry)
            text = text.strip()

        text_arry = (str(i) for i in text.split(" ", 1))
        shift = int(next(text_arry))
        text = next(text_arry)
        return shift, text

    def encrypt(shift, text_char):
        if text_char == " ":
            return text_char
        x = alphabet.index(text_char)
        return alphabet[(x + shift) % 26]

    def decrypt(shift, text_char):
        if text_char == " ":
            return text_char
        x = alphabet.index(text_char)
        return alphabet[(x - shift) % 26]

    if bool(re.search(r"-e", text)):
        shift, text = strip_caesar_arg(text)
        # print("stripped " + text)
        # print("shift %d" %(shift))
        # print(text)
        for i in text:
            cypher_str += encrypt(shift, i)
    else:
        shift, text = strip_caesar_arg(text)

        for i in text:
            cypher_str += decrypt(shift, i)

    print("[caesar] {} >> {}".format(text. cypher_str))


def rot13(text):
    cypher_str = ""

    def get_rot13_char(text_char):
        if text_char == "a":
            return "n"
        elif text_char == "b":
            return "o"
        elif text_char == "c":
            return "p"
        elif text_char == "d":
            return "q"
        elif text_char == "e":
            return "r"
        elif text_char == "f":
            return "s"
        elif text_char == "g":
            return "t"
        elif text_char == "h":
            return "u"
        elif text_char == "i":
            return "v"
        elif text_char == "j":
            return "w"
        elif text_char == "k":
            return "x"
        elif text_char == "l":
            return "y"
        elif text_char == "m":
            return "z"
        elif text_char == "n":
            return "a"
        elif text_char == "o":
            return "b"
        elif text_char == "p":
            return "c"
        elif text_char == "q":
            return "d"
        elif text_char == "r":
            return "e"
        elif text_char == "s":
            return "f"
        elif text_char == "t":
            return "g"
        elif text_char == "u":
            return "h"
        elif text_char == "v":
            return "i"
        elif text_char == "w":
            return "j"
        elif text_char == "x":
            return "k"
        elif text_char == "y":
            return "l"
        elif text_char == "z":
            return "m"
        else:
            return text_char

    for i in text:
        cypher_str += get_rot13_char(i)

    print("[rot13] {} >> {}".format(text, cypher_str))


def tableau(tab_type, some_str):
    tabula_recta = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z'],
        ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
         'x', 'y', 'z', 'a'],
        ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', 'a', 'b'],
        ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', 'a', 'b', 'c'],
        ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'a', 'b', 'c', 'd'],
        ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
         'b', 'c', 'd', 'e'],
        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
         'c', 'd', 'e', 'f'],
        ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
         'd', 'e', 'f', 'g'],
        ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h'],
        ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i'],
        ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j'],
        ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k'],
        ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l'],
        ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm'],
        ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n'],
        ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o'],
        ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p'],
        ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q'],
        ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r'],
        ['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's'],
        ['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't'],
        ['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u'],
        ['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v'],
        ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w'],
        ['y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x'],
        ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y']]

    def check_cypher(tab_type, some_str):

        if tab_type == "auto":
            if bool(re.search(r"-e", some_str)):
                some_str = strip_arg(some_str)
                key, text = strip_text(some_str)
                cypher_key = build_autokey(key, text)
                cypher_str = autokey(cypher_key, text)
            else:
                some_str = strip_arg(some_str)
                key, text = strip_text(some_str)
                cypher_key = build_autokey(key, text)
                cypher_str = auto_decrypt(cypher_key, text)
            print("[autokey] {} >> {}".format(text, cypher_str))
        elif tab_type == "beau":
            key, text = strip_text(some_str)
            key = build_beaukey(key, text)
            cypher_str = beaufort(key, text)
            print("[beaufort] {} >> {}".format(text, cypher_str))
        elif tab_type == "run":
            if bool(re.search(r"-e", some_str)):
                text = strip_arg(some_str)
                cypher_key = build_runningkey(text)
                cypher_str = autokey(cypher_key, text)
            else:
                text = strip_arg(some_str)
                cypher_key = build_runningkey(text)
                cypher_str = auto_decrypt(cypher_key, text)
            print("[running] {} >> {}".format(text, cypher_str))
        elif tab_type == "vg":
            if bool(re.search(r"-e", some_str)):
                some_str = strip_arg(some_str)
                key, text = strip_text(some_str)
                cypher_key = build_beaukey(key, text)
                cypher_str = autokey(cypher_key, text)
            else:
                some_str = strip_arg(some_str)
                key, text = strip_text(some_str)
                cypher_key = build_beaukey(key, text)
                cypher_str = auto_decrypt(cypher_key, text)
            print("[vignere] {} >> {}".format(text, cypher_str))

        # print(tabula_recta)

    def strip_arg(text):
        temp_text = ""
        if bool(re.search(r"-e", text)):
            text_arry = (str(i) for i in text.split("-e ", 1))
            blank = next(text_arry)
            temp_text = next(text_arry)
            temp_text = temp_text.strip()
        else:
            text_arry = (str(i) for i in text.split("-d ", 1))
            blank = next(text_arry)
            temp_text = next(text_arry)
            temp_text = temp_text.strip()
        return temp_text

    def autokey(cypher_key, text):
        # cypher_key = build_autokey(key, text)
        # text = list(text)
        temp_text = text.upper()
        cypher_str = ""
        for i in range(0, len(cypher_key)):
            if temp_text[i] == ' ':
                cypher_str += " "
            else:
                col_char = cypher_key[i]
                row_char = temp_text[i]
                col = ord(chr(ord(col_char) - 65))
                row = ord(chr(ord(row_char) - 65))
                cypher_str += tabula_recta[col][row]
        return cypher_str

    def auto_decrypt(cypher_key, cypher_text):
        # print(cypher_key)
        # print(len(cypher_key))
        # print(cypher_text)
        # print(len(cypher_text))
        temp_text = cypher_text.upper()
        decrypted_str = ""
        for i in range(0, len(cypher_text)):
            if temp_text[i] == ' ':
                decrypted_str += " "
            else:
                row_char = cypher_key[i]
                col_char = temp_text[i]
                col = ord(col_char) - ord(row_char)
                if col < 0:
                    col += 26
                # print(col)
                decrypted_str += tabula_recta[col][0]
                # print(decrypted_str)
        return decrypted_str
    
    def beaufort(cypher_key, text):
        cypher_str = ""
        cypher_key = cypher_key.lower()
        temp_text = text.upper()
        for i in range(0, len(cypher_key)):
            if temp_text[i] == ' ':
                cypher_str += " "
            else:
                col = ord(temp_text[i]) - 65
                # print(col)
                for j in range(0, len(tabula_recta[col])):
                    # print(tabula_recta[col][j])
                    # print(cypher_key[i])
                    if cypher_key[i] == tabula_recta[col][j]:
                        cypher_str += tabula_recta[0][j]
                        # print(cypher_str)
        
        return cypher_str
                

    def build_autokey(key, text):
        key_plus_text = key + text.replace(" ", "")
        new_key = ""
        j = 0
        for i in range(0, len(text)):
            if text[i] == " ":
                new_key += " "
            else:
                new_key += key_plus_text[j]
                j += 1
        # print(new_key)
        return new_key.upper()

    def build_beaukey(key, text):
        # print("len text: {}".format(len(text)))
        new_key = ""
        j = 0
        for i in range(0, len(text)):
            if text[i] == " ":
                new_key += " "
            else:
                if j == len(key):
                    j = 0
                new_key += key[j]
                j += 1

        return new_key.upper()
    
    def build_runningkey(text):
        # enter some passage from a book
        book_string = "A murder of ravens took flight from the twisted towers of Harrenhal On the Red Fork Lord Jason Lannister found himself facing the Lord of Pinkmaiden old Petyr Piper and the Lord of Wayfarers Rest Tristan Vance Though the westermen outnumbered their foes the riverlords knew the ground Thrice the Lannisters tried to force the crossing and thrice they were driven back in the last attempt Lord Jason was dealt a mortal wound at the hand of a grizzled squire Pate of Longleaf"
        book_string = book_string.replace(" ", "")
        new_key = ""
        j = 0
        for i in range(0, len(text)):
            if text[i] == " ":
                new_key += " "
            else:
                new_key += book_string[j]
                j += 1
        return new_key.upper()

    check_cypher(tab_type, some_str)


main()
