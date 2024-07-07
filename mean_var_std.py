import numpy as np

lst = input("Enter elements of your list seperated by comma(,)")
b = lst.split(",")

if len(b) < 9 or len(b) > 9:
    print("List must contain nine numbers.")
else:
    c = [int(i) for i in b]
    d = np.array(c)
    # Convert the list into a 3x3 Numpy array
    matrixA = d.reshape(3,3)
    
    
def calculate(matrixA):
    # Calculate the required statistics
    meanA = np.mean(matrixA,axis=0).tolist()
    meanB = np.mean(matrixA,axis=1).tolist()
    meanC = np.mean(matrixA).tolist()
    
    varA = np.var(matrixA,axis=0).tolist()
    varB = np.var(matrixA,axis=1).tolist()
    varC = np.var(matrixA).tolist()
    
    stdA = np.std(matrixA,axis=0).tolist()
    stdB = np.std(matrixA,axis=1).tolist()
    stdC = np.std(matrixA).tolist()
    
    maxA = np.max(matrixA,axis=0).tolist()
    maxB = np.max(matrixA,axis=1).tolist()
    maxC = np.max(matrixA).tolist()
    
    minA = np.min(matrixA,axis=0).tolist()
    minB = np.min(matrixA,axis=1).tolist()
    minC = np.min(matrixA).tolist()
    
    sumA = np.sum(matrixA,axis=0).tolist()
    sumB = np.sum(matrixA,axis=1).tolist()
    sumC = np.sum(matrixA).tolist()
    
    # Prepare the output dictionary
    calculations = {
        'mean': [meanA, meanB, meanC],
        'variance': [varA, varB, varC],
        'standard deviation': [stdA, stdB, stdC],
        'max': [maxA, maxB, maxC],
        'min': [minA, minB, minC],
        'sum': [sumA, sumB, sumC]
    }
    
    return calculations
    
calculate(matrixA)