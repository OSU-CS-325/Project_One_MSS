(1) Put file "cs325_Group12_ProjectOne.tar.bz2" in an empty directory on FLIP

(2) Navigate to that directory

(3) Type the following command:
    
tar -xvf cs325_Group12_ProjectOne.tar.bz2
    
(4) You should see the following directories/files:

./enumeration/alg1.py             - Contains python code for the 'enumeration' algorithm
./better-enumeration/alg2.py      - Contains python code for the 'better-enumeration' algorithm
./divide-and-conquer/alg3.py      - Contains python code for the 'divide-and-conquer' algorithm
./linear-time/alg4.py             - Contains python code for the 'linear-time' algorithm
./run-files/testAlg.py            - Miscellaneous code
./run-files/projectOne.py         - Contains python code to run inputs through algorithms and create outputs
                                    Also runs tests and experimental analysis (commented out)
./run-files/runProjectOne.sh      - Shell script for running the code
./run-files/MSS_Problems.txt      - Input file provided with the assignment
./run-files/MSS_Results.txt       - Output file containing (for each input array for each algorithm):
                                    - The input array
                                    - Size of input array
                                    - Max sum subarray
                                    - Max sum
                                    - Runtime in 10^-6 seconds

(5) Navigate to the "run-files" directory

(6) Type the following command to run the code and produce your own copy of 'MSS_Results.txt':

./runProjectOne.sh
