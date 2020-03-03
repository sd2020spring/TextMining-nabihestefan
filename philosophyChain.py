"""
Recieves a link from wikipedia (or just the title of it) and
finds how far away it is from Philosophy by only clicking the
first link in the page (without counting the dismabiguotions)

V 1.0.0
28/02/2020
@Nabih Estefan Diaz
"""

import doctest
import requests
import wikipedia
import sys
import string
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html_doc, 'html.parser')
base = 'https://en.wikipedia.org'
philosophy = base + '/wiki/Philosophy'
steps = [[], 0]

def findFirst(link):
    """
    Recieves link to Wikipedia webpage
    Finds and returns string representaing first link in Webpage
    """
    blank = '<p> class="mw-empty-elt"> </p>'
    text = BeautifulSoup(requests.get(link).text, 'html.parser')
    text = text.body.find(id="content").find(id="bodyContent")
    text = text.find(id="mw-content-text").div
    temp = text.next
    while (temp == '\n' or temp.has_attr('class') or temp.name == 'style'):
        temp = temp.next_sibling

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

    newLink = base + temp.a['href']

    #print used for debugging
    print(newLink)

    return newLink



def depth(link):
    """
    Recursive method designed to reach the end of the Philosophy chain

    Base Case: checks if you are in philosophy
        If yes returns 0, you are here, no more steps are needed
        If no goes to recursive case

    Recursive Case:
        calls findFirst which returns a string that includes the first link in
            the current Wiki page
        uses this lin to return 1 + depth(newLink) which will eventually return
            number of steps needed to reach philosphy

    """
    if link == philosophy:
        steps[0].append(philosophy)
        return steps
    else:
        newLink = findFirst(link)
        steps[0].append(link)
        steps[1] += 1
        return depth(newLink)

def main(args=sys.argv):
    """
    Run the main logic of the script.

    Args:
        args: a link used to start the program
    """
    link = args[1]
    result = depth(link)
    print("If you start at " + link + " you are %2d steps away from reaching the Wikipedia philosophy Webpage" %result[1])
    print("The steps taken to reach this were:")
    for i in steps[0]:
        print("\t" + i)

if __name__ == "__main__":
    """
    Starts the program by calling our main function
    """
    main()
