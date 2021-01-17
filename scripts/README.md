# install && monitor scripts

## email notification set up
* Install Msmtp client
```
sudo apt-get install msmtp-mta -y
```


* Configure msmtp for gmail
```
vim ~/.msmtprc
```
update the configuration file with following custom setup:
```
#Gmail account
defaults
#change the location of the log file to any desired location.
logfile ~/msmtp.log
account gmail
auth on
host smtp.gmail.com
from <yourmail@gmail.com>
auth on
tls on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
user <yourmail@gmail.com>
password <your-password>
port 587
#set gmail as your default mail server.
account default : gmail
```

protect scurity with 
```
chmod 600 .msmtprc
```

* Install heirloom-mailx
```
sudo apt-get install heirloom-mailx
```

* Configure Mailx
```
vim ~/.mailrc

set sendmail="/usr/bin/msmtp"
set message-sendmail-extra-arguments="-a gmail"

```
* test mail
```
mail -s "subject" -a "attachment-if-any" "receiver@some-domain.com"
```

* gmail less scure app access enable
https://myaccount.google.com/lesssecureapps

