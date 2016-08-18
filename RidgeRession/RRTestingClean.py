#Brandyn Deffinbaugh & James Gray
#Ridge Regression for Phenotype(X) and Genotype(Y) using Sci-Kit Learn
#May 2016

from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import Ridge
import numpy as np

#Reads in the data file and parses the input
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


def alphaOptimization(geno,pheno):
        alphas = np.array([0.1,0.01,0.001,0.0001,0.5,0.05,0.2,0.002,0.0002,1,0])
        model = Ridge()
        grid = GridSearchCV(estimator = model, param_grid=dict(alpha=alphas))
        grid.fit(geno,pheno)
        grid.best_score_
        return grid.best_estimator_.alpha


def RidgeRegression(file):
        pheno,geno = inputParse(file)
        rowLength = len(geno[0])
        for row in geno:
                if len(row)%2 !=0:
                        return "Rows are not even."
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
        oldGeno = geno
        
        geno = []
        for row in oldGeno:
                hold = [row[i:i+2] for i in range(0,len(row),2)]
                geno.append(hold)
        print geno[0]
        pheno = [float(i) for i in pheno]
        phenoLen = len(pheno)
        alpha = alphaOptimization(oldGeno,pheno)
        oldPheno = pheno
        pheno = []
        
        for x in range(rowLength/2):
                pheno.append(oldPheno[i])
        pheno = np.asarray(pheno)
        pheno = np.reshape(pheno,(rowLength/2,phenoLen))
        print len(pheno[0])
        genoIterVal = 0
        phenoIterVal = 0
        for i in range(len(geno)):
                clf = Ridge(alpha=alpha)
                print clf.fit(geno[i][genoIterVal:genoIterVal+rowLength/2],pheno[phenoIterVal])
                coef = clf.coef_
                importantCoef = []
                for i in coef:
                        if i >1:
                        importantCoef.append(i)
                print importantCoef
                genoIterVal += rowLength/2
                phenoIterVal +=1
                if phenoIterVal == phenoLen:
                        phenoIterVal = 0
        #print clf.predict(geno)



RidgeRegression('DongWang.ped')
