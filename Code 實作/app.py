def filtered_squares(amounts, threshold):
    result=[]
    for value in amounts:
        if value>0:
            squre= value*value
            if squre > threshold:
                result.append(squre)
    return result

amounts = [1, -2, 0, 3, 5, -4, 4]
threshold = 10
result=filtered_squares(amounts,threshold)
print(result)