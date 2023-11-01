import sys


def negate(clause):
    if '!' in clause:
        return clause[1:]
    else:
        return '!' + clause

def resolve(clauseI, clauseJ):
    #resolve a pair of clauses
    #keep i, negate j, see if same (if so they resolve)
    negatedJ = negate(clauseJ)
    newClauses = []
    if(clauseI == negatedJ):
        newClauses.append("[]")
    else:
        newClauses.append(clauseI + ',' + clauseJ)
    
    print(newClauses)
    return newClauses
    

def resolution(predicates, variables, constants, functions, clauses):    
    stillResolving = True
    #initial clauses
    clauses0 = clauses.copy()
    newClauses = []
    while stillResolving:
        #start at begining
        x = 0
        while x < len(clauses):
            #print(x)         
            #compare to all clauses after clause X
            y = x + 1
            while y < len(clauses):
                
                resolvents = resolve(clauses[x], clauses[y])
                if '[]' in resolvents:
                    return True
                newClauses = list(set(newClauses) | set(resolvents))            
                y = y + 1
            x = x + 1
        if newClauses in clauses:
            return False
        clauses = list(set(clauses) | set(newClauses))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 lab2.py <file_path>")
        return

    file_path = sys.argv[1]

    #Get info on KB
    with open(file_path, 'r') as file:
        predicates= file.readline().split()
        predicates = predicates[1:]
        print(predicates)
        
        variables = file.readline().split()
        variables = variables [1:]
        print(variables)
        
        constants = file.readline().split()
        constants = constants[1:]
        print(constants)
        
        functions = file.readline().split()
        functions = functions[1:]
        print(functions)

        clauses = file.read().split()
        clauses = clauses[1:]
        print(clauses)
        
    containsEmpty = resolution(predicates, variables, constants, functions, clauses)
    if(containsEmpty):
        print("no")
    else:
        print("yes")
        
        
if __name__ == "__main__":
    main()
