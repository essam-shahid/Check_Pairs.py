def chkPair(arr, sum):

    lth=len(arr)
    count=-0

    for i in range(lth):
        for j in arr[i+1:]:
            if (arr[i]+j==sum):
                count=+1
                x=("Pair with a given sum ", sum, " is (", arr[i], ", ", arr[j], ")")
                return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr=[0, -1, 2, -3, 1]
	print("Check Pair Running!")
	print("Great!!")
    sum = -2
    print(chkPair(arr, sum))

    if (chkPair(arr,sum)):
        print("Valid pair exists")

    else:
        print("No valid pair exists for ", sum)
