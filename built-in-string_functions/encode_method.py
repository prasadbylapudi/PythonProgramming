#A simple method which encode unicode string to utf-8 encoding standard.
str1="prasadbylapudi";
encode=str1.encode();
str2="PRASADBYLAPUDI";
encode2=str2.encode("ascii");
print(encode);
print(encode2);
