#Rewrite this code to be more concise by replacing the mean function with a lambda
# expression defined within the call to map().
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

mean = lambda num: sum(num)/len(num)

averages = list(map(mean, numbers))
print(averages)