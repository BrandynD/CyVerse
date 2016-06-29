#Brandyn Deffinbaugh & James Gray
#Ridge Regression for Phenotype(X) and Genotype(Y) using Sci-Kit Learn
#May 2016

from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import Ridge
import numpy as np
import os



def inputParse(file):
    pheno = []
    geno = []
    with open(file) as infile:
        for line in infile:
            line = line.strip('\n')
            line = line.replace(' ','\t',6)
            line = line.split('\t')
            genoHold = line[6]
            genoHold = genoHold.split(' ')
            phenoHold = line[5]
            geno.append(genoHold)
            pheno.append(phenoHold)
    return(pheno,geno)


#Transposes the matrix
#def transpose(mtx):
#    transpose = list(zip(*mtx))
#    return transpose

def transpose(mtx):
        mtx = [list(x) for x in zip(*mtx)]
        return mtx



def makeGenoAverages(geno,length,lenInnerGeno,genoMake):
    genoAvgMake = []
    for i in range(length):
        for x in range(lenInnerGeno):
            genoInner = geno[i][x]
            iterate = 0
            for j in range(len(allGeno)):
                genoMake[iterate]=genoInner.count(genoInner[j])
                iterate +=1
            total = 0
            for j in genoMake:
                total += x
            for j in range(len(genoMake)):
                genoMake[x] = genoMake[j]/total
    return genoMake


def alphaOptimization():
    alphas = np.array([1,0.1,0.01,0.001,0.0001,0.5,0.05,0.2,0.002,0])
    modal = Ridge()
    grid = GridSearchCV(estimator = model, param_grid=dict(alpha=alphas))
    grid.fit()


def RidgeRegression(file):
    pheno,geno = inputParse(file)
    maxGeno = max(geno)
    allGeno = list(set(maxGeno))
    encoder = [i for i in range(len(allGeno))]
    lengthGeno = len(geno)
    length = len(geno)
    lenInnerGeno = len(geno[0])
    genoMake = [0 for x in range(len(allGeno))]
    dictionary = dict(zip(allGeno,encoder))
    for i in range(length):
        for x in range(lenInnerGeno):
            geno[i][x] = dictionary[geno[i][x]]
    geno = transpose(geno)
    genoAvgMake = makeGenoAverage(geno,length,lenInnerGeno,genoMake)

        
    
    
    
