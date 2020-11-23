#merge sort implementation for interactiveSorting
import time

def start_mergeSort(data, drawData, speed, size):
    merge_sort(data, 0, len(data)-1, drawData, speed, size)

def merge_sort(data, left, right, drawData, speed, size):
    if left < right: #Stops when the left index meets the right index (only 1 item left)
        #find mid value
        mid = (left+right)//2   #Using // returns an integer

        #call merge_sort to cut each half into half recursively
        merge_sort(data, left, mid, drawData, speed, size)
        merge_sort(data, mid+1, right, drawData, speed, size)
        
        #Merge the left and right side of the array together
        merge(data, left, mid, right, drawData, speed, size)

def merge(data, left, mid, right, drawData, speed, size):
    drawData(data, size, getColorArray(len(data), left, mid, right))
    time.sleep(speed)

    #Grabs the two halves
    leftPart = data[left : mid+1]
    rightPart = data[mid+1 : right+1]

    leftIndex = rightIndex = 0
    
    #dataIndex points to main array
    for dataIndex in range(left, right+1): #For data range
        if leftIndex < len(leftPart) and rightIndex < len(rightPart): #if left or right parts out of range
            if leftPart[leftIndex] <= rightPart[rightIndex]:    #Left < Right then data = left
                data[dataIndex] = leftPart[leftIndex]
                leftIndex += 1
            else:                                               #Right < Left then data = right
                data[dataIndex] = rightPart[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftPart):     #After one of the pointers is OOB finish the non-OOB side
            data[dataIndex] = leftPart[leftIndex]
            leftIndex += 1
        else:                               #^^ but if right side is non-OOB
            data[dataIndex] = rightPart[rightIndex]
            rightIndex += 1
    drawData(data, size, ["navy" if x >= left and x <= right else "gray65" for x in range(len(data))])
    time.sleep(speed)

def getColorArray(length, left, mid, right):
    colorArray = []

    for i in range(length):
        if i>=left and i <=right:
            if i >= left and i <= mid:
                colorArray.append("red")
            else:
                colorArray.append("blue")
        else:
            colorArray.append("gray65")

    return colorArray