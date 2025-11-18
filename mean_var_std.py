import numpy as np


def calculate(arr):
    
    def function(matrix, func, a=0):
        if func == 'mean':
            return np.mean(matrix, axis=a)
        elif func == 'variance':
            return np.var(matrix, axis=a)
        elif func == 'standard deviation':
            return np.std(matrix, axis=a)
        elif func == 'max':
            return np.max(matrix, axis=a)
        elif func == 'min':
            return np.min(matrix, axis=a)
        elif func == 'sum':
            return np.sum(matrix, axis=a)

    try:
        x = np.array(arr)
        x = x.reshape((3, 3))
    except ValueError:
        raise ValueError('List must contain nine numbers.')

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    for k in calculations.keys():
        for i in range(3):
            if i in [0, 1]:
                calculations[k].append(function(x, k, i).tolist())
            else:
                if k in ['mean', 'variance', 'standard deviation']:
                    calculations[k].append(float(function(x.flatten(), k)))
                else:
                    calculations[k].append(int(function(x.flatten(), k)))

    return calculations

