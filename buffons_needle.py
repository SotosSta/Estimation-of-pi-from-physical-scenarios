"""
Tittle: Estimation of pi and Buffon's needle.
Author: Sotirios Stamnas
Date: June 2020

Code that attempts to calculate the value of pi, using the buffons needle 
problem (see https://www.youtube.com/watch?v=sJVivjuMfWA). The code simulates
a big number of needles randomly thrown on a piece of wood that consists of
strips that divide the piece in pieces of equal thickness. By counting how many
of these needle cross the boundary between two regions of the wood, an 
estimation of the value of pi can be made. We run the code multiple times in 
order to calculate a mean value and a simulation error.
"""

import numpy as np


length_of_needle = 1.5 # in cm
length_of_wood = 10 # in cm
N_of_strips = 5  #Choose number of strips
strip_thickness = length_of_wood/N_of_strips #Calculate thickness of each strip


number_of_drops = 10**5 #Has to be relatively large

number_of_simulations = 15 

pi_values = np.zeros(number_of_simulations) #Array to store pi calculations

#Simulation carried out multiple times
for i in range(number_of_simulations):
    

    crosses_counter = 0 #set counter of needles that pass the boundary to zero
    does_not_cross_counter = 0 #set counter of needles that do not pass the boundary to zero
    
    #For loop corresponding to multiple number of drops
    for j in range(number_of_drops):
        
        needle_orientation = np.random.random() #Choose random orientation of needle
        #with respect to the normal betwwen needle and axis parallel to the wood board
        
        needle_com_pos = np.random.random()*length_of_wood #Choose random position
        #for the centre of mass of the needle (We assume the weight of the needle is 
        #uniformly distributed)
  
        # if the random generated number is bigger or equal to 0.5 we choose an orientation
        # so that the needle makes an angle with the right part of the wood board's
        #parallel axis
        if needle_orientation >=0.5:
            angle_deg_right = (np.pi/2)*np.random.random() #generate angle between 0 and pi/2
            
            #find the x position of the needles' lower and upper ends
            needle_upper_end = needle_com_pos + (length_of_needle/2)*np.cos(angle_deg_right)
            needle_lower_end = needle_com_pos - (length_of_needle/2)*np.sin(angle_deg_right)
            
        # if the random generated number is smaller than 0.5 we choose an orientation
        # so that the needle makes an angle with the left part of the wood board's   
        #parallel axis
        else:
            angle_deg_left = (np.pi/2)*np.random.random() #generate angle between 0 and pi/2
            
            #find the x position of the needles' lower and upper ends
            needle_upper_end = needle_com_pos + (length_of_needle/2)*np.sin(angle_deg_left)
            needle_lower_end = needle_com_pos - (length_of_needle/2)*np.cos(angle_deg_left)
            
        #Test condition for needle passing a boundary for each strip
        for k in range(0,N_of_strips+1):
            #Condition for needle passing a boundary is to have its two ends in different regions
            if needle_lower_end< k*strip_thickness <needle_upper_end:    
                crosses_counter +=1 #If condition is met add one to counter
                doesnt_cross = False #If condition is met set doesnt_cross flag to False
                break #If condition is met, break for loop
                
        
            else:
                doesnt_cross = True #If condition is not met set doesnt_cross flag to True
            
            
            if doesnt_cross == True:
                does_not_cross_counter +=1 #if condition is met add one to counter
    
    #Pi values for each simulation    
    pi_values[i] = 2*length_of_needle*number_of_drops/(strip_thickness*crosses_counter)
    
#Find the mean value and standard deviation of the calculated pi values
pi_mean = np.mean(pi_values)
pi_error = np.std(pi_values)

#Print results to 4 significant figures
print(r'$\pi$ is approximately {:.4f} +/- {:.4f}'.format(pi_mean,pi_error))
        
            
        
