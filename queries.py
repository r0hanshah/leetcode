# You are given two arrays of integers a and b, and an array queries containing the queries you are required to process. Every queries[i] can have one of the following two forms:

# [0, i, x]. In this case, you need to add x to the current value of b[i].
# [1, x]. In this case, you need to find the total number of pairs of indices i and j such that a[i] + b[j] = x.
# Perform the given queries in order and return an array containing the results of the queries of the type [1, x].
def solution(a, b, queries):
    # For a = [1, 2, 3], b = [1, 4], and queries = [[1, 5], [0, 0, 2], [1, 5]], the output should be solution(a, b, queries) = [1, 2].
    solutions = []
    
    for query in queries:
        if query[0] == 0:
            b[query[1]] += query[2]
        else:
            count = 0
            othercounter = 0
            for i in range(len(a)):
                for j in range(len(b)):
                    if a[i] + b[j] == query[1]:
                        count += 1
            solutions.append(count)

        # For a = [1, 2, 2], b = [2, 3], and queries = [[1, 4], [0, 0, 1], [1, 5]], the output should be solution(a, b, queries) = [3, 4].
         
        
    return solutions

    
      

a = [1, 2, 3]
b = [1, 4]
queries = [[1, 5], [0, 0, 2], [1, 5]]
print(solution(a, b, queries))