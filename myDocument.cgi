#!/bin/bash

myTmp=`ls /var/www/html/myDocument`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

echo "<article><li>"
for arg in $myTmp
do
	echo "<ul><a href="/cgi-bin/readDocument.cgi?$arg">$arg</a></ul>"
done
echo "</li><a href=\"/cgi-bin/createDocument.cgi\">createDocument</a></article>"

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html
