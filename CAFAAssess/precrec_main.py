#!/usr/bin/env python2
# -*- coding: utf-8 -*-
''' This program calculates precision-recall valuses from prediction scores. 
    How to run the program: 
    pythonn2 ./CAFAAssess/precrec_main.py -I1=./workspace/blastScores/evalSet-1.bpo.scores.txt.1 
                                          -I2=./workspace/evalSets/bm-evalSet-1.bpo 
                                          -G=BPO 
                                          -O=./CAFAAssess/tmp-BPO-4.png
   First input parameter is a prediction score file, whose column 1 has the
        target name, column 2 has the GO term, and column 3 has the
        confidence score.
   Second input file is a benchmark file, whose column 1 has the target name
        and column 2 has the experimentally verified GO term.
   Third input parameter is the ontology name: MFO, BPO, or CCO
   Fourth input parameter is an output filename, where the precision-recall
        scores will be stored.
'''

import sys
import os
sys.path.append(os.getcwd())
import argparse
from CAFAAssess.precRec import PrecREC,read_benchmark
from CAFAAssess.precrec.GOPred import GOPred
import matplotlib.pyplot as plt
import numpy

def get_namespace_index(namespace):
    '''
    copied from confidence.py 07/15/2016
    '''
    num = None
    if namespace=='BPO' or namespace=='bpo':
        num = 0
    elif namespace=='MFO' or namespace=='mfo':
        num = 1
    elif namespace=='CCO' or namespace=='cco':
        num =2
    else:
        raise ValueError("name space not found, check prediction files")
        print namespace
    return num

parser = argparse.ArgumentParser(description='Precision- Recall assessment ' + \
         'for protein function predictions.', )
parser.add_argument('-I1', '--input1',type=open, help='Input the path of the ' + \
                    'prediction file. File should be split according ' + \
                    'to ontology, and should be a .txt file')
parser.add_argument('-I2', '--input2', help='Input the path of the ' + \
                    'benchmark file. File should have two columns: ' + \
                    'column 1: protein name, column 2: GO term')
parser.add_argument('-G', '--ontology',help='Input ontology',
                     choices=['BPO','MFO','CCO'])
parser.add_argument('-O', '--output', help='Input path+filename to save '+ \
                    'the Precision-Recall plot')
args = parser.parse_args()

print('prediction file: %s' %args.input1)
print('benchmark file: %s' %args.input2)
print('Ontology: %s' %args.ontology)
print('Output plot file: %s' %args.output)

bench = read_benchmark(args.ontology, args.input2)

all_pred = GOPred()
all_pred.read(args.input1)

c = PrecREC(bench,all_pred)
fm = c.Fmax_output(99)

plt.plot(fm[1],fm[0])
plt.axis([0,1,0,1])
plt.yticks(numpy.arange(0,1,0.1))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title(args.ontology)
plt.savefig(args.output,dpi=200)
plt.close()

print('fmax value for this prediction is: %s.\n' % fm[2])
print('PR plot is saved to %s.\n' % args.output)
