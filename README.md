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


Examples:

import generate_data_set as gds

array = gds.generate_NonLinear_array(5,5)
print(array)
  >>
[[0.7975085584935356, 0.5345052947739499, 0.6855090358411668, 0.8264690425792982, 0.9257237789280494], [0.8552313651721865, 0.04569157808334756, 0.48854060086766005, 0.5986109836059869, 0.8062800661751484], [0.5197002744109879, 0.028527282388840614, 0.7866818214873705, 0.29915402685500103, 0.049291271921638846], [0.5837877591902937, 0.45270725416368385, 0.8585333168204223, 0.544356012112294, 0.2668472241164265], [0.6107563407233887, 0.16836977429426092, 0.4845389369852138, 0.8158017492166225, 0.4873308823799307]]



data_points = gds.generate_Linear_data_points()

print(data_points)
  >>
[(1, -2.2143469961988527), (2, 2.1707243600834616), (3, -0.3282474981211232), (4, 4.144847117484683), (5, 4.013444624169473), (6, 5.709601404419416), (7, 2.5811446547894956), (8, 7.177544590988539), (9, 11.741676122470379), (10, 11.959825610269842)]
