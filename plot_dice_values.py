import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.size"] = 42
plt.rcParams["font.family"] = 'Times New Roman'
x_vals = np.arange(4)
scatter_size = 20
    
def plot_dice_values(point_estimate, dice_lb, dice_ub):    
    number_of_classes = point_estimate.shape[1]
    for i in range(number_of_classes): 
        fig, axs = plt.subplots(1, 1, figsize = (15,14))  
        rect = plt.Rectangle((-0.5, 0), 4, 1.2,facecolor=[0,255/255,0], alpha=0.5)
        axs.add_patch(rect)
    
        y_vals = point_estimate[:,i]
        y_errs = [point_estimate[:,i]-dice_lb[:,i],dice_ub[:,i]-point_estimate[:,i]]    
        print(y_vals)
        print(y_errs)
        plt.errorbar(x_vals, y_vals, yerr = y_errs, fmt = 'ok', alpha = 0.8, markersize = scatter_size, elinewidth=4) 
        
        plt.xlim([-0.5, 3.5])    
        plt.ylim([0, 1])
        plt.xticks(ticks = np.arange(4), labels = ['Method 1','Method 2','Method 3a','Method 3b'],rotation = 45)
        plt.ylabel('Final Dice Score Values')
        plt.title('Class '+str(i))
        plt.imshow()