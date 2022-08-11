import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sici
from scipy import signal


def grad(arr, d_arr):
    gradf = np.zeros(d_arr.shape)
    for l in range(len(d_arr)):
        if l==0:
            ax_ind = 1
        elif l==1:
            ax_ind = 0
        elif l==2:
            ax_ind = 2
        vec = (arr - np.roll(arr, 1, ax_ind))/(d_arr[l] - np.roll(d_arr[l], 1, ax_ind))
        gradf[l] = vec
    return gradf

def diverg(arr, dq):
    div_array = np.zeros(arr[0].shape)
    i = 0
    for x_i in arr:
        i += 1
        if i==1:
            ax_ind = 1
        elif i==2:
            ax_ind = 0
        elif i==3:
            ax_ind = 2
        dxi = dq[i-1] - np.roll(dq[i-1], 1, ax_ind)
        div_array += (x_i - np.roll(x_i, 1, ax_ind))/(dxi)
    return div_array

def curl_f(arr, dp):
    x_curl = np.zeros(arr[0].shape)
    y_curl = np.zeros(arr[1].shape)
    z_curl = np.zeros(arr[2].shape)
    for j in range(len(arr)):
        if j==0:
            dx_i = dp[j+1] - np.roll(dp[j+1], 1, 0)
            dx_j = dp[j+2] - np.roll(dp[j+2], 1, 2)
            x_curl += (arr[j+2]-np.roll(arr[j+2],1,0))/dx_i - (arr[j+1]-np.roll(arr[j+1],1,2))/dx_j
        elif j==1:
            dx_i = dp[j+1] - np.roll(dp[j+1], 1, 2)
            dx_j = dp[j-1] - np.roll(dp[j-1], 1, 1)
            y_curl += (arr[j-1]-np.roll(arr[j-1],1,2))/dx_i - (arr[j+1]-np.roll(arr[j+1],1,1))/dx_j
        elif j==2:
            dx_i = dp[j-2] - np.roll(dp[j-2], 1, 1)
            dx_j = dp[j-1] - np.roll(dp[j-1], 1, 0)
            z_curl += (arr[j-1]-np.roll(arr[j-1],1,1))/dx_i - (arr[j-2]-np.roll(arr[j-2],1,0))/dx_j
    return x_curl, y_curl, z_curl, np.array([x_curl, y_curl, z_curl])



