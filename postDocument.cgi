#!/bin/bash

read -n $CONTENT_LENGTH myTmp <&0
IFS='&'
eval $myTmp
echo $text > "/var/www/html/myDocument/$title"

cat << EOL
Location: /cgi-bin/myDocument.cgi

EOL
