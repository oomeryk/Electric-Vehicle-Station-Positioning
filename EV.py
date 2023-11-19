# Electric Vehicle Charging Station Application for Istanbul Districts


# first function:
"""
 Write a function called check_feasibility which takes two input as tuples: a 
"route" and a "combination". It should return whether the "combination" is feasible for the "route" 
(True) or not (False). Hence the function will return a boolean that shows the feasibility of that 
"route" and "combination". For example the function can read like the following

route = (“Beykoz”, “Cekmekoy”, “Sancaktepe”)
combination = (“Uskudar”, “Kadikoy”)

def check_feasibility(route, combination)
"""

# second function:
"""
Write a function called find_feasible_route_ex that takes a list of "routes" and a 
list of "combinations" and returns a dictionary which gives the feasible "combinations" for all of 
the given "routes". Now you will give the "routes" and "combinations" explicitly, i.e., you won’t use 
the ID’s given in the table. Assume that this function will be used for those "routes" and 
"combinations" which are not given in the tables above. The output will be something like this:

LofCex=[(Atasehir, Kadikoy),(Beykoz, Cekmekoy),(Cekmekoy, Sultanbeyli) ]
LofRex = [(Atasehir, Umraniye),( Beykoz,Cekmekoy,Sancaktepe)]

def find_feasible_route_ex(LofRex, LofCex, …)
"""

# third function:
"""
 Write a function called find_feasible_route that takes (at least) two 
parameters. One of them is a list of "routes" and the other parameter is a list of "combinations". 
It returns a dictionary which gives the feasible "combinations" for all of the given "routes". Please 
use ID’s to generate the dictionaries. The output will be something like this

LofC = [C1,C3, C5]
LofR = [R2, R4]

def find_feasible_route(LofR, LofC, …)

"""



# creating two list that "district" and "distance_matrix" for using distance between districts in functions
# creating district list for using with matrix of distance between districts
district = [
    "Atasehir", "Beykoz", "Cekmekoy", "Kadikoy", "Kartal", "Maltepe", "Pendik", "Sancaktepe", "Sultanbeyli", "Sile", "Tuzla", "Umraniye", "Uskudar"
]

# creating matrix of distance between all districts 
distance_districts =   [[0, 24, 34, 9, 17, 11, 33, 29, 14, 63, 26, 7, 14],
                       [24, 0, 24, 29, 37, 34, 60, 35, 34, 73, 47, 22, 26],
                       [34, 24, 0, 38, 33, 27, 43, 14, 21, 36, 33, 29, 36],
                       [9, 29, 38, 0, 19, 13, 20, 24, 18, 63, 30, 12, 11],
                       [17, 37, 33, 19, 0, 13, 7, 21, 18, 60, 17, 22, 27],
                       [11, 34, 27, 13, 13, 0, 16, 16, 11, 56, 27, 19, 20],
                       [33, 60, 43, 20, 7, 16, 0, 29, 23, 71, 16, 27, 29],
                       [29, 35, 14, 24, 21, 16, 29, 0, 10, 41, 21, 19, 28],
                       [14, 34, 21, 18, 18, 11, 23, 10, 0, 50, 16, 20, 25],
                       [63, 73, 36, 63, 60, 56, 71, 41, 50, 0, 63, 57, 63],
                       [26, 47, 33, 30, 17, 27, 16, 21, 16, 63, 0, 32, 36],
                       [7, 22, 29, 12, 22, 19, 27, 19, 20, 57, 32, 0, 12],
                       [14, 26, 36, 11, 27, 20, 29, 28, 25, 63, 36, 12, 0]]

# defining route tuples
R1 = ("Atasehir", "Umraniye")
R2 = ("Atasehir", "Beykoz", "Cekmekoy")
R3 = ("Atasehir", "Umraniye", "Uskudar")
R4 = ("Beykoz", "Cekmekoy", "Sancaktepe")
R5 = ("Beykoz", "Uskudar", "Umraniye", "Atasehir", "Kadikoy", "Maltepe", "Kartal")
R6 = ("Beykoz", "Cekmekoy", "Sancaktepe", "Sultanbeyli", "Maltepe", "Kartal", "Pendik")

