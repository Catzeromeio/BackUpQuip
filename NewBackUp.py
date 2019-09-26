 
import datetime
import json
import logging
import ssl
import sys
import time
import xml.etree.cElementTree

import urllib
import urllib2
import pdfkit

Request = urllib2.Request
urlencode = urllib.urlencode
urlopen = urllib2.urlopen
HTTPError = urllib2.HTTPError

iteritems = dict.iteritems

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
# except HTTPError as error:
# try:
# # Extract the developer-friendly error message from the response
# message = json.loads(error.read().decode())["error_description"]
# except Exception:
# raise error
# raise QuipError(error.code, message, error)
# user = client.get_authenticated_user()
# starred = client.get_folder(user["starred_folder_id"])
# print "There are", len(starred["children"]), "items in your starred folder"

def Traverse(client,foldid):
    folder = client.get_folder(foldid)
    for child in folder["children"]:
        if "folder_id" in child:
            Traverse(client,child["folder_id"])
        elif "thread_id" in child:
            threadid = child["thread_id"]
            DealwithThread(client,threadid)

def DealwithThread(client,threadid):
    thread = client.get_thread(threadid)
    link =  thread["thread"]["link"]
    title = thread["thread"]["title"]
    pdfkit.from_url(link,"hah.pdf",configuration=config)
    # if client.access_token:
    #     request.add_header("Authorization", "Bearer " + client.access_token)
    #     re = urlopen(request, timeout=500)
    #     with  open("./%s.txt" % (title),"w") as thedox:
    #         thedox.write(re.read())

import quip
client = quip.QuipClient(access_token="ZE5CQU1BcmtwRnQ=|1600850712|2bH//fDrlft1cx03ktiYFA9kfST9arohKRuPd+WmL4k=",request_timeout=500)
user = client.get_authenticated_user()
# Traverse(client,user["private_folder_id"])
for i in user["group_folder_ids"]:
    Traverse(client,i)
