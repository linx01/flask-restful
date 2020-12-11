#!/bin/bash

pid=`ps -ef|grep nginx|grep -v 'grep'|awk '{print $2}'`
for p in $pid
do
kill -9 $p
done

pids=`ps -ef|grep uwsgi|grep -v 'grep'|awk '{print $2}'`
for p in $pids
do
kill -9 $p
done
