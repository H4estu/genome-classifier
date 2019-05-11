*-----------------------------------------------------------------------
* README.txt
*
* Instructions for running the SGE parallel job and SVM classifier for
* Zach Wallace.
*
* Class: BOT 599
* Term: Spring 2018
*-----------------------------------------------------------------------
*
*
* OVERVIEW
*
* All shell scripts to run are contained in the 'run_job' directory.  
* When running these scripts, stay in the top-level 'Wallace_Project' 
* directory where this README is located. Thus, all shell scripts will
* have a 'run_job/' prefix.
*
* Commands to enter are labeled below as numbered steps.  Here I briefly
* describe what each will do:
*
* 	   - Steps 1-3 build the first feature set to feed into the SVM.  
*	   - Steps 4-6 build the second feature set to feed into the SVM.
*	   - Step 7 runs the classifer.
*
* I had to include command line arguments for some of the scripts, since 
* the bash wrappers and the python functions were not playing well together.  
* If you simply copy and paste to your terminal and hit enter separately 
* for each step below (omitting the "Step X: " portions), all scripts
* should run smoothly.  I apologize for any inconvenience.
* 


Step 1: python3 run_job/1_delete_old_files.py

Step 2: ./run_job/2_pipeline.sh FASTA/exonseq_upstream100_MT.txt

Step 3: ./run_job/3_merge_files.sh class1.txt

Step 4: python3 run_job/1_delete_old_files.py

Step 5: ./run_job/2_pipeline.sh FASTA/flank_upstream100_MT.txt

Step 6: ./run_job/3_merge_files.sh class2.txt

Step 7: ./run_job/4_call_quick_svm.sh
