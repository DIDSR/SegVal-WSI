import numpy as np
from calculate_dice import calculate_dice

def merge_all_cms(cm):
    cm_all = [j for i in cm for j in i]
    return cm_all

def merge_all_cms_wsi(cm):
    cm_all = [np.sum(i,axis = 0) for i in cm]
    return cm_all

def calculate_dice_inside(cm, class_index):    
    all_cm = merge_all_cms(cm)     
    all_cm_wsi = merge_all_cms_wsi(cm)  
    
    #first method
    cm_aggregated = np.sum(all_cm, axis = 0)   
    dice_1 = np.round(calculate_dice(cm_aggregated, class_index),4)
    
    #second method
    dice_vals = [calculate_dice(i, class_index) for i in all_cm]  
    dice_vals = [i for i in dice_vals if not np.isnan(i)] 
    dice_2 = np.round(np.mean(dice_vals),4)
    
    #third method a         
    dice_vals = [calculate_dice(i, class_index) for i in all_cm_wsi]
    dice_vals = [i for i in dice_vals if not np.isnan(i)] 
    dice_3_a = np.round(np.mean(dice_vals),4)
    
    #third method b
    dice_vals = [[calculate_dice(j, class_index) for j in i] for i in cm]    
    dice_vals = [[j for j in i if not np.isnan(j)] for i in dice_vals]    
    dice_vals = [i for i in dice_vals if i != []]
    dice_vals = [np.mean(i) for i in dice_vals]
    dice_3_b = np.round(np.mean(dice_vals),4)
    return np.array([dice_1, dice_2, dice_3_a, dice_3_b])

def calculate_dice_wsi(cm):
    number_of_classes = cm[0][0].shape[0]
    dice_vals = np.zeros((4,number_of_classes))
    for i in range(number_of_classes):
        dice_vals[:,i] =  calculate_dice_inside(cm, class_index = i)
    return dice_vals