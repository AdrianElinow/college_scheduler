
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

    ###

    return node_map

def show_graph(graph):
    ''' debug function '''

    for k, v in graph.items():
        print(v.show())


def scheduler(graph, taken=[]):

    ''' Primary program loop '''

    pass
    

def main():
    ''' main function '''
    
    graph = get_data(sys.argv[1])

    show_graph(graph)

    scheduler(graph)

# Do not touch
if __name__ == '__main__':
    main()

