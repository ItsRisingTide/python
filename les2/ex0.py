class my_list(list):
    def __add__(a, b):
        data =[]
        len_a=len(a)
        len_b=len(b)
        
        diff = min(len_a,len_b)
        length = max(len_a,len_b)
        for i in range(length):
            if i >= diff:
                if len_a < len_b:
                    data.append(0 + b[i])
                elif len_a > len_b:
                    data.append(a[i] + 0)
            else:
                data.append(a[i] + b[i])
        return data;

    def __sub__(a,b):
        negative_b=[]
        len_b = len(b)
        for i in range(len_b):
            negative_b.append(b[i]*(-1))
        return my_list.__add__(a,negative_b)

    def __gt__(a,b):
        if (sum(a) > sum(b)):
            return True
        else:
            return False

    def __ge__(a,b):
        if (sum(a) >= sum(b)):
            return True
        else:
            return False

    def __lt__(a,b):
        if (sum(a) < sum(b)):
            return True
        else:
            return False

    def __le__(a,b):
        if (sum(a) <= sum(b)):
            return True
        else:
            return False

lst1 = my_list([1,2])
lst2 = my_list([1,4])
lst3 = my_list([1,3,4])

print(f"{lst1} + {lst2} --> {lst1 + lst2}")
print(f"lst1 : {lst1}    lst2 : {lst2}\n")

print(f"{lst1} + {lst3} --> {lst1 + lst3}")
print(f"lst1 : {lst1}    lst2 : {lst3}\n")

print(f"{lst3} + {lst2} --> {lst3 + lst2}")
print(f"lst1 : {lst3}    lst2 : {lst2}\n\n")


print(f"{lst1} - {lst2} --> {lst1 - lst2}")
print(f"lst1 : {lst1}    lst2 : {lst2}\n")

print(f"{lst1} - {lst3} --> {lst1 - lst3}")
print(f"lst1 : {lst1}    lst2 : {lst3}\n")

print(f"{lst3} - {lst2} --> {lst3 - lst2}")
print(f"lst1 : {lst3}    lst2 : {lst2}\n")


print(f"{lst1} > {lst2} --> {lst1 > lst2}")
print(f"{lst3} >= {lst2} --> {lst3 >= lst2}")
print(f"{lst1} < {lst2} --> {lst1 < lst2}")
print(f"{lst3} <= {lst2} --> {lst3 <= lst2}")
