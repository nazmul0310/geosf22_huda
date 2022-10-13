import math

class Square:

    def __init__(self, x=0.0, y=0.0, ): # default values of x and y coordinates are 0 
        self.x = x
        self.y = y
        
    def display(self):  # displays the attributes
        print('xCoord of the upper left corner of square= ', self.x)
        print('yCoord of the upper left corner of square= ', self.y)
        print('The length(m) of the arms of the square= ', arm_length)
        print('The angle(degree) of the arm of the square with horizontal line= ', rot_angle)
        
        
    # method calculates the distance from self.x/y to secondPoint.x/y        
    def getCorners(self, arm_length, rot_angle): 
        
        # Equation for finding upper right:
        upper_right_x = (math.cos(math.radians(rot_angle))*arm_length)+self.x
        upper_right_y = (math.sin(math.radians(rot_angle))*arm_length)+self.y
        lower_right_x = (math.sin(math.radians(rot_angle))*arm_length)+upper_right_x
        lower_right_y = (math.cos(math.radians(rot_angle))*arm_length)-upper_right_y
        lower_left_x = self.x-(math.sin(math.radians(rot_angle))*arm_length)
        lower_left_y = self.y-(math.cos(math.radians(rot_angle))*arm_length)
        return([upper_right_x, upper_right_y], [lower_right_x, lower_right_y], [lower_left_x, lower_left_y])

