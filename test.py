#!/usr/bin/env python
import os
from sh import sbatch


ROOT = os.path.dirname(__file__)



for username in ('test1', 'test2'):
    for i in range(500):
        sbatch('-A', username, os.path.join(ROOT, 'job.py'))

