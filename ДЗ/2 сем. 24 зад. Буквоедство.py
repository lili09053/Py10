st = input()

"""
for i in range(len(st)):
    st = st.strip(st[0])
    st = st.strip(st[len(st)-1])

    #st = st.rstrip(st[len(st) - 1])
    #st = st.lstrip()
    print(st)
"""

while len(st) > 0:
    print(st)
    if len(st) != 1:
        st = st.strip(st[0])
    st = st.strip(st[len(st) - 1])
# print(st)
