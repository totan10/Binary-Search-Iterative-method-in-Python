def BinarySearch(l,x):
  low=0
  high=len(l)-1
  while low<=high:
    mid=(low+high)//2
    if l[mid]==x:
      return mid
    elif l[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return -1

n=int(input("Enter the number of elements: "))
l=list(map(int,input("\nEnter the numbers of the sorted list : ").strip().split()))[:n]
x=int(input("Enter the number to search: "))
result=BinarySearch(l,x)
if result != -1:
    print(f"{x} is present in the list at index {result}")
else:
    print(f"{x} is not present in the list")