from Bio import Entrez
import xml.etree.ElementTree as ET
import re

from pprint import pprint as pp
# from xml.dom.minidom import parseString
# import re
Entrez.email = "brendan.lawlor@gmail.com"     # Always tell NCBI who you are
# handle = Entrez.esearch(db="snp", term="HFE[Gene], c282y")
# record = Entrez.read(handle)
# print('Number of results: ' + record['Count'])
# c282y_records = record['IdList']
# handle.close()

# In order to avoid calling Entrez over and over, this is the list of records returned.
c282y_records = ['115372583', '111535158', '111033563', '58044250', '28934888', '28934597', '17530654', '4134660', '1800730', '1800562']

# Attempt 1
# for id in c282y_records:
#     handle = Entrez.efetch(db="snp", id=id)#, rettype='flt', retmode='xml')
#     # This handle.read function returns a kind of pseudo-json which can't be easily parsed.
#     res = handle.read()
#     handle.close();
#     print res

# Attempt 2 - use the xml output and parse it independently of BioPython (which doesn't like namespaces)
# An alternative would be to string the namespace from the xml, save it into a tmp file,
# reload and parse using Entrez.parse


def findMergedRecordIds(rs):
    merges = set()
    for child in rs:
        if child.tag == 'MergeHistory':
            print 'Merge found'
            merges.add('rs' + child.attrib['rsId'])
    return merges

mutations = set()
merges = set()
for id in c282y_records:
    print id
    handle = Entrez.efetch(db="snp", id=id, rettype='flt', retmode='xml')
    # This handle.read function returns a kind of pseudo-json which can't be easily parsed.
    res = handle.read()
    handle.close();
    # Strip namespace for easier reading.
    res = re.sub(' xmlns="[^"]+"', '', res, count=1)
    exchangeSet = ET.fromstring(res)
    # Find all the HGVS entries that mention the c.845G>A mutation
    has_mutation = False
    for rs in exchangeSet:
        for child in rs:
            if child.tag == "hgvs":
                if 'c.845G>A' in child.text:
                    mutations.add('rs'+id)
                    mergedRecordIds = findMergedRecordIds(rs)
                    if len(mergedRecordIds) > 0:
                        print 'Adding', mergedRecordIds, 'to merges'
                        merges = merges.union(mergedRecordIds)

mutations = mutations.difference(merges)
print 'Merges:', merges
print 'Mutations:', mutations



# This manages to get an XML string but BioPython cannot handle the fact that it uses namespaces
# So we have to consider parsing it using another library.



# Back to two problems: The hgvs data in the returned xml does not include the links that the UI search provides
    # I can't search by HGVS names even in the UI

    # nodes = result.getElementsByTagName('hgvs')
    # if nodes == None or len(nodes) == 0:
    #     print ('No HGVS records returned')
    # for node in nodes:
    #     if 'NP_' in node.firstChild.nodeValue:
    #         flag = 1
    #         val = node.firstChild.nodeValue
    #         regex1 = r'[A-Z][a-z]+'
    #         regex2 = r'[0-9]+'
    #         aa = re.findall(regex1, val)
    #         pos = re.findall(regex2, val)
    #         print aa[0] + " > " + aa[1] + " Position: " + pos[2]
    #         if flag == 0:
    #             print "SNP not in coding region"

def pull_line(var_set,line):
    """
    This function parses data from lines in one of three ways:

    1.) Pulls variables out of a particular line when defined as "variablename=[value]" - uses a string to find the variable.
    2.) Pulls variables based on a set position within a line [splits the line by '|']
    3.) Defines variables that can be identified based on a limited possible set of values - [categorical variable, specified using an array]

    """
    line_set = {}
    for k,v in var_set.items():
        if type(v) == str:
            try:
                line_set[k] = [x for x in line if x.startswith(v)][0].replace(v,'')
            except:
                pass
        elif type(v) == int:
            try:
                line_set[k] = line[v]
            except:
                pass
        else:
            try:
                line_set[k] = [x for x in line if x in v][0]
            except:
                pass
    return line_set

