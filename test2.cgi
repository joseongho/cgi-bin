#!/bin/bash

myTmp=`cat /var/www/html/cgiDocument/$QUERY_STRING`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

echo $myTmp

cat < /var/www/html/index2.html
