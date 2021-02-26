import re
import os


class Firstclass:

    def __init__(self, no_of_keyword):
        self.no_of_keyword_of_keyword = no_of_keyword
        self.file_name = open("input.txt", 'r')
        self.file_read = self.file_name.read()


class Secondclass(Firstclass):
    def search_write_function(self):
        for ii in range(no_of_key):
            user_input = input("Enter the keyword:\n")
            tt = self.file_read.split()
            nnn = re.split(r'\W+', str(tt))
            filename = "{}.txt".format(user_input)
            file_output = open(filename, 'w')
            count = 0
            for i in range(len(nnn)):
                if re.fullmatch(user_input, nnn[i], re.M | re.I):
                    txt1 = "The keyword is {0} {1} {2}\n ".format(nnn[i - 4],
                                                                  nnn[i],
                                                                  nnn[i + 4])
                    file_output.write(txt1)
                    count += 1

            if count != 0:
                file_output.write("Total count of keyword is: " + str(count))
            file_output.close()
            if count == 0:
                print("Entered Keyword not found in the file\n")
                if os.path.isfile(filename):
                    os.remove(filename)


no_of_key = int(input("enter no of keywords to search:\n"))
s_object = Secondclass(no_of_key)
s_object.search_write_function()
s_object.file_name.close()
