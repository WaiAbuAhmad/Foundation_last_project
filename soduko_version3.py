import random
import collections


#a dictionary with the grid coordinates

game_layout = {"1,1" : 0,"1,2" : 0,"1,3" : 0,"1,4" : 0,"1,5" : 0,"1,6" : 0,"1,7" : 0,"1,8" : 0,"1,9" : 0,
               "2,1" : 0,"2,2" : 0,"2,3" : 0,"2,4" : 0,"2,5" : 0,"2,6" : 0,"2,7" : 0,"2,8" : 0,"2,9" : 0,
               "3,1" : 0,"3,2" : 0,"3,3" : 0,"3,4" : 0,"3,5" : 0,"3,6" : 0,"3,7" : 0,"3,8" : 0,"3,9" : 0,
               "4,1" : 0,"4,2" : 0,"4,3" : 0,"4,4" : 0,"4,5" : 0,"4,6" : 0,"4,7" : 0,"4,8" : 0,"4,9" : 0,
               "5,1" : 0,"5,2" : 0,"5,3" : 0,"5,4" : 0,"5,5" : 0,"5,6" : 0,"5,7" : 0,"5,8" : 0,"5,9" : 0,
               "6,1" : 0,"6,2" : 0,"6,3" : 0,"6,4" : 0,"6,5" : 0,"6,6" : 0,"6,7" : 0,"6,8" : 0,"6,9" : 0,
               "7,1" : 0,"7,2" : 0,"7,3" : 0,"7,4" : 0,"7,5" : 0,"7,6" : 0,"7,7" : 0,"7,8" : 0,"7,9" : 0,
               "8,1" : 0,"8,2" : 0,"8,3" : 0,"8,4" : 0,"8,5" : 0,"8,6" : 0,"8,7" : 0,"8,8" : 0,"8,9" : 0,
               "9,1" : 0,"9,2" : 0,"9,3" : 0,"9,4" : 0,"9,5" : 0,"9,6" : 0,"9,7" : 0,"9,8" : 0,"9,9" : 0}     


def first_line(): #  a function that creates a random list with elements from 1-9 in non sequential order
    
    values = random.sample(range(1,10),9)
    
    return values   


def grid_creater(): # fills in the grid with the created list from first_line() and makes shifting for each row depends on the order
    
    rotation_by_row = [0,-3,-3,-1,-3,-3,-1,-3,-3]
    first_row  = collections.deque(first_line())
    for i in range(1,10):
        first_row.rotate(rotation_by_row[i-1])
        for j in range(1,10):
            game_layout[str(i)+","+str(j)] = first_row[j-1]
    return game_layout
            


def check_row():#a function that check each row of the grid to make sure no digit repeats its self and that it is unique as well
    
    for i in range(1,10):
        row = [game_layout[str(i)+","+str(j)] for j in range(1,10)]
        print(row)
        if len(set(row)) == 9 :
            print("Row number {} is correct".format(i))
        else:
            print("Row number {} is WRONG".format(i))
            
        
def check_column():  #a function that check each column of the grid to make sure no digit repeats its self and that it is unique as well
    
    for i in range(1,10):
        line = [game_layout[str(j)+","+str(i)] for j in range(1,10)]
        print(line)
        if len(set(line)) == 9 :
            print("Column number {} is correct".format(i))
        else:
            print("Column number {} is WRONG".format(i))


def check_cube(cube_number,i,j): # a function that checks a cube out of the 9 cubes inside the grid to make sure that each digit is unique
    
    cube_items = [game_layout[str(a)+","+str(b)] for a in range(i-2,i+1) for b in range(j-2,j+1)]
    print(cube_items)
    cube_items = set(cube_items)
    if len(cube_items) == 9 :
            print("Cube {} is correct".format(cube_number))
    else:
        print("Cube {} is WRONG".format(cube_number))
     
         
            



def check_all_cubes(): # a function that send arguments to the check_cube function to check each cube from the whole 9 cubes in the grid
    counter = 0
    cube_name = "ABCDEFGHI"
    for i in range(3,10,3):
        for j in range(3,10,3):
            
            check_cube(cube_name[counter],i,j)
            counter +=1
            
        


grid_creater()


# print the grid just to check the values and coordinates

def print_grid():
    counter = 1
    for key , value in game_layout.items():
        if counter%9 == 0 :
            print( key , value," ")
        else :
            print(key, value ," ", end = "")

        counter +=1
    


def new_grid():
    grid_creater()
    print_grid()
    
    







        
        
 
