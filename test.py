#!/usr/bin/env python
import os
from sh import sbatch


ROOT = os.path.dirname(__file__)


username = 'test1'
for i in range(5):
    sbatch('-A', username, os.path.join(ROOT, 'job.py'))

