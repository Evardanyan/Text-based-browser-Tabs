import os
import sys


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
args = sys.argv # convert arguments to flocr
dir_name = args[1]


try:
        # Create target Directory
    os.mkdir(f'C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{dir_name}')
    print("Directory ", dir_name, " Created ")
except FileExistsError:
    print("Directory ", dir_name, " already exists")

bloomberg = 'C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/bloomberg'
nytimes = 'C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/nytimes'

file_handle1 = open(bloomberg, "w", encoding="utf-8")
file_handle1.write("""
        The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
        """)
file_handle1.close()

file_handle2 = open(nytimes, "w", encoding="utf-8")
file_handle2.write("""
        This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.
        """)
file_handle2.close()

rule = ["bloomberg.com", "nytimes.com", ".", "bloomberg", "nytimes", "exit"]

while True:
    url_input = str(input())
    if url_input not in rule:
        print("error")
    elif url_input == "bloomberg.com":
        print(bloomberg_com)
    elif url_input == "nytimes.com":
        print(nytimes_com)
    if url_input == "bloomberg":
        file_handle_bloomberg = open(bloomberg, "r")
        print(file_handle_bloomberg.read())
        file_handle_bloomberg.close()
    if url_input == "nytimes":
        file_handle_nytimes = open(nytimes, "r")
        print(file_handle_nytimes.read())
        file_handle_nytimes.close()

    if url_input == "exit":
        break

