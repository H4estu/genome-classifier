#!/usr/bin/tcsh
setenv R_LIBS "${R_LIBS}:/local/cluster/R_Packages/3.3"

set class1=output/merge/class1.txt
set class2=output/merge/class2.txt

Rscript SVM/quick_svm.R $class1 $class2
