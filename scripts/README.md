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

## crontab work set up
note utc time is used in gcp machine local time, conert it into us eastern time
```
0 7 * * *  ~/chives/scripts/monitor.sh  2>&1 | mail -s "chives daily auto sync from crontab" wpw436@gmail.com
0 1 * * 0  ~/chives/scripts/backup_data.sh 2>&1 | mail -s "chives cold storage backup from crontab" wpw436@gmail.com
0 3 * * 6  ~/chives/scripts/monitor_option.sh 2>&1 | mail -s "chives weekly option monitoring from crontab" wpw436@gmail.com
0 5 * * 6  ~/chives/scripts/monitor_option.sh 2>&1 | mail -s "chives weekly option monitoring from crontab" wpw436@gmail.com
0 0 1 * *  ~/chives/scripts/monitor_financial_report.sh 2>&1 | mail -s "chives monthly financial report from crontab" wpw436@gmail.com
```

common crontab debug cmd
```
crontab -e # for non-sudo user
grep CRON /var/log/syslog # crobtab log
```