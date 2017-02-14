# bug 4
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2017/01/24/04_Debugging_1/#activity-fix-as-many-bugs-as-possible

# Define the sinc-function sinc(x) = \sin(x)/x:
import numpy as np

def sinc(x):
   return np.sin(x)/x

print(sinc(3.145))

