from tf import transformations as tr


R=tr.random_rotation_matrix()

R=R[0:3,0:3]

print R

joints=tr.euler_from_matrix(R,'rzyx')

print joints


