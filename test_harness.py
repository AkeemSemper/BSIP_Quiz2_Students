#import thinkplot
#import thinkstats2
import pandas as pd
import numpy as np
import pytest
import scipy
import math

#Import solution file
import import_ipynb
import solution_file

#Load data file
df_in = pd.read_csv("diabetes.csv")
df_in.dropna()
df_in = df_in[df_in["BloodPressure"]>0]
df_in = df_in[df_in["SkinThickness"]>0]
df_in = df_in[df_in["BMI"]>0]
df_in = df_in[df_in["Glucose"]>0]
df_in = df_in[df_in["Insulin"]>0]


#Import remote solutions
import httpimport
from httpimport import *
url = "https://gist.githubusercontent.com/AkeemSemper/e5e433f1f3138889260634242bab19fd/raw/f9ead571f7590068b5eac5771d82f338ddef4838/"
with httpimport.remote_repo(["stats_Quiz2_sol"], url):
    import stats_Quiz2_sol

#Set Test Variables
col1 = "Glucose"
col2 = "BloodPressure"
col3 = "SkinThickness"
col4 = "Insulin"
col5 = "BMI"


@pytest.mark.a
def test_multiCorr():
    studAnswer = solution_file.rangeMag(df_in, col1, col2, False)
    solAnswer = stats_Quiz2_sol.rangeMag(df_in, col1, col2, False)
    print(studAnswer, solAnswer)
    assert math.isclose(studAnswer, solAnswer, abs_tol=.01)

@pytest.mark.b
def test_rankSkew():
    stud1, studSk1, stud2, studSk2, stud3, stdSk3 = solution_file.rankSkew(df_in, col5, col3, col4)
    sol1, solSk1, sol2, solSk2, sol3, solSk3 = stats_Quiz2_sol.rankSkew(df_in, col5, col3, col4)
    print(stud2, sol2, stud3, sol3)
    assert ((stud2 == sol2) & (stud3 == sol3))

@pytest.mark.c
def test_passAnalytical():
    studAnswer, mod1 = solution_file.passAnalytical(df_in, col3)
    solAnswer, mod2 = stats_Quiz2_sol.passAnalytical(df_in, col3)
    print(studAnswer, solAnswer)
    assert (studAnswer == solAnswer)

@pytest.mark.d
def test_logNormOrNorm():
    studAnswer = solution_file.lognormOrNorm(df_in, col2)
    solAnswer = stats_Quiz2_sol.lognormOrNorm(df_in, col2)
    print(studAnswer, solAnswer)
    assert (studAnswer == solAnswer)

test_multiCorr()
test_rankSkew()
test_passAnalytical()
test_logNormOrNorm