# defining combination tuples "district that include charge station" 
C1 = ("Atasehir", "Kadikoy")
C2 = ("Beykoz", "Cekmekoy")
C3 = ("Beykoz", "Sancaktepe")
C4 = ("Cekmekoy", "Sultanbeyli")
C5 = ("Maltepe", "Kadikoy")
C6 = ("Uskudar", "Kadikoy", "Beykoz")
C7 = ("Beykoz", "Sultanbeyli", "Kartal")
C8 = ("Beykoz", "Atasehir", "Maltepe")

# second question's function will only work for routes and combinations GIVEN above
# second question's function will return route - combination ID  but work route - combination VALUES
# so we created two dictionary with ID and VALUES
# defining two dictionary with routes and combinations above  for using in "second question".
route_dict = {"R1":R1, "R2":R2, "R3":R3, "R4":R4, "R5":R5, "R6":R6}
combination_dict = {"C1":C1, "C2":C2, "C3":C3, "C4":C4, "C5":C5, "C6":C6, "C7":C7, "C8":C8}





##################################################################################################################
# first function:


# create function to return feasibilty for given route, combination and charge_user tuples
# charge_user value received from user as fully charge value
def check_feasibility(route, combination, charge_user):
    
    # if there is no charge station in first district EV car charge == charge_user/2
    # if there is a charge station in first district EV car charge == charge_user
    if route[0] not in combination:
        charge = charge_user/2
    else: charge = charge_user
        
    # create a loop for lenght-1 of district
    for i in range(0, len(route)-1):  
  
        # define index of two district in district list
        district1_index = district.index(route[i])  
        district2_index = district.index(route[i+1])  
        # decrease the charge in moving between two district
        charge -= distance_districts[district1_index][district2_index]  
    
        # if EV car charge is smaller than zero quit in loop and return False
        if charge < 0: 
            break  
 
        # if there is a charge station in current district, EV car charging to charge_user value. 
        for j in range(0, len(combination)):  
            if (route[i+1] == combination[j]):  
                charge = charge_user 
            else: continue
        
    # end of the loop or function, if charge smaller than zero retun False or bigger than zero return True
    if charge > 0: 
        return True
    else:  
        return False
    
    
    
    
    
############################################################################################################
# second function:


# charge_user value received from user as fully charge value
def find_feasible_route_ex(LofR, LofC, charge_user):
    
    # definiation empty dictionary for route-combination key-value
    dictionary = {}
    # loop for route in LofR list
    for route in LofR:
        
        # define empty feasible_combination list for route
        feasible_combination = []
        # loop for combination in LofC list
        for combination in LofC:
            # if there is no charge station in first district EV car charge==charge_user/2
            # if there is a charge station in first district EV car charge==charge_user
            if route[0] not in combination:
                charge = charge_user/2
            else: charge = charge_user

            # create a loop for lenght-1 of district
            for i in range(0, len(route)-1):  

                # define index of two district in district list
                district1_index = district.index(route[i])  
                district2_index = district.index(route[i+1])  
                # decrease the charge in moving between two district
                charge -= distance_districts[district1_index][district2_index]  

                # if EV car charge is smaller than zero quit in loop and return False
                if charge < 0: 
                    break  

                # if there is a charge station in current district, EV car charging to charge_user value. 
                for j in range(0, len(combination)):  
                    if (route[i+1] == combination[j]):  
                        charge = charge_user  
                    else: continue

            # end of the loop, if charge bigger than zero, add current combination to combination list
            if charge > 0: 
                feasible_combination.append(combination)
            else:  
                continue
                
        # add current route"key" and feasible_combination"value" to dictionary         
        dictionary[route] = tuple(feasible_combination)

    return dictionary
    
    
    
    
###############################################################################################################
# third function:


