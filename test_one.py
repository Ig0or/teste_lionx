""" 
Write a function that takes as arguments: an array of distinct integers and an integer (target value). 
You need to check if any two numbers of the array sum up to the target value. 
If that's the case, your function should return those two numbers in array fashion. Otherwise, just return an empty array.
"""


def two_sum(array, target):
    for num in array:
        for num2 in array:
            if num + num2 == target and array.index(num) != array.index(num2):
                return [num, num2]
    else:
        return []


if __name__=="__main__":
    array_one = [3, 5, -4, 8, 11, 1, -1, 6]
    array_two = [5, 1, 8, 3, 7, 9, 10, 20, 11]
    array_three = [1, 5, 2, 6, 2, 11]
    target = 10

    print(two_sum(array_one,target))
    print(two_sum(array_two, target))
    print(two_sum(array_three, target))