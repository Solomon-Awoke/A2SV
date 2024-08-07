if __name__ == '__main__':
    m = int(input())
    arr = map(int, input().split())
    sorted_list = sorted(list(set(arr)))
print(sorted_list[-2])
    
            