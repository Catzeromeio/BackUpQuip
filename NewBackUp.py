 
import datetime
import json
import logging
import ssl
import sys
import time
import xml.etree.cElementTree

import urllib
import urllib2

Request = urllib2.Request
urlencode = urllib.urlencode
urlopen = urllib2.urlopen
HTTPError = urllib2.HTTPError

iteritems = dict.iteritems



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

# request = Request(
#     url=client._url("blob/%s/%s" % (thread_id, blob_id)))
# if client.access_token:
#     request.add_header("Authorization", "Bearer " + client.access_token)
# try:
#     re = urlopen(request, timeout=client.request_timeout)
def Traverse(client,foldid):
    folder = client.get_folder(foldid);
    for child in folder["children"]:
        if "folder_id" in child:
            Traverse(client,child["folder_id"])
        elif "thread_id" in child:
            threadid = child["thread_id"];
            TraverseThread(client,threadid)

def TraverseThread(client,threadid):
    thread = client.get_thread(threadid)
    title =  thread["thread"]["link"]
    print title

import quip
client = quip.QuipClient(access_token="ZE5CQU1BcmtwRnQ=|1600850712|2bH//fDrlft1cx03ktiYFA9kfST9arohKRuPd+WmL4k=")
user = client.get_authenticated_user()
# Traverse(client,user["private_folder_id"])
for i in user["group_folder_ids"]:
    Traverse(client,i)
