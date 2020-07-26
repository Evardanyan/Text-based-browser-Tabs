# Text-based-browser-Tabs
Description
Let's make our browser store web pages in a file and show them if the user types a shortened request (for example, wikipedia instead of wikipedia.org). You can store each page as a separate file or find another way to do this. But your program should accept one command line argument which is a directory to store the files, and your web pages should be saved inside this directory.

Objectives
At this stage, your program should:

Check if the user has entered a valid URL. It must contain at least one dot, for example, bloomberg.com. If the URL is incorrect, the browser should output an error message (it should contain the word error) and wait for another URL.
Accept a command-line argument which is a directory for saved tabs. For example, if the argument is dir, then you need to create a folder with the name dir and save all web pages that the user downloads in this folder.
Save this web page in a file. After that, the user needs to have a simple way to see the saved web page by typing "bloomberg". The rule is simple: you just need to remove the last dot and everything that comes after it. bloomberg.com becomes bloomberg, en.wikipedia.org becomes en.wikipedia.
Check out a tutorial to learn how to work with files and create folders in Python.

Example
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

> python browser.py dir-for-files
> bloomberg.com
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
 
> bloomberg
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
 
> nytimes
Error: Incorrect URL
 
> exit
