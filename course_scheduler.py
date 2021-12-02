
import sys

class Course:

    ''' Graph Node Format
        
        title       -> instance node's id
            course identifier (i.e. "csc141","mat151","csc496")
        prereqs     -> instance node's parents
        subseqs     -> instance node's children

    '''

    def __init__(self, title, prereqs=[], subseqs=[]):
        self.title = title
        self.prereqs = prereqs
        self.subseqs = subseqs

    def show(self):
        return "{0}\n\t({1})prereqs:{2}\n\t({3})subseqs:{4}".format(self.title, len(self.prereqs), self.prereqs, len(self.subseqs), self.subseqs)

    def __str__(self):
        return self.title


def get_data(filename):
    
    ''' Source file intake function

        WARNING
        Source file intake is NOT ROBUST (will crash when handling misinput)
        
        line-by-line format:

        {title} : {prerequisites} ; {subsequents}

            {title}         -> course identifier (i.e. "csc141","mat151","csc496")
            {prerequisites} -> 0 or more course identifiers. Separated by single spaces
                        {title} node's parents
                    the courses that must be taken before the {title} course can be considered available
            {subsequents}   -> 0 or more course identifiers. Separated by single spaces
                        {title} node's children
                    the courses with the {title} course as a prerequisite

        e.x. : Standard
            "csc142 : csc141 ; csc240 csc231"
            {title}         = "csc142"
            {prerequisites} = "csc141"
            {subsequents}   = "csc240 csc231"
        e.x. : No Prerequisites
            "csc141 : ; csc142"
            {title}         = "csc141"
            {prerequisites} = None
            {subsequents}   = "csc142"
        e.x. : No Subsequents
            "csc417 : csc241 ;"
            {title}         = "csc417"
            {prerequisites} = "csc241"
            {subsequents}   = None
    '''


    # class lookup
    node_map = {}

    with open(filename, "r") as src:
        lines = src.readlines()

        for line in lines:

            entry = line.strip().split(" ")
            
            # find separators
            pre   = entry.index(":")+1
            sub   = entry.index(";")+1

            # read from end-of-line
            subseqs = entry[sub:]
            entry = entry[:sub]

            # add new Course object to node map
            node_map[entry[0]] = Course(entry[0], entry[pre:sub-1], subseqs)

    return node_map



def show_graph(graph):
    ''' Debug function '''

    for k, v in graph.items():
        print(v.show())


def is_satisfied( prereqs, taken ):
    ''' Determines if course prerequisites have been satisfied
            basically just checks if 'prereqs' is a subset of 'taken'
            
            helper function for get_options()
    '''

    for i in prereqs:

        # course has been taken?
        if (i in taken):
            continue 
        elif i == "*": # special case for csc301
            if len(taken) >= prereqs.count("*"):
                continue
        return False

    return True


def get_options(graph, taken):
    ''' Finds next available courses 

            helper function for scheduler()
    '''

    options = []

    for k,v in graph.items():

        # disregard taken courses
        if v.title in taken:
            continue

        # Make sure course prerequisites are satisfied
        if is_satisfied(v.prereqs, taken): 
            options.append(v.title)

    return options


def user_select(options, max_classes):

    ''' User input is NOT ROBUST (will crash when handling misinput) '''

    # get user selection
    print("\nselect up to",max_classes)
    print("(Enter the number before the course id)")
    print("(e.x. : \"> 0 1 2 ...\" )")

    # show options
    for i in range(len(options)):
        print("\t({0}) {1}".format(i, options[i]))

    selection = list(set([ options[int(x)] for x in input("> ").strip().split(" ")[:max_classes] if (0 <= int(x) < len(options)) ]))

    return selection


def scheduler(graph, max_classes, auto_control=True):

    semester = 1

    options = []
    taken = []

    # first options are courses with no prerequisites
    options = [ v.title for k,v in graph.items() if not v.prereqs]

    while options:

        chosen = []
        if auto_control:
            chosen = options[:max_classes] # does this throw an error?
        else:
            chosen = user_select(options, max_classes)

        print("Classes for Semester ({0}): {1}".format(semester, chosen))

        for c in chosen:
            taken.append(c)

        semester += 1

        options = get_options(graph, taken)


    print("It took you",(semester-1),"semesters to finish every class.")


def main():
    ''' main function '''

    print("This program does not handle misinputs in its current state. Be careful that input follows the correct format (indicated each time)")
    
    graph = get_data(sys.argv[1])


    ''' user input is NOT ROBUST (will crash when handling misinput) '''

    max_classes = int(input("\nmax classes per semester? (integer)\n\t> "))

    control = input("Enter 'y' to use auto-scheduler or [enter] for manual control\n\t(y?)> ")
    if "y" in control.strip().lower():
        scheduler(graph, max_classes, auto_control=True)
    else:
        scheduler(graph, max_classes, auto_control=False)

# Do not touch
if __name__ == '__main__':
    main()

