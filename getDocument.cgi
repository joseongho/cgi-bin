#!/bin/bash

eval $QUERY_STRING

if [ -z "$QUERY_STRING"]
then

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

echo "<article><li>"
for arg in $myTmp
do
echo "<ul><a href="/cgi-bin/myDocument.cgi?myRead=$arg">$arg</a></ul>"
done
echo "</li><a href=\"/cgi-bin/createDocument.cgi\">createDocument</a></article>"

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html

elif [ -n "$myRead" ]
then

myTmp=`cat /var/www/html/myDocument/$myRead`

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

cat << EOL
<article>
	<p>title</p>
	<p>$myRead</p>
	<p>content</p>
	<p>$myTmp</p>
	<a href="/cgi-bin/myDocument.cgi?myDelete=$myRead">remove</a>
	<a href="/cgi-bin/myDocument.cgi?myUpdate=$myRead">update</a>
</article>
EOL

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html

elif [ -n "$myDelete" ]
then

rm "/var/www/html/myDocument/$myDelete"

cat << EOL
Location: /cgi-bin/myDocument.cgi

EOL

fi
