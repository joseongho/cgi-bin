#!/bin/bash

myTmp=`cat /var/www/html/myDocument/$QUERY_STRING`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

echo "<article><p>$myTmp</p></article>"

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html
