The file 'generate_data_set.py'

Contains all methods for generating different types of data.


  Generate Data Sets
  ==================
  
  Provides:
      Various ways of generating linear, or nonlinear data points in either arrays or graphing points
      mostly for training algorithms for testing etc.
      
  
  It is also used to get data whenever needed for graphing purposes etc.
  
  Additional Information ->
  ----------------------
      - Various bools in this file    On = True    False = Off
          - For Example...
              - If there is a bool in a method like from 'generate_Linear_data_points()' It will have 'abs=False'
                if that abs == True, any value that is returned in the dependent value will always be positive.
  
  Methods ->
  =======
      - generate_NonLinear_array (width, height, max_value, min_value, round_on_off, round_value)
          - Generates an array with random values between min and max values
          - You give it a size and it will return you that array with all rand uniform values
          - round_on_off, will round each value if set to True
          - Round_value how many decimal places to round to. Default = 5
          - Finally, return you the array
      
      - generate_Linear_data_points( xpoints, deviation, ypoint_start_value, abs (on or off), max_value_cap ypoint (on or off), linear_line_adder)
          - Generates a list with tuples of coordinates that are linearized
          - xpoints Default = 10
          - Deviation -> How far off you want to randomize your y values from the linearized line Default = 5
          - ypoint_start_value -> where you y point will first start for the linearization Default = 0
          - abs, returns all values of the random y to a positive. If put True
          - max_value_cap -> looks at each y value and makes sure that won't go over the highest y value there can be
          - linear_line_adder -> How much you want the y value to increase Default = 1
          - x_point_adder -> How much you want the y value to increase Default = 1
          
  
  Uses: 
  -----
  numpy, random
    
