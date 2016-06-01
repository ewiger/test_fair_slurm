
#test_fair_slurm

A bunch of scripts to test that the slurm has a correctly set up "fair share"
policy


## Configuration details

Assuming you have an installed and configured SLURM cluster.


The multifactor plugin has a "fair share" component that does exactly what you want: attempt to give each user a predefined share of the cluster's time.  (In practice, this means: if you are below your usage quota over a certain time window, your jobs get more priority; on the contrary, if you are *over* quota then your jobs get down-prioritized.)

An cut out of parameters:

    PriorityType=priority/multifactor

    # set the weight of factors
    PriorityWeightAge=1000
    PriorityWeightFairshare=5000
    PriorityWeightJobSize=500
    PriorityWeightPartition=1000
    PriorityWeightQOS=2000

    # configure the fairshare factor
    PriorityDecayHalfLife=14-0
    PriorityFavorSmall=NO
    PriorityMaxAge=7-0
    PriorityUsageResetPeriod=NONE

More info on the fair-share plugin configuration: <http://slurm.schedmd.com/priority_multifactor.html#fairshare>
