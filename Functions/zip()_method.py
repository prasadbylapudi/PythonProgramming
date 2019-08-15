num=[1,2,3,4,5]
names=['munna','chatrapati','rebel','saaho','mirchi'];
#no iterables are passed
result=zip();
print(result);

#onverting iterator to list
resultlist=list(result);
print(resultlist);

#two iterables are passed
result=zip(num,names);


#converting iterator to set
resultset=set(result);
print(resultset)
