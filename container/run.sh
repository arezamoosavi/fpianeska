#!/bin/sh


set -o errexit
set -o nounset


echo "wait"

# spark-submit --master local[*] --verbose /opt/project/test_spark.py
sleep 100000