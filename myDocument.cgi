#!/bin/bash

myTmp=`ls /var/www/html/myDocument`

if [ "$REQUEST_METHOD" == "GET" ]
then

source getDocument.cgi

elif [ "$REQUEST_METHOD" == "POST" ]
then

source postDocument.cgi

fi
