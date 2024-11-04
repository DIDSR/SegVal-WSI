from tqdm import tqdm
import numpy as np
from calculate_dice_wsi import calculate_dice_wsi

def pick_bootstrap_sample(data,rng):
    idx = rng.randint(0, len(data), len(data))
    data_random = [data[n] for n in idx]
    return data_random

def find_mean_std_lb_ub(dice_boots, confidence_level):
    delta = (100-confidence_level)/2
    mean_vals = np.round(np.mean(dice_boots, axis = 0),4)
    std_vals =  np.round(np.std(dice_boots, axis = 0),4)
    lb_vals = np.round(np.percentile(dice_boots,delta, axis = 0),4)
    ub_vals = np.round(np.percentile(dice_boots,100-delta, axis = 0),4)        
    return mean_vals, std_vals, lb_vals, ub_vals

def calculate_dice_bootstrap_cases(cm,nboots = 2000,confidence_level = 95):
    dice_boots = []
    seed = 0
    rng = np.random.RandomState(seed)
    for k in tqdm(range(nboots), desc = 'Boostrapping Samples'):
        cm_boot = pick_bootstrap_sample(cm,rng)
        dice_boots.append(calculate_dice_wsi(cm_boot))    
    _, dice_boots_std, dice_boots_lb, dice_boots_ub = find_mean_std_lb_ub(dice_boots, confidence_level)
    dice_boots_point_estimate = calculate_dice_wsi(cm)
    return dice_boots_point_estimate, dice_boots_std, dice_boots_lb, dice_boots_ub