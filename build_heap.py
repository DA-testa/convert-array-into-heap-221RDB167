# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    swaps=[]
    for i in range (n // 2, -1,-1):
        heap(data,swaps,i,n)

    return swaps

def heap(data, swaps, i, n):
    min_i = i
    left = 2*i+1
    right = 2*i+2
    
    if left < n and data[left] < data[min_i]:
        min_i =  left
        
    if right < n and data[right] < data[min_i]:
        min_i = right
        
    if i != min_i:
        swaps.append((i,min_i))
        data[i], data[min_i] = data[min_i], data[i]
        heap(data,swaps,min_i,n)
def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_t = input().strip()
    if input_t == "I":
        # input from keyboard
        n=int(input())
        data = list(map(int,input().split()))
        
    elif input_t == "F":
        test_nr = input().strip()
        with open(f"tests/{test_nr}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
