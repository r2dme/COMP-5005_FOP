#!/bin/bash

exp_dir=shrimp`date "+%Y-%m-%d_%H:%M"`

mkdir $exp_dir

cp shrimpSimBase_v2.py $exp_dir 
cp shrimptest.py $exp_dir
cp shrimp_sweep.sh $exp_dir 
cd $exp_dir

num_experiment=$1 
simulation_time=$2 

echo "\n***Test Simulation with 5 sea monkeys for 10 steps***\n"
echo "\nParameters are: "
echo "Number of experiments : " $num_experiment
echo "Number of iterations : " $simulation_time

for i in `seq $num_experiment`; 
do
    for d in `seq $simulation_time`; 
    do
        echo "Experiment: " $i "Iteration: " $d 
        outfile="shrimp_I"$i"_D"$d".txt" 
        python3 shrimpSimBase_v2.py 5 10 $i $d > $outfile
    done 
done
