import requests
from datetime import datetime

def write_log(log, file="log.txt"):
	print(log)
	i = datetime.now()
	with open("Logs\\" + file, "a", encoding='utf8') as log_write:
		log_write.write("[" + i.strftime('%Y/%m/%d %H:%M:%S') + "]" + " || " + log + "\n")

def GetCollectionDetails(collection,key,appId,indentLevel,collectionLog):
	totalSize = 0
	sortOrderOffset = 1
	spacer = ""

	payload = {"collectioncount":"1", "publishedfileids[0]":collection}
	response = requests.post(url="https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/",
							data=payload)

	collectionItems = response.json()
	collectionDetails = collectionItems["response"]["collectiondetails"][0]["children"]

	for publishedFile in collectionDetails:
		fileId = publishedFile["publishedfileid"]
		sortOrder = publishedFile["sortorder"]
		fileType = publishedFile["filetype"]

		if fileType == 0:
			# is a mod
			itemDetails = GetWorkshopItemDetails(key,fileId,appId)
			if itemDetails[15] == True:
				totalSize += int(itemDetails[1])

				if indentLevel > 0:
					spacer = "  " * indentLevel
				write_log(spacer + "[" + str(sortOrder+sortOrderOffset) + "] - " + "Size [" + str(int(itemDetails[1])/1000000) +" MB] - Title [" + itemDetails[2] + "]", collectionLog)
			else: sortOrderOffset -= 1
		else:
			#is a collection
			totalSize += GetCollectionDetails(fileId,key,appId,indentLevel+1,collectionLog)

	return totalSize

def GetWorkshopItemDetails(key,item,appId):
	#write_log("0: " + key + "\n1: item: " + item + "\n2: appId: " + appId,collectionLog)

	payload = {
		"key"                       : key,
		"publishedfileids[0]"       : item,
		"includetags"               : "true",
		"includeadditionalpreviews" : "true",
		"includechildren"           : "true",
		"includekvtags"             : "true",
		"includevotes"              : "true",
		"short_description"         : "true",
		"includeforsaledata"        : "false",
		"includemetadata"           : "true",
		"return_playtime_stats"     : "0",
		"appid"                     : appId,
		"strip_description_bbcode"  : "true"
	}
	response = requests.get("https://api.steampowered.com/IPublishedFileService/GetDetails/v1/", params=payload)
	workshopItem = response.json()
	workshopItemDetails = workshopItem["response"]["publishedfiledetails"][0]

	try:
		creator = workshopItemDetails["creator"]
		fileSize = workshopItemDetails["file_size"]
		title = workshopItemDetails["title"]
		shortDescription = workshopItemDetails["short_description"]
		timeCreated = workshopItemDetails["time_created"]
		timeUpdated = workshopItemDetails["time_updated"]
		subscriptions = workshopItemDetails["subscriptions"]
		favorited = workshopItemDetails["favorited"]
		lifetimeSubscriptions = workshopItemDetails["lifetime_subscriptions"]
		lfietimeFavorited = workshopItemDetails["lifetime_favorited"]
		views = workshopItemDetails["views"]
		revision = workshopItemDetails["revision"]
		voteScore = workshopItemDetails["vote_data"]["score"]
		votesUp = workshopItemDetails["vote_data"]["votes_up"]
		votesDown = workshopItemDetails["vote_data"]["votes_down"]
	except KeyError as e:
		return ["n/a",0,"n/a","n/a",0,0,0,0,0,0,0,0,0,0,0,False]


	return [
		creator, fileSize, title, shortDescription, timeCreated, timeUpdated,
		subscriptions, favorited, lifetimeSubscriptions, lfietimeFavorited,
		views, revision, voteScore, votesUp, votesDown, True
	]

# EPublishedFileInfoMatchingFileType:
#  0 = workshop item
#  2 = workshop collection

key = input("Enter Steam API Key: ")
appId = input("Enter Steam Game ID: ")
indentLevel = 0

sizes = []
input_url = []
addon_count = 0
with open("F:\\USBBACKUP\\GitHub\\SteamCollectionSizeFinder\\API Version\\Collections.txt", "r", encoding='utf8') as url_file:
	for line in url_file:
		print("On: " + line)
		collection = line[55:-1]
		collectionLog = collection+".txt"
		with open("Logs\\" + collectionLog, "w") as f: f.close()
		size = GetCollectionDetails(collection,key,appId,indentLevel,collectionLog)
		write_log("Total size: " + str(size/1000000) + " MB", collectionLog)


print("Press ENTER to exit...")