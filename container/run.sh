#!/bin/sh


set -o errexit
set -o nounset


echo "wait"


start-history-server.sh
echo "History server is sarting ...."
sleep 2
echo "Master is sarting ...."
start-master.sh

sleep 1
echo "Master started at port 8080 ...."

echo "worker is sarting ...."

start-slave.sh spark://spark:7077

sleep 1
echo "worker started at port 8081 ...."

# spark-submit --master spark://spark:7077 --verbose /opt/project/pi.py
# spark-submit --class org.apache.spark.examples.SparkPi --master spark://spark:7077 --verbose /opt/spark/examples/jars/spark-examples*.jar 10
# sbt assembly
# spark-submit --master spark://spark:7077 --verbose RatingsCounter-assembly-1.0.jar 

sleep 100000