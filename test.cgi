#!/bin/bash

myTmp=`ls /var/www/html/cgiDocument`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

echo "<li>"
for arg in $myTmp
do
	echo "<ul><a href="/cgi-bin/test2.cgi?$arg">$arg</a></ul>"
done
echo "</li>"

cat < /var/www/html/index2.html
