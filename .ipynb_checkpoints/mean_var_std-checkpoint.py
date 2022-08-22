import numpy as np

def calcul(valeurs, function):
    axis1 = []
    axis2 = []
    for i in range(len(valeurs)):
        x = [valeurs[0][i], valeurs[1][i], valeurs[2][i]]
        axis1.append(function(x))
        
    for i in range(len(valeurs)):
        y = valeurs[i]
        axis2.append(function(y))
    return [axis1, axis2, function(valeurs)]


def calculate(list):
    try:
        list_shaped = np.array(list).reshape((3, 3))
        calculations = {}
        calculations["mean"] = calcul(list_shaped, np.mean)
        calculations["variance"] = calcul(list_shaped, np.var)
        calculations["standard deviation"] = calcul(list_shaped, np.std)
        calculations["max"] = calcul(list_shaped, np.max)
        calculations["min"] = calcul(list_shaped, np.min)
        calculations["sum"] = calcul(list_shaped, np.sum)
        return calculations
    except:raise ValueError("List must contain nine numbers.")
    