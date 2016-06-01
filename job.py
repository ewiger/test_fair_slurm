#!/usr/bin/env python

import time


def wait(period=5):
    print 'sleeping for: %s' % period
    time.sleep(period)


if __name__ == '__main__':
    for x in range(60):
        wait()
