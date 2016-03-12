from tf import transformations as tr
import numpy as np





R=np.array([[-0.7288132,  -0.27346933,  0.62773071, 0],
 [ 0.57236671,  0.25984954,  0.77773682, 0],
 [-0.37580271,  0.92611702, -0.03285703, 0],
 [0,  0, 0, 1]]
 )



print R

q=tr.quaternion_from_matrix(R)

print q

joints=tr.euler_from_matrix(R,'rzxy')

print joints





