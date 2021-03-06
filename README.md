
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


See **slurm.conf** for details.

## Accounting


```
ubuntu@frontend001:~$ sacctmgr add account test1,test2
 Adding Account(s)
  test1
  test2
 Settings
  Description     = Account Name
  Organization    = Parent/Account Name
 Associations
  A = test1      C = gc3cluster
  A = test2      C = gc3cluster
 Problem adding accounts: Access/permission denied
ubuntu@frontend001:~$ sacctmgr show Account
   Account                Descr                  Org 
---------- -------------------- -------------------- 
       gc3                  gc3                  gc3 
      root default root account                 root 
ubuntu@frontend001:~$ sudo sacctmgr add account test1,test2
 Adding Account(s)
  test1
  test2
 Settings
  Description     = Account Name
  Organization    = Parent/Account Name
 Associations
  A = test1      C = gc3cluster
  A = test2      C = gc3cluster
Would you like to commit changes? (You have 30 seconds to decide)
(N/y): y

```


Correct command for coupling slurm account with user entity is: 

```
sudo sacctmgr add account test2
sudo sacctmgr add User ubuntu Account=test2
```


One can use commands like `sshare` `sprio` `sacct` to monitor the priority for the jobs.

Also see [1](https://www.hpc2n.umu.se/batchsystem/policies/abisko) and [2](http://slurm.schedmd.com/priority_multifactor.html)

```
Job_priority =
	(PriorityWeightAge) * (age_factor) +
	(PriorityWeightFairshare) * (fair-share_factor) +
	(PriorityWeightJobSize) * (job_size_factor) +
	(PriorityWeightPartition) * (partition_factor) +
	(PriorityWeightQOS) * (QOS_factor) +
	SUM(TRES_weight_cpu * TRES_factor_cpu,
	    TRES_weight_<type> * TRES_factor_<type>,
	    ...)
```
