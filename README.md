# Batch-Script-Go
Small tools useful when I working on windows. Hope to help you.

## friday_report.bat
This batch script will creat a file named by the date of coming friday, 
and pop up a message to tell you let's write the weekly report.
It can be double click to run, whenever you wish to write weekly report.
In fact, usually, it is set into the task scheduler to run every friday afternoon automaticly.

## text2qrcode.py
This python script will read a text file and then transform to Quick Response Code(qr code), 
which is convinience for extracting middle text file from networkless and usbless device. 

How to use it?
> python text2qrcode.py text2qrcode.py

or add compress command:
> python text2qrcode.py text2qrcode.py --compress

## make_album.py
This python script will assamble all txt file in the folder and then print them into one txt file which is named album.txt.

## assemble_report.bat
This batch script is going to run make_album.py as a easy way.
