st=""
print("Enter the paragraph for word counting")
for i in iter(input,""):
    st=st+i+'\n'
print(len(st.split()))