# charge_user value received from user as fully charge value
def find_feasible_route(LofR, LofC, charge_user):
    
    # definiation empty dictionary for route-combination key-value
    dictionary = {}
    # loop for accessing values of LofR list 
    for route in LofR:
        # this function will only work for routes and combinations GIVEN above
        # this function will return route - combination ID  but work route - combination VALUES
        # so we created two dictionary with ID and VALUES above
        ## and this loop for looping by route dictionary lenght
        for r in range(len(route_dict)):
            # this function work with VALUES of route dictionary GIVEN above 
            # and if route that received from user equal one of the VALUES of route dictionary, continue with that route.
            if ( route==tuple(route_dict.values())[r] ):
        
                # define empty feasible_combination list for feasible route
                feasible_combination = []
                # loop for accessing values of LofC list
                for combination in LofC:
                    # this loop for looping by combination dictionary lenght
                    for c in range(len(combination_dict)):
                        # this function work with VALUES of combination dictionary  
                        # and if combination that received from user equal one of the VALUES of combiantion dictionary, continue with that combination.
                        if ( combination==tuple(combination_dict.values())[c] ):


                            # if there is no charge station in first district EV car charge == charge_user/2
                            # if there is a charge station in first district EV car charge == charge_user
                            if route[0] not in combination:
                                charge = charge_user/2
                            else: charge = charge_user

                            # create a loop for lenght-1 of district
                            for i in range(0, len(route)-1):  

                                # define index of two district in district list
                                district1_index = district.index(route[i])  
                                district2_index = district.index(route[i+1])  
                                # decrease the charge in moving between two district
                                charge -= distance_districts[district1_index][district2_index]  

                                # if EV car charge is smaller than zero quit in loop and return False
                                if charge < 0: 
                                    break  

                                # if there is a charge station in current district, EV car charging to charge_user value. 
                                for j in range(0, len(combination)):  
                                    if (route[i+1] == combination[j]):  
                                        charge = charge_user
                                    else: continue

                            # end of the loop, if charge bigger than zero, add current combination to feasible_combination list
                            if charge > 0: 
                                feasible_combination.append(tuple(combination_dict.keys())[c])
                            else:  
                                continue

                # add current route"key" and feasible_combination"value" to dictionary         
                dictionary[tuple(route_dict.keys())[r]] = tuple(feasible_combination)

    return dictionary
    

#########################################################################################
#########################################################################################
 
   
check_feasibility(("Atasehir", "Cekmekoy"), ("Atasehir", "Sancaktepe"), 40)

# output:   True

check_feasibility(("Atasehir", "Cekmekoy"), ("Atasehir", "Sancaktepe"), 33)

# output:   False

#####################################################################

LofCex = (("Beykoz", "Cekmekoy"), ("Kartal", "Sultanbeyli"))
LofRex = (("Atasehir", "Beykoz", "Cekmekoy"), ("Kartal","Maltepe","Pendik"))

find_feasible_route_ex(LofRex, LofCex, 40)

# output:   {('Atasehir', 'Beykoz', 'Cekmekoy'): (),   ('Kartal', 'Maltepe', 'Pendik'): (('Kartal', 'Sultanbeyli'),)}


LofCex = (("Atasehir", "Kadikoy"), ("Beykoz", "Cekmekoy"), ("Cekmekoy", "Sultanbeyli"))
LofRex = (("Atasehir", "Umraniye"), ("Beykoz","Cekmekoy","Sancaktepe"))

find_feasible_route_ex(LofRex, LofCex, 40)

# output:   {('Atasehir', 'Umraniye'): (('Atasehir', 'Kadikoy'),('Beykoz', 'Cekmekoy'),('Cekmekoy', 'Sultanbeyli')),   ('Beykoz', 'Cekmekoy', 'Sancaktepe'): (('Beykoz', 'Cekmekoy'),)}


#####################################################################

LofC = [C1,C3, C5]
LofR = [R2, R4]

find_feasible_route(LofR, LofC, 40)

# output:   {'R2': (), 'R4': ('C3',)}




