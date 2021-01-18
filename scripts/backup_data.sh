#!/bin/bash


# crontab synced every week
# 0 6 * * 6  ~/chives/scripts/backup_data.sh 2>&1 | mail -s "chives cold storage backup from crontab" wpw436@gmail.com

printf -v tmpname '%(%Y_%m_%d)T.tar\n' -2

tar zcf $tmpname ~/chives/datahut/data

gsutil cp $tmpname gs://chives_backup

echo "successfully loadded to gs://chives_backup/$tmpname"
