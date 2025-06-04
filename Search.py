inputArr = list(map(int, input("Enter The Numbers : ").split(' ')))
searchElement = int(input("ENTER THE NUMBER TO BE SEARCH :"))
start, end = 0, len(inputArr) - 1
Found = False
while (start <= end):
    mid = (start + end) // 2
    if (inputArr[mid] == searchElement):
        print("Element Found")
        Found = True
        break
    elif (inputArr[mid] < searchElement):
        start = mid + 1
    else:
        end = mid - 1
if not Found:
    print("Element Not Found ")

