'''
  HW3 Q4 data
  by David Conner CPSC 472/PCSE 572
  Spring 2025
'''

import numpy as np

#Homework Hw3.4
# Feel free to import rotations and use those methods if you want

#RESULTS: for pelvis to r_palm
#Chain is: r_palm -> r_hand -> r_arm_wrist_roll -> r_arm_wrist_yaw -> r_arm_elbow -> r_arm_shoulder_yaw -> r_arm_shoulder_roll -> r_arm_shoulder_pitch -> utorso -> waist -> pelvis
# plm-hnd-wr-wy-el-shy-shr-shp-tor-wst-pel
t_pel_wst = np.array([0.000, 0.000, 0.137])  # waist frame in pelvis frame (^p T_w)
q_pel_wst = np.array([1.000, 0.000, 0.000, -0.000]) # [w, (x,y,z)] form

t_wst_tor = np.array([0.000, 0.000, 0.000])
q_wst_tor= np.array([1.000, 0.000, 0.003, 0.000])# [w, (x,y,z)] form

t_tor_shp = np.array([0.000, -0.234, 0.165])
q_tor_shp = np.array([0.851, 0.000, -0.525, 0.000]) # [w, (x,y,z)] form

t_shp_shr = np.array([0.000, 0.000, 0.000])
q_shp_shr = np.array([0.960, -0.279, 0.000, 0.000])# [w, (x,y,z)] form

t_shr_shy = np.array([0.000, 0.000, 0.000])
q_shr_shy = np.array([0.842, 0.000, 0.000, 0.540])# [w, (x,y,z)] form

t_shy_el = np.array([0.030, 0.000, -0.246])
q_shy_el = np.array([0.863, 0.000, -0.506, 0.000])# [w, (x,y,z)] form

t_el_wy = np.array([-0.030, 0.000, -0.186])
q_el_wy = np.array([0.566, 0.000, 0.000, 0.824])# [w, (x,y,z)] form

t_wy_wr = np.array([0.000, 0.000, 0.000])
q_wy_wr = np.array([0.904, -0.428, 0.000, 0.000])# [w, (x,y,z)] form

t_wr_hnd = np.array([0.000, 0.000, 0.000])  # hand in wrist frame
q_wr_hnd = np.array([0.797, 0.000, 0.000, -0.605])# [w, (x,y,z)] form

t_hnd_plm = np.array([0.000, 0.000, -0.160])  # palm in hand frame
q_hnd_plm = np.array([0.000, 0.707, 0.707, 0.000])# [w, (x,y,z)] form
