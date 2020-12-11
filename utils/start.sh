#!/bin/bash

pid=`ps -ef|grep nginx|grep -v 'grep'|awk '{print $2}'`

pids=`ps -ef|grep uwsgi|grep -v 'grep'|awk '{print $2}'`

if [[ ! $pids ]];then
    uwsgi --ini /home/app/uwsgi.ini
else
    echo "uwsgi is running."
fi


if [[ ! $pid ]];then
   /usr/sbin/nginx -c /etc/nginx/nginx.conf
else
   echo "nginx is running."
fi
