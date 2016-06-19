from Bio import Entrez
from xml.dom.minidom import parseString
import re
Entrez.email = "brendan.lawlor@gmail.com"     # Always tell NCBI who you are
handle = Entrez.esearch(db="pubmed", term="1800562")
record = Entrez.read(handle)
handle.close()
print record
# http://www.ncbi.nlm.nih.gov/sites/entrez?Db=pubmed&DbFrom=snp&Cmd=Link&LinkName=snp_pubmed_cited&LinkReadableName=Pubmed%20(SNP%20Cited)&IdsFromResult=1800562
# c282y_records = ['115372583', '111535158', '111033563', '58044250', '28934888', '28934597', '17530654', '4134660', '1800730', '1800562']
#
# print c282y_records
# "Pubmed (SNP Cited) for SNP (Select 1800562)"
#
# # for id in c282y_records:
# handle = Entrez.efetch(db="snp", id="1800730")#, rettype='flt', retmode='xml')
# res = handle.read()
# handle.close()
# print res
# result = Entrez.read(handle)
# result = parseString(handle.read())
# handle.close()
# nodes = result.getElementsByTagName('hgvs')
# for node in nodes:
#     if 'NP_' in node.firstChild.nodeValue:
#         flag = 1
#         val = node.firstChild.nodeValue
#         regex1 = r'[A-Z][a-z]+'
#         regex2 = r'[0-9]+'
#         aa = re.findall(regex1, val)
#         pos = re.findall(regex2, val)
#         print aa[0] + " > " + aa[1] + " Position: " + pos[2]
# if flag == 0:
#     print "SNP not in coding region"