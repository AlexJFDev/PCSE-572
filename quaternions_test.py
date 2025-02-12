'''
Rotation demo with matrices and quaternions
  by David Conner CPSC 472/PCSE 572 Spring 2024
  uses Python 3 printing

  Modified version of rotations_test focusing on quaternions
'''

import numpy as np

from rotations import *

# Demo rotation conversions with matrices and quaternions
alpha = np.pi/4.0
beta  = np.pi/6.0;
theta = np.pi/3.0;
Rx = rotX(alpha);
Ry = rotY(beta);
Rz = rotZ(theta);

# NOTE: We must use np.dot to do matrix multiplication
# Simple multiplication using Rx*Ry does element by element,
# and NOT linear algebra matrix multiplication.
# In Python 3 you can also use np.matmul or @ operator
#  for linear algebra style matrix multiplication

# These three notations are equivalent
R= np.dot(Rx,np.dot(Ry,Rz)) # Rx*Ry*Rz = Rx*(Ry*Rz)
R1 = np.matmul(Rx, np.matmul(Ry, Rz))
R2 = Rx@Ry@Rz

print("Rx(",alpha,") =\n",Rx)
print("Ry(",beta, ") =\n",Ry)
print("Rz(",theta,") =\n",Rz)
print("R = Rx*Ry*Rz = \n",R)
print("R1 =\n",R1)
print("R2 =\n",R2)

print("Vector to rotate:")
v = np.array([1.,1.,1.])
vn = v/np.sqrt(np.dot(v,v))

print(" vn=",vn)

vr = np.dot(R,vn)
print(" R*vn=",vr)


print("\n\nDemo for quaternions")
q = M2Q(R)  # convert rotation matrix to quaternion
rot = Q2M(q)  # convert back (better be the same modulo some numeric noise)
print("q=", q)
print("rot(q)=",rot)
print("R.T@rot=", NoDust(R.T@rot))  # if Q2M was good, then better be identity

# Now do each rotation about single axis
qx = M2Q(Rx)
qy = M2Q(Ry)
qz = M2Q(Rz)
qq = Q1xQ2(qx, Q1xQ2(qy,qz))  # quaternion multiplication is associative

print("Conversion to quat:")
print("q=",q)
print("q=qx.qy.qz=",qq)
print("qx =",qx)
print("qy =",qy)
print("qz =",qz)


print("quat inverse ")
qi = ConjQ(q)  # for normalized quaternion, q^(-1) is q*
print("q*=", qi)
print(" inverse test:")
print("qi.q = q.qi = ", Q1xQ2(qi,q), "=", Q1xQ2(q, qi))

print("\n\nPure vector quaternion form")
qv = np.array([0.0, vn[0], vn[1], vn[2]])
print("qv=",qv)

print("Rotation by quaternions")
print(" quaternion conjugate:")
print(" qc = ",ConjQ(q))

qr = Q1xQ2(q,Q1xQ2(qv,ConjQ(q)))
print(" qr = ",NoDust(qr), " from matrix conversion")
qqr = Q1xQ2(qq,Q1xQ2(qv,ConjQ(qq)))
print(" qr = ",NoDust(qqr), " from composition quaternion")
