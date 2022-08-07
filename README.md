# MRPMS-FAHZU
Medical Research Project Management System (demo) for First Affiliated Hospital Zhejiang University School of Medicine
## 👋Welcome!  
This summer I was asked by an acquaintance to build a lightweight web management system for archived medical research projects at FAHZU. 
Prior to this, I didn't have any experience with API or jQuery - I had only built FLASK applications solely based on Python and SQL.
## ✍️Languages + Tools Used:
* HTML, CSS, Bootstrap 
* jQeury, JavaScript
* Python, Flask, RESTFUL API
* SQL (MS SQL Server)
## 🛠️Biggest Challenge:
* Chinese character display issues during the execution of RESTFUL API, database (selecting and inserting data requires different charsets), and serializing JSON. 
  * I wished to avoid the potential consequences of the encoding and decoding hassle so I wrote a function in connect.py file to select the correct charset based on specific SQL execution demands.


