f = open("ascii.html",'w')
#message = '<html><head></head><body><p>Hello,World!</p><p>demo</p></body></html>'
begin='<html><body><table>'
middle=''
for i in range(66):
	middle+="<tr><td>"+str(i)+"</td><td>"+chr(i)+"</td></tr>"

end='</table></body></html>'
#print(begin+middle+end)
f.write(begin+middle+end)
f.close()