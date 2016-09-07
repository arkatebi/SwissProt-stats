<a name="title" />
## Impact of 'Open World Assumption' on evaluation of predictive model
* The open-world problem arises from the open-world assumption: 'the 
  absence of evidence does not amount to the evidence of absence'.
* In this project, I investigate this problem by taking the advantage 
  of the curated growth of the protein annotation database, 
  UniProtKB/SwissProt.
* I update this repository with the new tools that I develop to 
  facilitate the research. 

### Contents
1\. [Introduction] (#intro)

2\. [Experiment Design] (#expDesign)

3\. [Requirements to use the tools] (#requirements)

4\. [Gene Count Statistics] (#geneCounts)

5\. [Generate Training and Evaluation Sets] (#genSets)

5.1\. [Generate Training Set] (#genTrainingSet)

5.2\. [Generate Evaluation Set-1] (#genEvalSet-1)

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

<a name="expDesign" />
### Experimental Design 
The following figure shows the time points for collecting the training and 
evaluation sets. 

![alt Experiment Design] (/figures/experiment-design-1.2.png?raw=true “Experiment Design”)

<a name="requirements" />
### Requirements
* Python 3.5 or greater
* Biopython 1.66 or greater

<a name="geneCounts" />
### Gene Count Statistics 
The statistics for gene counts in the UniProtKB/SwissProt can 
be found by following the link below: 

https://github.com/arkatebi/SwissProt-stats/blob/master/geneCount.md

<a name="genSets" />
### Generate Training and Evaluation Sets 

The details of the usage description of this software are as follows.

<a name="genTrainingSet" />
#### Generate Training Set 

This program will extract the sequences of the proteins that have 
experimental evidence codes in a UniProt/SwissProt file: 

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01

```
The input file uniprot_sprot.dat.2010_01 is the UniProt/SwissProt file 
where the sequences are extracted from. The program generates the
following six output files - two files for each ontological category:

```
uniprot_sprot.dat.2010_01.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01.tfa_LK_cco.1
uniprot_sprot.dat.2010_01.tfa_LK_cco.1.map
```

The first ouput file has the extracted training sequences in the FASTA 
file format for MFO ontology. The id for each sequence is constructed from 
a program generated string and the SwissProt name of the protein. The 
second output file records the mapping between the program generated string 
and the SwissProt protein name, corresponding to the entries in the first 
file. Subsequent files are for BPO and CCO ontological categories.

The program can also be used to extract training sequences for a specific 
organism:

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606
```

This will generate the following output files:

```
uniprot_sprot.dat.2010_01.9606.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01.9606.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01.9606.tfa_LK_cco.1
uniprot_sprot.dat.2010_01.9606.tfa_LK_cco.1.map
```

This program can also take an optional output file name: 

```
python xTract_trainingSet -I1=uniprot_sprot.dat.2010_01 -G=9606 -O=trainingSet
```

This will create the following output files:

```
trainingSet.9606.tfa_LK_mfo.1
trainingSet.9606.tfa_LK_mfo.1.map
trainingSet.9606.tfa_LK_bpo.1
trainingSet.9606.tfa_LK_bpo.1.map
trainingSet.9606.tfa_LK_cco.1
trainingSet.9606.tfa_LK_cco.1.map
```

Repeated run of the program will create the subsequent versions of each 
output file.

<a name="genEvalSet-1" />
#### Generate Evaluation Set-1 (ES-1)

This program will extract the sequences of the proteins whose annotations
did not have experimental evidence codes in UniProt/SwissProt database at time
t1 but gained experimental evidence codes at time t2:

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01

```
The first input file uniprot_sprot.dat.2010_01 is the UniProt/SwissProt 
annotation file at t1 and the second input file uniprot_sprot.dat.2011_01 is the 
UniProt/SwissProt annotation file at t2. The name of a SwissProt file should have 
the following format: a file name prefix followed by the exact string .dat. 
followed by the time stamp (in yyyy_mm format). The program generates the 
following six output files - two files in each ontological category:

```
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_cco.1
uniprot_sprot.dat.2010_01-2011_01.tfa_LK_cco.1.map
```

The first ouput file has the extracted test sequences in the FASTA 
file format for MFO ontology. The id for each sequence is constructed from 
a program generated string and the SwissProt name of the protein. The 
second output file records the mapping between the program generated string 
and the SwissProt protein name, corresponding to the entries in the first file.
The subsequent two pairs of files are for BPO and CCO ontological categories, 
respectively.

The program can also be used to extract sequences for a specific organism:

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01 -G=9606
```

This will generate the following output files:

```
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_mfo.1
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_mfo.1.map
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_bpo.1
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_bpo.1.map
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_cco.1
uniprot_sprot.dat.2010_01-2011_01.9606.tfa_LK_cco.1.map
```

This program can also take an optional output file name: 

```
python xTract_testSet -I1=uniprot_sprot.dat.2010_01 -I2=uniprot_sprot.dat.2011_01 -G=9606 -O=testSet
```

This will create the following output files:

```
testSet.9606.tfa_LK_mfo.1
testSet.9606.tfa_LK_mfo.1.map
testSet.9606.tfa_LK_bpo.1
testSet.9606.tfa_LK_bpo.1.map
testSet.9606.tfa_LK_cco.1
testSet.9606.tfa_LK_cco.1.map
```

Repeated run of the program will create the subsequent versions of each 
output file.

### Source Code
This is an open source project and the source code is publicly available on 
GitHub through the following URL: https://github.com/arkatebi/OpenWorld-problem.
For questions, please email either of us: Iddo Friedberg (idoerg@gmail.com),  
Ataur Katebi (arkatebi@gmail.com).

[Go to the top] (#title)
