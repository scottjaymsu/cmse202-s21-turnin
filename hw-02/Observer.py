from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.wcs import WCS

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self, im1_filename, im2_filename):
        '''
        This function loads the image data and stores them as dictionaries as attributes 
        '''
        hdu1 = fits.open(self.im1_filename)[0] 
        hdu2 = fits.open(self.im2_filename)[0]
        self.im1_data = hdu1.data
        self.im2_data = hdu2.data
        
    def calc_stats(self):
        '''
        This function prints the mean and standard deviation for both images
        '''
        print('The mean of the red image is', self.im1_data.mean(), 'and the standard deviation is ', self.im1_data.std())
        print('The mean of ir image is', self.im2_data.mean(), 'and the standard deviation is ', self.im2_data.std())
    
    def make_composite(self):
        '''
        This function creates a 3D numpy array that represents a 2D image and its corresponding RGB values
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        # Compute the green channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,1] = ((self.im1_data.astype("float")+self.im2_data.astype("float"))/2)/norm_factor
        rgb[:,:,1][rgb[:,:,0] > 1.0] = 1.0
        
        # Compute the blue channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,2] = (self.im1_data.astype("float")/norm_factor)
        rgb[:,:,2][rgb[:,:,0] > 1.0] = 1.0
        
        plt.imshow(rgb)