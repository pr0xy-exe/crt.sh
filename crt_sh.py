import lxml.html
import requests
import sys

domain = sys.argv[1]

url =  "https://crt.sh/?q="+domain
response = requests.get(url, stream=True)
response.raw.decode_content = True
tree = lxml.html.parse(response.raw)
first_column = tree.xpath("(//table)[3]//tr/td[5]/text()")
second_column = tree.xpath("(//table)[3]//tr/td[6]/text()")
subdomains = list(set(first_column + second_column))
final = []
for subdomain in subdomains:
    if domain in subdomain and subdomain!=f'*.{domain}':
    	final.append(subdomain)
for x in final:
	print(x)