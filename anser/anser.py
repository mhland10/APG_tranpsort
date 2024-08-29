"""
ANSER

Author:     Matthew Holland

This module is the Python software that allows for the 

"""

import numpy as np
import scipy.interpolate as sint

###################################################################################################
#
# Functions
#
###################################################################################################

def lawOfTheWallDistribution( ypluss , logCutoff = 11.0 , k = 0.41 , Cplus = 5.0 ):
    """
    This function will return the U+ distribution of the law of the wall for the input y+ array

    Args:

    ypluss [float]:     The matrix of y+ distribution to produce the law of the wall distribution
                            over.

    logCutoff <float>:  The cutoff to switch from log law to direct law for decreasing bounday
                            layer height.

    k <float>:  The von Karman constant.

    Cplus <float>:  The van Driest constant for the log law.

    Returns:

    Upluss [float]:     The matrix of the same shape of "ypluss". That contains the U+ distribution
                            for "ypluss".
    
    """ 

    ypluss_flat = ypluss.flatten()
    Upluss_flat = np.zeros( ypluss_flat.shape )

    for i , ypl in enumerate( ypluss_flat ):
        
        if ypl < logCutoff :
            Upluss_flat[i] = ypl
        else:
            Upluss_flat[i] = ( 1 / k ) * np.log( ypl ) + Cplus

    Upluss = Upluss_flat.reshape( ypluss.shape )

    return Upluss

###################################################################################################
#
# Data Objects
#
###################################################################################################

