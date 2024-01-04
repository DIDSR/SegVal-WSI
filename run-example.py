"""
Created on Fri Dec  1 14:56:52 2023

@author: Arian.Arab
@ author email address: arian.arab@fda.hhs.gov
"""

############## Load Confusion Matrices #############
import numpy as np
cm = list(np.load('cm-example.npy', allow_pickle = True))

############## Calculate Final Dice Score Values #############
from calculate_dice_wsi import calculate_dice_wsi
point_estimate = calculate_dice_wsi(cm)

############## Calculate Final Dice Score Values and Confidence Intervals #############
from calculate_dice_bootstrap_cases import calculate_dice_bootstrap_cases
point_estimate,std,lb,ub = calculate_dice_bootstrap_cases(cm, nboots = 2000, confidence_level = 95)

############## Plot Final Dice Score Values and Confidence Intervals #############
from plot_dice_values import plot_dice_values
plot_dice_values(point_estimate, lb, ub)


############## Example ROI with Ground Truth and Prediction Labels #############
example_roi = np.load('mask-pred-example.npy', allow_pickle = True).item(0)
img = example_roi['img']
gt = example_roi['gt']
pred = example_roi['prediction']
del example_roi

import matplotlib.pyplot as plt
plt.imshow(img)
plt.imshow(gt)
plt.imshow(pred)
plt.plot()

from calculate_cm import calculate_cm
cm_roi = calculate_cm(gt, pred, number_of_classes=3)
