#!/bin/bash

myTmp=`ls /var/www/html/javascriptSlide`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

echo "<article><li>"
for img in $myTmp
do
	echo "<img src=\"/javascriptSlide/$img\" />"
done
echo "</li></article>"
echo "<script src=\"/javascriptSlide.js\"></script>"

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html
