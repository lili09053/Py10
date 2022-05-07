n = int(input())
lst = []
for i in range(n):
    st = input()
    if st.startswith('####'):
        continue
    elif st.startswith('%%'):
        lst.append(st.lstrip('%%'))
        #print(st.lstrip('%%'), end="\n")
    else:
        lst.append(st)
        #print(st, end='\n')
for elem in lst:
    print(elem)