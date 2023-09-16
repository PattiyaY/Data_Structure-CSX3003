graph = [[1,3],[0,2],[1,3],[0,2]] #True
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] #False
# graph = [[4,1],[0,2],[1,3],[2,4],[3,0]] #False
# graph = [[],[3],[],[1],[]] #True
# graph = [[4,8,9,10,11,14,18],[3,4,8,10,13,14,19],[4,5,7,10,14,16,17,19],
#          [1,6,10,14,16],[0,1,2,12],[2,7,8,13],[3,7,8,9,14,16],
#          [2,5,6,10,11,16,17],[0,1,5,6,13,15],[0,6,10,12,14,15,16],
#          [0,1,2,3,7,9,15,16],[0,7,18],[4,9,18],
#          [1,5,8,14,15],[0,1,2,3,6,9,13],[8,9,10,13,16],
#          [2,3,6,7,9,10,15],[2,7],[0,11,12],[1,2]] #False
# graph = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],
#          [],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],
#          [],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],
#          [37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],
#          [46,48,49],[46,47,49],[45,46,47,48]] #False
# graph = [[4],[],[4],[4],[0,2,3]] #True


def isBipartite(r):
    if len(graph) < 1:
        return True

    while q != []:
            n1 = q.pop()
            if n1 < size:
                if graph[n1] == []:
                    q.append(n1+1)
                    continue
                for n2 in graph[n1]:
                    if color[n2] == None:
                        color[n2] = 'BLUE' if color[n1] == 'RED' else 'RED'
                        q.append(n2)
                    else:
                        if color[n2] == color[n1]:
                            return False #'Graph is not Bipartite'
                Answer = True #'Graph is Bipartite'
                if q == []:
                    q.append(n1+1)

    return Answer

global q
global color

size = len(graph)
color = [None]*size
q = None

#Set default value
q = [0]
color[0] = 'RED'
Answer = False
print(isBipartite(q))