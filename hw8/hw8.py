
# @param d Represents dataset
# @param max_weight Represents max weight
def greedy_algo(d, max_weight):

    ds = d.copy()   # for tesing purposes

    # will hold the best combination of objects
    #   for value/weight the greedy way
    best_combo = []

    end_loop = False
    i = 0
    while end_loop == False:

        # end_loop will remain true and end the loop
        #   if there is not an addition to the
        #   knapsack after checking all objects
        end_loop = True

        # will hold the object with the best ratio
        best_object = [0,0]
        best_ratio = 0

        # vw is each Value, weight array
        for vw in ds:

            # if adding current weight is > max, do
            #   not put it in
            if i + vw[0] <= max_weight:
                vw_ratio = vw[1]/vw[0]  # current ratio

                # if the current ratio is better than
                #   the best, replace it
                if vw_ratio > best_ratio:
                    best_object[0] = vw[0]
                    best_object[1] = vw[1]
                    best_ratio = vw_ratio
                    end_loop = False

        if(end_loop == False):
            i += best_object[0]
            best_combo.append(best_object)
            ds.remove(best_object)
    
    return best_combo

#end function


# @param d Represents dataset
# @param wr Represents weight remaining
#           implemented as max weight
# @param n Implemented as length of d
#           is used for base case as
#           no better combos remaining
def dynamic_algo(d,wr,n):

    # base case
    if n == 0 or wr == 0:
        return 0

    # curr_object Contains the target object
    # curr_weight and value respective
    curr_object = d[n-1]
    curr_weight = curr_object[0]
    curr_value = curr_object[1]

    # if the current weight exceeds the
    #   remaining weight go to the next
    #   (n-1) object and try again
    if(curr_weight > wr):
        return dynamic_algo(d,wr,n-1)

    # otherwise, check if the new value(curr)
    #   being added into the equation and changing
    #   remaining weight is larger than if it
    #   were not added, recurse through trying
    #   this with every possible object
    else:
        new_wr = wr-curr_weight
        return max(curr_value + dynamic_algo(d,new_wr,n-1),dynamic_algo(d,wr,n-1))
    
# end function
    


# testing

ds =  [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], \
[103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], \
[110, 107], [111, 108], [113, 107], [114, 110]]


# testing greedy

print("Greedy Algorithm test:")

best_combo100 = greedy_algo(ds,100)
ret = 0
for best_object in best_combo100:
    ret += best_object[1]
print("max weight = 100:",ret)

best_combo200 = greedy_algo(ds,200)
ret = 0
for best_object in best_combo200:
    ret += best_object[1]
print("max weight = 200:",ret)

best_combo300 = greedy_algo(ds,300)
ret = 0
for best_object in best_combo300:
    ret += best_object[1]
print("max weight = 300:",ret)
print()

# testing dynamic

print("Dynamic Algorithm test:")

n = len(ds)

print("max weight = 100:",dynamic_algo(ds,100,n))
print("max weight = 200:",dynamic_algo(ds,200,n))
print("max weight = 300:",dynamic_algo(ds,300,n))