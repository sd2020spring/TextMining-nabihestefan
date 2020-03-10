"""
Recieves a link from wikipedia (or just the title of it) and
finds how far away it is from Philosophy by only clicking the
first link in the page (without counting the dismabiguations)

28/02/2020
@Nabih Estefan Diaz
"""
import doctest
import requests
import sys
import os.path
import string
from bs4 import BeautifulSoup

base = 'https://en.wikipedia.org'
philosophy = base + '/wiki/Philosophy'

def findFirst(link):
    """
    Recieves link to Wikipedia webpage
    Finds and returns string representaing first link in Webpage
    """
    #gets to the content part of the html where we'll find link

    info = BeautifulSoup(requests.get(link).text, 'html.parser')
    info = info.body.find(id="content").find(id="bodyContent")
    info = info.find(id="mw-content-text").div
    info = info.next

    #check to cycle through content till we find first lnk
    while (info == '\n' or info.has_attr('class') or info.name == 'style'):
        info = info.next_sibling

    """
    prints used of debugging
    print(link)
    print('temp')
    print(temp)
    print('temp.a')
    print(temp.a)
    print('\nhref')
    print(temp.a['href'])
    """

    #Fix problem if first paragraph has no link
    while True:
        try:
             newLink = base + info.a['href']
             break
        except TypeError:
            info = info.next_sibling
            while (info == '\n' or info.has_attr('class') or info.name == 'style'):
                info = info.next_sibling
            break

    #Fixed problem with coordinates Coordinates
    while True:
        if newLink == "https://en.wikipedia.org/wiki/Geographic_coordinate_system":
            info = info.next_sibling
            while (info == '\n' or info.has_attr('class') or info.name == 'style'):
                info = info.next_sibling
            newLink = base + info.a['href']
        else:
            break

    #Fix problem with Citations
    while True:
        if info.a.text == "[1]":
            info = info.next_sibling
            while (info == '\n' or info.has_attr('class') or info.name == 'style'):
                info = info.next_sibling
        else:
            break

    newLink = base + info.a['href']
    #print("\t\t" + newLink)
    return newLink[24:]


def depth(link, file, steps):
    """
    Recursive method designed to reach the end of the Philosophy chain
    Base Case: checks if you are in philosophy
        If yes returns 0, you are here, no more steps are needed
        If no goes to recursive case
    Recursive Case:
        calls findFirst which returns a string that includes the first link in
            the current Wiki page
        uses this to return 1 + depth(newLink) which will eventually return
            number of steps needed to reach philosphy
    """
    if link == philosophy:
        file.write("\t" + philosophy + "\n")
        return 0
    else:
        newLink = base + findFirst(link)
        file.write("\t" + link + "\n")
        return 1 + depth(newLink, file, steps)


def main(args=sys.argv):
    """
    Run the main logic of the script.
    Args:
        args: a link used to start the program
    """
    #Find link for name given
    name = args[1]
    name.replace(" ", "_")
    link = base + "/wiki/" + name
    filename = "Philosophy Chain " + name +".txt"
    print(filename)

    #check if file already exists
    if not os.path.isfile(filename):
        #file was not found, we need to find the path
        #open file, write first lines, call recursive function, call final lines
        file = open(filename, "w+")
        file.write("Starting at " + link + ", these are the steps to reach the Wikipedia Philosophy Webpage\n")
        result = depth(link, file, 0)
        file.write("\n\nThese were the %2d steps to reach the Wikipedia Philosophy Webpage" %result)
        file.close()

    #open file for read (either it was found or created)
    #print the links to the user
    with open(filename, "r") as file:
        lines =  file.readlines()
        for line in lines:
            print(line)


if __name__ == "__main__":
    """
    Starts the program by calling our main function
    """
    main()
