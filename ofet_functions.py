import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import scipy

# function to calculate linear mobility given already the region of interest (ROI)
def linear_mobility(L,W,Vd,Ci,vg,id):
  slope, intercept, r_value, p_value, std_error = stats.linregress(vg, id)
  yregress = slope*vg+intercept
  mu_lin= np.format_float_scientific((slope*L)/(W*Vd*Ci),precision = 2)
  return mu_lin,yregress

# function to calculate saturation mobility given already the region of interest
def saturation_mobility(L,W,Ci,vg,id):
    id_sqrt = np.sqrt(id)
    slope, intercept, r_value, p_value, std_error = stats.linregress(vg, id_sqrt)
    mu_sat = np.format_float_scientific((2*L)/(W*Ci)*(slope)**2,precision = 2)
    yregress = slope*vg+intercept
    return mu_sat,yregress

# algorithm to find the best linear region
def linear_roi(vg,id,vd,vt):

  # make a low limit for linear region and cut the data
  low_lim = abs(vt + vd)
  vg_cut = vg[low_lim <= np.absolute(vg)].reset_index(drop = True)
  id_cut = id[low_lim <= np.absolute(vg)].reset_index(drop = True)

  # determine the number of steps to take, this is determined by the width of the region
  vg_range = (vg_cut.max(axis = 0)-vg_cut.min(axis = 0))
  if vg_range > 1:
      sampling_rate = len(vg_cut)/vg_range
      width = (vg_cut.max()-vg_cut.min())/8
      real_width = round(width*sampling_rate)
      steps = round((len(vg_cut)-real_width)/3)

      # for loop that selects the best fit
      score = 0
      best_roi = [0,0]
      for i in range(steps):
        vg_roi = vg_cut[i*3:i*3 + real_width]
        id_roi = id_cut[i*3:i*3 + real_width]
        slope, intercept, r_value, p_value, std_error = stats.linregress(vg_roi, id_roi)
        slope = np.absolute(slope)
        if (r_value**2 > 0.99) and (slope > score):
          score = slope
          best_roi = [vg_cut[i*3],vg_cut[i*3 + real_width]]
  else:
    best_roi = [0,0]
  if best_roi == [0,0]:
      print ('could not find linear region')
  else:
      return best_roi

def find_vt(vg,id):
    return 9


# create figure and subplots
def transfer_curve_plot(vg,id_list,vd,vt,title):
  
  # creat figures
  fig,ax = plt.subplots()
  ax2 = ax.twinx()

  # run a for loop that plots each id in the list, and only calculates mobility for the first one
  if vt == None:
      counter = 1
  else:
      print('somehow vt is nont None anymore')
      counter = 0
  set_linestyle = 'solid'
  for id in id_list:
    
      # plot raw data  
      ax.plot(vg.to_numpy(),id.to_numpy(), color = 'b',linestyle = set_linestyle)
        
      # plot square root data
      sqrt_id = np.sqrt(id.to_numpy())
      ax2.plot(vg.to_numpy(),sqrt_id, color = 'r', linestyle = set_linestyle)

      # change linestyle for other sets of data
      set_linestyle = 'dashed'

      # plot auto linear mobility
      if counter == 0:
          roi = linear_roi(vg,id,vd,vt)
          counter = 1
          if not roi == None:
              roi.sort()
              vg_roi = vg[(roi[0] <= vg) & (vg <= roi[1])]
              id_roi = id[(roi[0] <= vg) & (vg <= roi[1])]
              mu_lin,yregress = linear_mobility(50,1000,vd,11.5e-9,vg_roi,id_roi)
              ax.plot(vg_roi.to_numpy(),yregress.to_numpy(), linewidth = 4,linestyle = 'dashed', color = 'k')
              plt.figtext(0.5,0.15,'linear mobility = ' + mu_lin,fontsize = 12)
              
  # plot formatting
  ax.set_yscale('log')
  ax.set_xlabel('$V_G$', fontsize = 16)
  ax.set_ylabel('$I_d$', color = 'b', fontsize = 16)
  ax2.set_ylabel('${I_d}^{1/2}$', color = 'r',fontsize = 16)
  ax2.ticklabel_format(axis = 'y',style="sci", scilimits=(0,0))
  

  plt.figtext(0.7, 0.2, 'Vds=' + str(vd) + 'V', fontsize=15)
  plt.title(title)
  plt.show()