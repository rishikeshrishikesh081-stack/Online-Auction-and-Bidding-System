import os
import random


class split_and_store():
    def split_file(self,txt,id):
        letters_and_digits = txt
        result_str = ''.join((random.choice(letters_and_digits) for i in range(5)))
        lst = []
        for i in result_str:
            lst.append(i)
        result = []
        for x in lst:
            temp = txt.split(x)
            tmp1 = len(temp)
            if tmp1 < 2:
                result.append(temp[tmp1 - 1])
            else:
                result.append(str(temp) + str(tmp1))
        dir1 = '1'
        dir2 = '2'
        dir3 = '3'
        dir4 = '4'
        dir5 = '5'

        if not os.path.exists(dir1):
            os.makedirs(dir1)
        if not os.path.exists(dir2):
            os.makedirs(dir2)
        if not os.path.exists(dir3):
            os.makedirs(dir3)
        if not os.path.exists(dir4):
            os.makedirs(dir4)
        if not os.path.exists(dir5):
            os.makedirs(dir5)
        file1 = os.path.join(dir1, (str(id) + ".txt"))
        file2 = os.path.join(dir2, (str(id) + ".txt"))
        file3 = os.path.join(dir3, (str(id) + ".txt"))
        file4 = os.path.join(dir4, (str(id) + ".txt"))
        file5 = os.path.join(dir5, (str(id) + ".txt"))

        f = open(file1, 'w')
        f.write(result[0])

        f = open(file2, 'w')
        f.write(result[1])
        f = open(file3, 'w')
        f.write(result[2])

        f = open(file4, 'w')
        f.write(result[3])

        f = open(file5, 'w')
        f.write(result[4])

    def encrypt(self,message, key):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        LETTERS = LETTERS.lower()
        encrypted = ''
        for chars in message:
            if chars in LETTERS:
                num = LETTERS.find(chars)
                num += key
                encrypted += LETTERS[num]
        return encrypted










