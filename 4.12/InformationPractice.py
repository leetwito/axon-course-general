import urllib2 as ul



data = ul.urlopen('https://www.gutenberg.org/files/1934/1934-0.txt').read()
s1 = open('code_sample1.py').read()
s2 = open('code_sample2.py').read()

print s1

{c:1.0*s1.count(c)/len(s1) for c in set(s1+s2)}
