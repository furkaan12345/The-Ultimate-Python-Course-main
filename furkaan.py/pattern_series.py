# n= int(input("Enter the number"))
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

def print_right_aligned_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k6 in range(i + 1):
            print("*", end=" ")
        print()




n = int(input("Enter the number: "))
print_right_aligned_triangle(n)
