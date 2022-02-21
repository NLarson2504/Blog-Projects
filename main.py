import random
from Tkinter import *

# This the graph ting fam
listy5 = [1, 2, 3, 4, 5]
listy10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listy100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
random.shuffle(listy5)
random.shuffle(listy10)
random.shuffle(listy100)
global mergeCount
# bogoSort AKA SHOTGUN SORT
def bogoSort(listy):
    count = 0
    while listy != sorted(listy):
        random.shuffle(listy)
        count = count + 1
    print("Bogo sort: " + str(count) + " moves.")

# selectionSort algorithm
def selectionSort(listy):
    count = 0
    for i in range(len(listy)):
        min_idx = i
        for j in range(i+1, len(listy)):
            if listy[min_idx] > listy[j]:
                min_idx = j
                count += 1
        listy[i], listy[min_idx] = listy[min_idx], listy[i]
    print("Selection Sort: " + str(count) + " moves.")

# bubbleSort algorithm
def bubbleSort(listy):
    count = 0
    n = len(listy)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if listy[j] > listy[j+1]:
                listy[j], listy[j+1] = listy[j + 1], listy[j]
                count += 1

    print("Bubble Sort: " + str(count) + " moves.")

# mergeSort algorithm; I can't print out the # of moves because it is a recursive algorithm
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        counter1 = 0
        counter2 = 0
        counter3 = 0
        while counter1 < len(left) and counter2 < len(right):
            if left[counter1] < right[counter2]:
                arr[counter3] = left[counter1]
                counter1 += 1
            else:
                arr[counter3] = right[counter2]
                counter2 += 1
            counter3 += 1
        while counter1 < len(left):
            arr[counter3] = left[counter1]
            counter1 += 1
            counter3 += 1
        while counter2 < len(right):
            arr[counter3] = right[counter2]
            counter2 += 1
            counter3 += 1

if __name__ == "__main__":
    on = True
    while(on):
        random.shuffle(listy5)
        random.shuffle(listy10)
        random.shuffle(listy100)
        userIn = raw_input("Choose sorting method: (merge, selection, bubble, bogo): ")
        if "merge" in userIn.lower():
            mergeSort(listy5)
            print("Recursive algorithm no likey counters but it worked")
            if "no" in raw_input("Continue?: (yes/no)"):
                on = False
        if "selection" in userIn.lower():
            selectionSort(listy5)
            if "no" in raw_input("Continue?: (yes/no)"):
                on = False
        if "bubble" in userIn.lower():
            bubbleSort(listy5)
            if "no" in raw_input("Continue?: (yes/no)"):
                on = False
        if "bogo" in userIn.lower():
            bogoSort(listy5)
            if "no" in raw_input("Continue?: (yes/no)"):
                on = False
