"""
Recieves a link from wikipedia (or just the title of it) and
finds how far away it is from Philosophy by only clicking the
first link in the page (without counting the dismabiguotions)

V 1.0.0
28/02/2020
@Nabih Estefan Diaz
"""

def depth(link)

    if link == Philosophy:
        return 0
    else:
        newLink = firstLink
        return depth(newLink) + 1

def main(args=sys.argv):
    """
    Run the main logic of the script.

    Args:
        args: a link used to start the program
    """
    link = args[0]
    depth(link)

if __name__ = "__main__"
    main()
