#!/bin/bash

myTmp=`ls /var/www/html/javascriptSlide`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

echo "<li>"
for img in $myTmp
do
	echo "<img src=\"/javascriptSlide/$img\" />"
done
echo "</li>"
echo "<script src=\"/javascriptSlide.js\"></script>"

cat < /var/www/html/index2.html
