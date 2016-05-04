## Genes in UniProtKB/SwissProt with experimentally valided annotations  
* How many genes for each species in the UniProtKB/SwissProt whose 
  annotations have experimental validations? 

#### Some informative sites 

#### UniProtKB/SwissProt
This is a non-redundant protein sequence database. Each entry in this database
is manually annotated involving detailed analysis of the protein sequence and
of the scientific literature. The database is recognized as the central access
point of the extensive curated protein information, classification, and
cross-reference.

* UniProtKB/SwissProt dataset current release:
  ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/
* UniProtKB/SwissProt dataset archive (release 46 and greater):
  ftp://ftp.uniprot.org/pub/databases/uniprot/previous_releases/
* UniProtKB/SwissProt dataset archive (release 9 to 45):
  ftp://ftp.ebi.ac.uk/pub/databases/swissprot/sw_old_releases/
* Detailed release statistics:
  http://web.expasy.org/docs/relnotes/relstat.html
* UniProtKB/SwissProt file format:
  http://arep.med.harvard.edu/labgc/jong/Fetch/SwissProtAll.html

### Requirements
* Python 2.7 
* Biopython 1.66 or greater 

### Software Usage 

The details of the usage description of this software are as follows.

#### Statistics of Experimentally Annotated Genes 

This program will create a file with the number of genes whose annotations 
are experimentally validated for a set of organism over a series of time 
points. The simplest way to run the program: 

python Count_genes --input1 file_listing_species_taxon_ids --input2 file_listing_sprot_filenames.txt 

input1 is a TWO column text file containing the list of species: the first 
column has the taxon id and the second column has the organism name. input2 
is a list of UniprotKB/SwissProt filenames over a series of time points.

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt -O=sprot_genes.txt
```

It will create an output file: sprot_genes.stat.1 
This output file has one row for each SwissProt file listed in 
sprot_files.txt. Each row has THREE columns for each organism, 
according to the organisms listed in sp_list.txt file. 


### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/CAFA-Toolset.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),  
Ataur Katebi (arkatebi@gmail.com).

