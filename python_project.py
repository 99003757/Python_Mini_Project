"""========================================================================
File Name           :   python_project.py
File Description    :   This file illustrate usage of pyhton .iterates as many times as the user input
                        search the given keyword in input file and create file
                        if match found
File created on     :   26 February, 2021
Author              :   Arpita A Kulkarni
PS Number           :   99003757
contact info        : arpita.kulkarni@ltts.com
============================================================================"""
import re
import os

"""-----------------------------SUPER CLASS---------------------------"""
class Firstclass:
    def __init__(self):
        # constructor class to read no of keywords
        # it also read input file
        # flag is to check for exception
        flag = True
        while flag:
            # if Entered input is not digit throws an error
            try:
                string_name = "enter no of keywords to search:\n"
                self.no_of_keyword = int(input(string_name))
                flag = False # clear flag
            except ValueError:
                print("Please enter the correct input value")

# function to read file from input txt
    def function_read(self):
        # opens input file in read mode and reads the file
        self.file_name = open("input.txt", 'r')
        self.file_read_input = self.file_name.read()
        # declare count to count total keyword occurred
        self.count = 0

class Secondclass(Firstclass):
    # second class is inherited from firstclass
    def search_write_function(self):
        Firstclass.function_read(self)
        # loop executes no of times keyword want to search
        for ii in range(int(self.no_of_keyword)):
            # user input takes keyword
            user_input = input("Enter the keyword:\n")
            # split the input file into tuple
            input_split = self.file_read_input.split()
            # remove all character in tuple
            splited = re.split(r'\W+', str(input_split))
            # output file format as per user input
            filename = "{}.txt".format(user_input)
            file_output = open(filename, 'w')
            for i in range(len(splited)):
                # match the given keyword in the input file
                if re.fullmatch(user_input, splited[i], re.M | re.I):
                    string = "The keyword is{0} {1} {2}\n"
                    txt1 = string.format(splited[i - 1],
                                         splited[i],
                                         splited[i + 1])
                    # if match found write
                    file_output.write(txt1)
                    self.count += 1

            if self.count != 0:
                file_output.write("Total count:" + str(self.count))
            file_output.close()
            if self.count == 0:
                print("Entered Keyword not found in the file\n")
                if os.path.isfile(filename):
                    os.remove(filename)


# ask user input to iterate
# oject of second class created
s_object = Secondclass()
# call search write function to do the task
s_object.search_write_function()
s_object.file_name.close()
