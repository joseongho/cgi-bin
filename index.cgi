#!/bin/bash

cat << EOL
Content-type: text/html

EOL

cat < /var/www/html/index1.html

cat < /var/www/html/modal.html

cat < /var/www/html/nav.html

cat < /var/www/html/index2.html
