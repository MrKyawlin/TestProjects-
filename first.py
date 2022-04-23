# f=open(r'G:\KKiei\myfile.txt','w',-1,'UTF-8')
# f.write("ကျော်လင်းထွန်း")
# f.close()
f=open(r'G:\KKiei\myfile.txt','r',-1,'UTF-8')
for line in f:
    print(line)
f.close()