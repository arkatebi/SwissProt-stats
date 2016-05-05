#!/usr/bin/env python
'''
    This module has the following method:

    count_genes_with_EXP:
        This method takes four input arguments:
            (1) a uniprot-swissProt file handle,
            (2) a taxonomy id,
            (3) the set of EXP codes.
            
        This method counts the number of proteins whose annotations 
        have experimental evidences, in each of BPO, CCO, and MFO ontological 
        categories, for an organism with the supplied taxon id.
          
        Finally, it returns these THREE counts.
'''
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SwissProt as sp

def count_genes_with_EXP(fh_sprot, taxon_id, EXP_default=set([])):
    # The exp_ct variable counts total number of genes in 
    # the sprot file related to the taxonomy id taxon_id whose 
    # annotations have EXP evidence:
    exp_ct = 0

    # The exp_bpo_ct variable counts total number of genes in 
    # the sprot file related to the taxonomy id taxon_id whose 
    # annotations have EXP evidence and in BPO ontological category:
    exp_bpo_ct = 0

    # The exp_cco_ct variable counts total number of genes in 
    # the sprot file related to the taxonomy id taxon_id whose 
    # annotations have EXP evidence and in CCO ontological category:
    exp_cco_ct = 0

    # The exp_mfo_ct variable counts total number of genes in 
    # the sprot file related to the taxonomy id taxon_id whose 
    # annotations have EXP evidence and in MFO ontological category:
    exp_mfo_ct = 0

    for rec in sp.parse(fh_sprot):
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            exp_code = False
            # Go over the list of GO information:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that 
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0], 
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
                        exp_code = True
                        exp_ct += 1
                        if goList[-1].upper() == 'P': 
                            exp_bpo_ct += 1
                        elif goList[-1].upper() == 'C':
                            exp_cco_ct += 1
                        elif goList[-1].upper() == 'F':
                            exp_mfo_ct += 1
                        #break
#    return (exp_ct, exp_bpo_ct, exp_cco_ct, exp_mfo_ct)
    return (exp_bpo_ct, exp_cco_ct, exp_mfo_ct)

def count_genes_with_EXP_per_species_old(fh_sprot, taxon_id, EXP_default=set([])):
    # The rec_count variable counts the number of records
    rec_count = 0

    # The seqCopunt variable counts total number of sequences
    # in the sprot file related to the the taxonomy id taxon_id:
    seqCount = 0

    # The seqCount_exp variable counts total number of sequences in 
    # the sprot file related to the the taxonomy id taxon_id whose 
    # annotations have EXP evidence:
    seqCount_exp = 0

    # The seqCount_no_exp variable counts total number of sequences in 
    # the sprot file related to the the taxonomy id taxon_id whose 
    # annotations have EXP evidence:
    seqCount_no_exp = 0

    for rec in sp.parse(fh_sprot):
        rec_count += 1
        # SELECT records that are related to a specific
        # taxon_id such as 559292 for yeast:
        if taxon_id in rec.taxonomy_id:
            exp_code = False
            seqCount += 1
            # Go over the list of GO information:
            for crossRef in rec.cross_references:
                # Consider the cross_reference entries that 
                # relate to GO DB:
                if crossRef[0] == 'GO':
                    goList = [crossRef[1],
                              (crossRef[3].split(':'))[0], 
                              crossRef[2][0]]
                    if (crossRef[3].split(':'))[0] in EXP_default:
                        exp_code = True
                        seqCount_exp += 1
                        #break
            # If the protein has an no EXP evidence,
            # increase seqCount_no_exp:
            if not exp_code: 
                seqCount_no_exp += 1
#    return (rec_count, seqCount, seqCount_exp)
    return seqCount_exp

if __name__ == '__main__':
    print (sys.argv[0] + ':')
    print(__doc__)
    sys.exit(0)