def pull_vars(var_set,line_start,line,multi=False):
    """
    Delegates and compiles data from entrez flat files dependent on whether
    the type of data trying to be pulled is contained in unique vs. non-unique lines.
    For example - the first line of the flat file is always something like this:

    rs12009 | Homo Sapiens | 9606 | etc.

    This line is unique (refers to RefSnp identifier)- and only occurs once in each flat file. On the other hand, lines
    beginning with "ss[number]" refer to 'submitted snp' numbers and can appear multiple times.

    """
    lineset = [x.split(' | ') for x in line if x.startswith(line_start)]
    if len(lineset) == 0:
        return
    # If the same line exists multiple times - place results into an array
    if multi == True:
        pulled_vars = []
        for line in lineset:
            # Pull date in from line and append
            pulled_vars.append(pull_line(var_set,line))
        return pulled_vars
    else:
    # Else if the line is always unique, output single dictionary
        line = lineset[0]
        pulled_vars = {}
        return pull_line(var_set,line)

def get_snp(q):
    """
    Takes as input an array of snp identifiers and returns
    a parsed dictionary of their data from Entrez.
    """
    response = Entrez.efetch(db='SNP', id=','.join(q), rettype='flt', retmode='flt').read()
    print response
    r = {} # Return dictionary variable
    # Parse flat file response
    for snp_info in filter(None,response.split('\n\n')):
        # print snp_info
        # Parse the First Line. Details of rs flat files available here:
        # ftp://ftp.ncbi.nlm.nih.gov/snp/specs/00readme.txt
        snp = snp_info.split('\n')
        # Parse the 'rs' line:
        rsId = snp[0].split(" | ")[0]
        r[rsId] = {}

        # rs vars
        rs_vars = {"organism":1,
                   "taxId":2,
                   "snpClass":3,
                   "genotype":"genotype=",
                   "rsLinkout":"submitterlink=",
                   "date":"updated "}

        # rs vars
        ss_vars = {"ssId":0,
                   "handle":1,
                   "locSnpId":2,
                   "orient":"orient=",
                   "exemplar":"ss_pick=",
                   }

        # SNP line variables:
        SNP_vars = {"observed":"alleles=",
                    "value":"het=",
                    "stdError":"se(het)=",
                    "validated":"validated=",
                    "validProbMin":"min_prob=",
                    "validProbMax":"max_prob=",
                    "validation":"suspect=",
                    "AlleleOrigin":['unknown',
                                    'germline',
                                    'somatic',
                                    'inherited',
                                    'paternal',
                                    'maternal',
                                    'de-novo',
                                    'bipaternal',
                                    'unipaternal',
                                    'not-tested',
                                    'tested-inconclusive'],
                    "snpType":['notwithdrawn',
                               'artifact',
                               'gene-duplication',
                               'duplicate-submission',
                               'notspecified',
                               'ambiguous-location;',
                               'low-map-quality']}

        # CLINSIG line variables:
        CLINSIG_vars = {"ClinicalSignificance":['probable-pathogenic','pathogenic','other']}

        # GMAF line variables
        GMAF_vars = {"allele":"allele=",
                     "sampleSize":"count=",
                     "freq":"MAF="}

        # CTG line variables
        CTG_vars = {"groupLabel":"assembly=",
                    "chromosome":"chr=",
                    "physmapInt":"chr-pos=",
                    "asnFrom":"ctg-start=",
                    "asnTo":"ctg-end=",
                    "loctype":"loctype=",
                    "orient":"orient="}

        # LOC line variables
        LOC_vars = {"symbol":1,
                    "geneId":"locus_id=",
                    "fxnClass":"fxn-class=",
                    "allele":"allele=",
                    "readingFrame":"frame=",
                    "residue":"residue=",
                    "aaPosition":"aa_position="}

        # LOC line variables
        SEQ_vars = {"gi":1,
                    "source":"source-db=",
                    "asnFrom":"seq-pos=",
                    "orient":"orient="}

        # Pull out variable information:
        r[rsId]['rs']       = pull_vars(rs_vars,"rs",snp)
        r[rsId]['ss']       = pull_vars(ss_vars,"ss",snp,True)
        r[rsId]['SNP']      = pull_vars(SNP_vars,"SNP",snp)
        r[rsId]['CLINSIG']  = pull_vars(CLINSIG_vars,"CLINSIG",snp)
        r[rsId]['GMAF']     = pull_vars(GMAF_vars,"GMAF",snp)
        r[rsId]['CTG']      = pull_vars(CTG_vars,"CTG",snp,True)
        r[rsId]['LOC']      = pull_vars(LOC_vars,"LOC",snp,True)
        r[rsId]['SEQ']      = pull_vars(SEQ_vars,"SEQ",snp,True)
    return r


#snp = get_snp(["1800562"])
# print pp(snp)