class boundaryLayer:

    def __init__( self , vonKarmanConst = 0.41 , vanDriestConst = 5.0 , distDomainLims = [ 1e-3 , 1e3 ] , distDomainN = 1e3 ):
        """
        This object is the data object that contains the data and methods to define the boundary
            layer.

        Args:

        **vonKarmanConst <float>:   The von Karman constant that will be used to define the law-of-
                                        the-wall distribution.

                                    The default value is 0.41 for a smooth wall.

        **vanDriestConst <float>:   The constant that define the van Driest profile of the law-of-
                                        the-wall distribution.

                                    The default value is 5.0 for a smooth wall.

        **distDomainLims [float]:   The limits of the tabulated law-of-the-wall distribution's 
                                        domain. 

                                    The default value is [1e-3, 1e3].

        **distDomainN <int>:    The number of points in the tabulated law-of-the-wall
                                    distribution's domain.

                                The default value is 1e3.

        Attributes:

        vonKarmanConst <float>:     The von Karman constant that will be used to define the law-of-
                                        the-wall distribution.

        vanDriestConst <float>:     The constant that define the van Driest profile of the law-of-
                                        the-wall distribution.

        ypluss [float]:     The y+ domain to find the law-of-the-wall over.

        Upluss [float]:     The values of U+ that define the law-of-the wall distribution.
 
        """
    
        self.vonKarmanConst = vonKarmanConst
        self.vanDriestConst = vanDriestConst
    
        self.ypluss = np.logspace( np.log10( np.min( distDomainLims ) ) , np.log10( np.max( distDomainLims ) ) , num = int( distDomainN ) )
        self.Upluss = lawOfTheWallDistribution( self.ypluss , k = self.vonKarmanConst , Cplus = self.vanDriestConst )

    def viscousPropertiesDefine( cls , kineticViscosity , shearVelocity ):
        """
        This method defines the viscous properties for the boundary layer.

        Note: If units other than SI are used, the user should be careful to make sure that the
                units match that of other data.

        Args:
            kineticViscosity <float>:   The kinetic viscosity of the flow for the boundary layer. 
                                            Assumed constant.

            shearVelocity <float>:  The shear velocity for the boundary layer. Assumed constant.

        Attributes:

            kineticViscosity <float>:   The kinetic viscosity of the flow for the boundary layer. 
                                            Assumed constant.

            shearVelocity <float>:  The shear velocity for the boundary layer. Assumed constant.

        """

        cls.kineticViscosity = kineticViscosity
        cls.shearVelocity = shearVelocity

    def boundaryLayerLimitDefine( cls , boundaryLayerHeights , U_inf , threshold = 0.99 , N_sweep = 1e3 , N_points = 1e6 ):
        """
        This method takes the boundary layer heights and the known viscous properties and alters 
            the boundary layer distribution to reflect as such.

        Note: If units other than SI are used, the user should be careful to make sure that the
                units match that of other data.

        Args:
            boundaryLayerHeights [float]:   The list of boundary layer heights to dimensionalize
                                                the boundary layer distribution to. The order will
                                                be:

                                            [Boundary Layer Height , 
                                            Displacement Boundary Layer Height, 
                                            Momentum Boundary Layer Height]

                                            If one of the heights is not given, then leave the 
                                                entry as None. At least two must be float values.

            U_inf <float>:  The freestream velocity at the outside of the boundary layer.

            **threshold <float>:    The threshold for the boundary layer.

                                    The default value is 0.99.

            **N_sweep <int>:    The number of points to sweep along to find the limit of the boundary layer effects.

                                The default value is 1e3.

            **N_points <int>:   The number of points to sweep along to calculate the boundary layer behavior along.

                                The default value is 1e6

        Attributes:

            U_inf <float>:  The freestream velocity at the outside of the boundary layer.

            yplus_inf <float>:  The y+ value where the freestream velocity is according to the law of the wall.

            y_inf <float>:  The height where the freestream velocity is according to the law of the wall.

            yplus_samples [float]:  The samples of the y+ domain to sweep values along.

            y_samples [float]:  The samples of the y domain to sweep values along.

            Uplus_samples [float]:  The U+ values along "yplus_samples" according to the law of the wall.

            U_samples [float]:  The U values that come from the U+ values.

            u_U_samples [float]:    The ratio of velocity to freestream velocity from "U_samples".

            H_sweep [float]:    The array of values for H, which describes the limit of where the
                                    boundary layer is to sweep to find where the limit is based on
                                    known data.

            error_sweep [float]:    The error of the values for H according to the given boundary
                                        layer heights.

            *disp_error_sweep [float]:  The error from the displacement boundary layer calculation.

            *mom_error_sweep [float]:   The error from the momentum boundary layer calculation.

            H_flow <float>: The H value for the boundary layer to minimize the error based on known
                                input values for boundary layer heights.

            Hplus_flow <float>:     The law-of-the-wall transformed value for "H_flow".

        """

        cls.U_inf = U_inf
        cls.yplus_inf = np.exp( ( ( cls.U_inf / cls.shearVelocity ) - cls.vanDriestConst ) * cls.vonKarmanConst )
        cls.y_inf = cls.yplus_inf * ( cls.kineticViscosity / cls.shearVelocity )

        cls.yplus_samples = np.logspace( np.log10( np.min( cls.ypluss ) ) , np.log10( cls.yplus_inf ) , num = int( N_points ) )
        cls.y_samples = cls.yplus_samples * cls.kineticViscosity / cls.shearVelocity
        cls.Uplus_samples = lawOfTheWallDistribution( cls.yplus_samples , k = cls.vonKarmanConst , Cplus = cls.vanDriestConst )
        cls.U_samples = cls.Uplus_samples * cls.shearVelocity
        cls.u_U_samples = cls.U_samples / cls.U_inf
        
        #
        # Generate an array to sweep values of H to find the closest value 
        #
        cls.H_sweep = np.logspace( 2 , np.log10( cls.yplus_inf ) , num = int( N_sweep ) ) * ( cls.kineticViscosity / cls.shearVelocity )
        cls.error_sweep = np.zeros( np.shape( cls.H_sweep ) )
        if boundaryLayerHeights[0]:
            convergence = cls.u_U_samples / threshold - 1
            bl_error_sweep = np.interp( cls.H_sweep , cls.y_samples , convergence )
            cls.error_sweep += bl_error_sweep
        if boundaryLayerHeights[1]:
            delta_disps = np.zeros( np.shape( cls.H_sweep ) )
            for i , h in enumerate( cls.H_sweep ):
                f = ( 1 - cls.u_U_samples )
                delta_disps[i] = np.trapz( f[ cls.y_samples <= h/2 ] , x = cls.y_samples[ cls.y_samples <= h/2 ] )
            convergence = delta_disps / boundaryLayerHeights[1] - 1
            cls.disp_error_sweep = convergence
            cls.error_sweep += cls.disp_error_sweep
        if boundaryLayerHeights[2]:
            theta_disps = np.zeros( np.shape( cls.H_sweep ) )
            for i , h in enumerate( cls.H_sweep ):
                f = cls.u_U_samples * ( 1 - cls.u_U_samples )
                theta_disps[i] = np.trapz( f[ cls.y_samples <= h/2 ] , x = cls.y_samples[ cls.y_samples <= h/2 ] )
            convergence = theta_disps / boundaryLayerHeights[2] - 1
            cls.mom_error_sweep = convergence
            cls.error_sweep += cls.mom_error_sweep
        cls.H_flow = np.interp( 0 , cls.error_sweep , cls.H_sweep )
        cls.Hplus_flow = cls.H_flow * cls.shearVelocity / cls.kineticViscosity

            
        
