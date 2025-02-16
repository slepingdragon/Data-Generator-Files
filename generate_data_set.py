import random
import numpy as np
class Generate_Data_Set_Read_Me:
    """
    Generate Data Sets
    ==================
    
    Provides:
        Various different ways of generating linear, or nonlinear data points in either arrays, or graphing points
        mostly for training algorythyms for testing etc.
        
    
    Also used to get data whenever needed for graphing purposes etc.
    
    Additional Information ->
    ----------------------
        - Various bools in this file    On = True    False = Off
            - For Example...
                - If there is a bool in a method like from 'generate_Linear_data_points()' It will have 'abs=False'
                  if that abs == True that means any value that is returned in the dependent value will be positive always.
    
    Methods ->
    =======
        - generate_NonLinear_array (width, height, max_value, min_value, round_on_off, round_value)
            - Generates you an array with random values between min and max values
            - You give it a size and it will return you that array with all rand uniform values
            - round_on_off, will round each value if set to True
            - Round_value how many decimal places to round to. Default = 5
            - Finally, returns you the array
        
        - generate_Linear_data_points( xpoints, deviation, ypoint_start_value, abs (on or off), max_value_cap ypoint (on or off), linear_line_adder)
            - Generates a list with tuples of cordinates that are linearized
            - xpoints Default = 10
            - Deviation -> How far off you want to randomize your y values from the linearized line Default = 5
            - ypoint_start_value -> where you y point will first start for the linearization Default = 0
            - abs, returns all values of the random y to a positive. If put True
            - max_value_cap -> looks at each y value and make sure that wont go over the highest y value there can be
            - linear_line_adder -> How much you want the y value to increase Default = 1
            - x_point_adder -> How much you want the y value to increase Default = 1
            
    
    Uses: 
    -----
    numpy, random
    
    """
    pass



def generate_NonLinear_array(width:float=1,height:float=1,max_value:float=1,min_value:float=0,round_on_off:bool=False,round_value:int=5) -> list:
    """ 
    Generates a NonLinear array
    ----
    Default width size = 1,    Default height size = 1,

    Default minimum value = 0,    Default maximum value = 1

    "All array values round to 5 points", if round_on_off = True and round_value = 5
    round_value default = 5 will only round if round_on_off == True
    
    Minimum value = the lowest value that can be generated
    
    Maximum value = the highest value that can be generated
    """
    array = []
    for y in range(0,height):
        array.append([])
        for x in range(0, width):
            if round_on_off == True:
                rand_value = round(random.uniform(min_value,max_value), round_value)
            else:
                rand_value = random.uniform(min_value,max_value)
            array[y].append(rand_value)
    
    return array



def generate_Linear_data_points(x_points:int=10,deviation:int=5,linear_line:int=0,abs:bool=False,max_value_cap:bool=False,linear_line_adder:float=1,x_point_adder:float=1) -> list[tuple]:
    """    
    Generates a list with tuples of cordinates that are linearized
    ----
    - xpoints Default = 10
    - Deviation -> How far off you want to randomize your y values from the linearized line Default = 5
    - ypoint_start_value -> where you y point will first start for the linearization Default = 0
    - abs, returns all values of the random y to a positive. If put True
    - max_value_cap -> looks at each y value and make sure that wont go over the highest y value there can be
    - linear_line_adder -> How much you want the y value to increase Default = 1
    - x_point_adder -> How much you want the y value to increase Default = 1
    """
    list_to_return = []    # return a list with tuples inside with values of an x and y
    for i in range(x_points):
        i += x_point_adder
        min_deviation = (linear_line - deviation)
        max_deviation = (linear_line + deviation)        
        y_value = random.uniform(min_deviation,max_deviation)
        if abs == True:
            y_value = np.abs(y_value)
        if max_value_cap == True:
            if y_value > x_points:
                y_value = x_points
        list_to_return.append((i,y_value))
        linear_line += linear_line_adder

    return list_to_return