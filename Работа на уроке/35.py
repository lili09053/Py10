# задача  должна быть записана в одну строку!!!
for elem in (input().split()):
    print("*" * int(elem))
# ---------------------------------------------
print("\n".join(["*" * int(elem) for elem in (input().split())]))
