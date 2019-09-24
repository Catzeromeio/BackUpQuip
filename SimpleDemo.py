import quip
client = quip.QuipClient(access_token="ZE5CQU1BcmtwRnQ=|1600850712|2bH//fDrlft1cx03ktiYFA9kfST9arohKRuPd+WmL4k=")
user = client.get_authenticated_user()
starred = client.get_folder(user["starred_folder_id"])
print "There are", len(starred["children"]), "items in your starred folder"
