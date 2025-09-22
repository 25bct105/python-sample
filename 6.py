n=int(input("enter the number of the disk"))
def hanoi(n,source,target,auxilliary):
    if n==1:
        print(f"move disk 1 from (source) to (target)")
        return
    hanoi(n-1,source,auxilliary,target)
    print(f"move the disk(n) from (source) to (target)")
    hanoi(n-1,auxilliary,target,source)
hanoi(n,'A','C','B')
