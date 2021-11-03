progLang = { # prog lang name and lil desc
    'Go' : 'A statically typed, compiled programming language designed at Google',
    'Java' : 'A high-level, class based, object-oriented programming language that is designed to have as few implementation dependencies as possible',
    'C++' : 'A general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes"',
    'Python' : 'An interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation',
    'R' : 'A programming language and free software environment for statistical computing and graphics supported by the R Core Team and the R Foundation for Statistical Computing'
}

indexing = { # create an index for each language name
    1 : 'Go',
    2 : 'Java',
    3 : 'C++',
    4 : 'Python',
    5 : 'R'
}

def printDict(): # A function ask for the number
    for i in range(5):
        a = int(input("Enter number (1-5) : "))
        print(indexing[a],"\n",progLang[indexing[a]],"\n",sep="")
        # output key and value
        
printDict()


# Manual

# print(
#     indexing[3],"\n",progLang[indexing[3]],"\n\n",
#     indexing[2],"\n",progLang[indexing[2]],"\n\n",
#     indexing[4],"\n",progLang[indexing[4]],"\n\n",
#     indexing[1],"\n",progLang[indexing[1]],"\n\n",
#     indexing[5],"\n",progLang[indexing[5]],"\n\n"
# )