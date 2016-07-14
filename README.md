<a name="title" />
## Impact of incomplete knowledge on function-prediction and evaluation of predictive model
* This is an ongoing project. In this project, I am developing tools to 
  facilitate my research into the impact of incomplete knowledge on the 
  functional predictions of proteins and the evaluation of the related 
  predictive models. Currently, the toolset has the following programs:
* A program that creates a table of gene counts for a set of species in
  UniProtKB/SwissProt whose annotations have experimental evidence codes.
* A program that creates graphs of the gene counts for those speceis over
  a series of time points.
* More programs will be added as the research continues ...

### Contents
1\. [Introduction] (#intro)

2\. [Some Informative Sites] (#sites)

2.1\. [UniProtKB/SwissProt] (#swissprot)

2.2\. [Experimental Evidence Codes] (#expCode)

3\. [Requirements to Run the Software] (#requirements)

4\. [Software Usage] (#usage)

4.1\. [Generate Gene Counts Annotated by Exp Evidence Codes] (#genGeneCounts)

4.2\. [Generate Graphs for Gene Counts] (#genGraphs)

4.3\. [Generate Training Set] (#genTrainingSet)

5\. [Graphical Views of Gene Counts] (#graphicalView)

5.1\. [Gene Counts: Jan 2010 to May 2016] (#year_2010to2016)

5.2\. [Gene Counts: Jan 2012 to May 2016] (#year_2012to2016)

<a name="intro">
#### Introduction
Models for functional predictions of proteins are developed based on the
current state of the functional annotation databases. However, the
annotations of most proteins are incomplete. Therefore, the question arises
whether the assigned strengths and weaknesses of the predictive models based
on the current knowledge still hold when new annotations becomes 
available through additional experiments. The situation can be depicted in the
following figure.

![alt Incomplete Knowledge] (/figures/incomplete-knowledge-1.1.png?raw=true “Incomplete Knowledge”)

Suppose, T is the set of experimentally annotated functions for some protein, 
according to the current state of knowledge. Some model A predicts this 
set to be P. Therefore, tp (true positive) = |P∩T|, fp (false positive) = 
|P-T|, and fn (false negative) = |T-P|. The performance will be measured 
according to these values. Now, if, because of new experiments, T expands to 
become T′ as shown in the figure above, then tp, fp, and fn will change. We 
want to address the following question: how can this change of knowledge 
impact the performance evaluation of the predictive model A?

<a name="sites" />
#### Some Informative Sites 

<a name="swissprot" />
##### UniProtKB/SwissProt
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
  http://web.expasy.org/docs/userman.html

<a name="expCode" />
##### Experimental Evidence Codes 

* Guide to GO evidence codes: 
  http://geneontology.org/page/guide-go-evidence-codes
* Evidence code decision tree: 
  http://geneontology.org/page/evidence-code-decision-tree  

<a name="requirements" />
### Requirements to Run the Software 
* Python 3.5 or greater
* Biopython 1.66 or greater

<a name="usage" />
### Software Usage 

The details of the usage description of this software are as follows.

<a name="genGeneCounts" />
#### Generate Gene Counts Annotated by Exp Evidence Codes

This program creates an output file listing the number of genes, whose
annotations have experimental evidence codes in the UniProtKB/SwissProt
annotation databases, for a set of organisms over a series of time points.
One can run this program in the following way:

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt
```

The first input file, sp_list.txt, is a text file listing the species
to be considered. The second input file, sprot_files.txt, is a text file
listing the UniprotKB/SwissProt filenames over a series of time
points. Successful run of this program will create an output file,
sprot_genes.stat.1, that will have the gene count values. Repeated run
of this program will create subsequent versions of the output file.
The program can also take an optional output filename prefix as an
additional argument as shown below and will behave the same way.

```
python Count_genes -I1=sp_list.txt -I2=sprot_files.txt -O=geneCount.stat
```

###### Automatic download of the datasets
If the program does not find the UniProtKB/SwissProt files in the
current or working directory, it will automatically download them.

###### File format of the first input file
The first input file, sp_list.txt, is a TWO-column text file where
each row corresponds to one species. The first column has the taxonomy 
ids and the second column has the organism names. Blank lines are allowed.

###### File format of the second input file
The second input file, sprot_files.txt, is a ONE-column text file where
each line corresponds to a UniprotKB/SwissProt filename at a timepoint.
The filenames should be listed according to the desired series of valid 
time points. Blank lines are allowed. However, the filenames listed in 
this file must follow this specific naming format: 
uniprot_sprot.dat.2010_01 where the first part uniprot_sprot.dat. is a 
string in lowercase and the second part is a string in the format yyyy_mm, 
yyyy being a FOUR-digit year and mm a TWO-digit month. Also, the program 
will not accept any year before 2010.

###### File format of the output file
The output file, sprot_genes.stat.1, has two header lines: the first line
has the taxonomy ids and the second line has three strings (MFO, BPO, and
CCO) under each taxonomy id to indicate the ontological categories of
Molecular Function, Biological Process, and Cellular Component,
respectively. The subsequent lines are for the gene count values - one row
for each timepoint. The gene count values on each row are listed in groups,
where each group has THREE values corresponding to a specific organism.
The THREE gene count values in each group are for MFO, BPO, and CCO
ontological categories, respectively. The order of the organisms on a row
are the same as they are found in the sp_list.txt file.

##### Execution time
The UniProtKB/SwissProt files are large in size (each file several 
GB). Running this program for the first time, without having those files
already stored in the workspace, will automatically download the files 
taking a substantial amount of time. Execution time breakdown for a 
first time run of this program with the default input files on a 
computing environment, consisting of an Intel hardware platform 
(Intel(R) Core(TM) i7-4790 CPU @ 3.60 GHz, 16 GB System Memory) 
operated by Ubuntu 14.04.4 LTS, is as follows: 

* Download time for the target set of UniProtKB/SwissProt files: 
  01 hr, 14 min, and 30 sec.
* Gene count time for the query species in those target files:
  02 hr, 20 min, and 14 sec.

A subsequent run of this program would cost only the gene count time.

<a name="genGraphs" />
#### Generate Graphs for Gene Counts

This program will create a graph of the gene count for each organism 
that is found in the above step. One can run the program as follows:

```
python Plot_geneCounts -I1=sp_list.txt -I2=sprot_files.txt -I3=geneCount.stat.1
```

where the first and the second input files are the same as they are for 
the Count_genes program in the previous section. The third input file 
geneCount.stat.1 is the output file from the Count_genes program. 

For these specific input files, the Plot_geneCounts program generates the 
following figure files (one figure for each speceis):

```
geneCount.9606.1.png
geneCount.10090.1.png
geneCount.3702.1.png
geneCount.10116.1.png
geneCount.559292.1.png
geneCount.9913.1.png
geneCount.284812.1.png
geneCount.83333.1.png
geneCount.224308.1.png
geneCount.44689.1.png
```

Repeated run of the program creates the subsequent versions of each figure file. 

The program can also take an output filename prefix as an additional argument 
as shown below. 

```
python Plot_geneCounts -I1=sp_list.txt -I2=sprot_files.txt -I3=geneCount.stat.1 -O=geneCount
```

This will behave the same way as it does without the additional argument, 
except that the figure name prefix can be supplied to the program in the 
latter case.

<a name="genTrainingSet" />
#### Generate Training Set 

This program will extract the sequences of the proteins that have 
experimental evidence codes in a UniProt/SwissProt file: 

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01

```
The input file uniprot_sprot.dat.2010_01 is the UniProt/SwissProt file 
where the sequences are extracted from. The program generates the
following two output files:

```
uniprot_sprot.dat.2010_01.tfa.1
uniprot_sprot.dat.2010_01.tfa.1.map
```

The first ouput file has the extracted training sequences in the FASTA 
file format. The id for each sequence is constructed from a program 
generated string and the SwissProt name of the protein. The second output 
file records the mapping between the program generated string and 
the SwissProt protein name.

The program can also be used to extract sequences for a specific organism:

```
python2 xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606
```

This will generate the following two output files: 

```
uniprot_sprot.dat.2010_01.tfa.9606.1
uniprot_sprot.dat.2010_01.tfa.9606.1.map
```

This program can also take an optional output file name: 

```
python2 xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606 -O=trainingSet.9606
```

This creates the following two output files:

```
trainingSet.9606.1
trainingSet.9606.1.map
```

Repeated run of the program creates the subsequent versions of each out file. 

<a name="graphicalView" />
### Graphical View of Gene Counts 

<a name ="year_2010to2016" />
##### Gene Counts: Jan 2010 to May 2016
The following command creates the gene count file: geneCount_2010to2016.stat.1 

```
python Count_genes -I1=sp_list.txt -I2=sprot_2010to2016.txt -O=geneCount_2010to2016.stat.1
```
The following command creates the figures to show the gene counts generated:

```
python Plot_geneCounts -I1=sp_list.txt -I2=sprot_2010to2016.txt -I3=geneCount_2010to2016.stat.1 -O=geneCount_2010to2016
```

The figures can be viewed by following the link below:

https://github.com/arkatebi/SwissProt-stats/blob/master/geneCount_2010to2016.md

<a name ="year_2012to2016" />
##### Gene Counts: Jan 2012 to May 2016
The following command creates the gene count file: geneCount_2012to2016.stat.1 

```
python Count_genes -I1=sp_list.txt -I2=sprot_2012to2016.txt -O=geneCount_2012to2016.stat.1
```

The following command creates the figures to show the gene counts generated:

```
python Plot_geneCounts -I1=sp_list.txt -I2=sprot_2012to2016.txt -I3=geneCount_2012to2016.stat.1 -O=geneCount_2012to2016
```

The figures can be viewed by following the link below:

https://github.com/arkatebi/SwissProt-stats/blob/master/geneCount_2012to2016.md

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/SwissProt-stats.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),  
Ataur Katebi (arkatebi@gmail.com).

[Go to the top] (#title)
