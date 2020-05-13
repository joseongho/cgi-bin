#!/bin/bash

if [ $REQUEST_METHOD = "GET" ]
then
cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

cat << EOL
<article>
	<form method="post">
		<input type="text" name="title">
		<textarea name="text"></textarea>
		<button>submit</button>
	</form>
</article>
EOL

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html

elif [ $REQUEST_METHOD = "POST" ]
then
read -n $CONTENT_LENGTH myTmp <&0
IFS='&'
eval $myTmp
echo $text > "/var/www/html/myDocument/$title"

cat << EOL
Location: /cgi-bin/myDocument.cgi

EOL
fi
