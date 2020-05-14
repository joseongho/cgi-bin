#!/bin/bash

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/nav.html

cat < /var/www/html/header.html

cat << EOL
<article>
	<form action="myDocument.cgi" method="post">
		<input type="text" name="title">
		<textarea name="text"></textarea>
		<button>submit</button>
	</form>
</article>
EOL

cat < /var/www/html/footer.html

cat < /var/www/html/index2.html

