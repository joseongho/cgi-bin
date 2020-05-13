#!/bin/bash

eval $QUERY_STRING
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
	<a href="">remove</a>
</article>
EOL

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html
