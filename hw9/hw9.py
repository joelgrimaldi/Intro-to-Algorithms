import random
import json

def pr1(data,d,t):

    # converts data to adjacency list which holds
    # a vertex, v, as a key and all verticies that
    # link to v as the value
    g = {}
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if data[i][j] == 1:
                if j in g.keys():
                    g[j].append(i)
                else:
                    g[j] = [i]
        
    i = 0
    webpages_visited = []
    len_keys = len(g.keys())
    random_webpage = random.randint(0,len_keys-1)
    curr = list(g.keys())[random_webpage]
    while i < t:
        p = random.uniform(0,1)
        if p < d:
            len_curr = len(g[curr])
            random_linked = random.randint(0,len_curr-1)
            curr = g[curr][random_linked]
        if p > d:
            len_keys = len(g.keys())
            random_webpage = random.randint(0,len_keys-1)
            curr = list(g.keys())[random_webpage]
        webpages_visited.append(curr)
        i += 1
    
    if(len(webpages_visited) == 0):
        return None

    first_run = True
    for webpage in webpages_visited:
        if first_run:
            ret = {webpage : 1}
            first_run = False
            continue

        if webpage in ret:
            ret[webpage] += 1
        else:
            ret[webpage] = 1
    
    ret_s = ""
    for s in sorted(ret.keys()):
        ret_s += "Website " + str(s+1) + ": frequency " + str(ret[s]/t) + "\n"
    
    return ret_s
# end function


def pr2(data,d,t):

    g = {}
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if data[i][j] == 1:
                if j in g.keys():
                    g[j].append(i)
                else:
                    g[j] = [i]

    if(len(g.keys()) == 0):
        return None

    default = 1/len(g.keys())
    ret = {}
    for key in g.keys():
        ret[key] = default

    first = True
    i = 0
    while i < t:
        # for each website
        for website in ret.keys():
            combined_prt = 0
            # for each hyperlink to website
            for link in g[website]:
                curr_L = 0
                # for each link from hyperlink
                # this calculates L(hyperlink)
                for links in data[link]:
                    if links == 1:
                        curr_L += 1
                combined_prt += ret[link]/curr_L
            ret[website] = (1-d)/len(ret.keys()) + d*combined_prt
        i += 1
    
    ret_s = ""
    for s in sorted(ret.keys()):
        ret_s += "Website " + str(s+1) + ": frequency " + str(ret[s]) + "\n"
    
    return ret_s
#end function
    
    
datafile = open("lab3.dat", "r")
data = json.load(datafile)
datafile.close()
# g = {
#     "A" : ["A","B","C"],
#     "B" : ["B"],
#     "C" : ["C","A"],
#     "D" : ["D","B","C"],
# }
d = .9
t = 100000

print(pr1(data,d,t))
print(pr2(data,d,t))