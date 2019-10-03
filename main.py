import time
import vk_api
import getpass

userlogin = getpass.getuser()


print(":--VkToolsBot--:")
print("Welcome, " + (userlogin))
time.sleep(1)
print("Developed by KidChan.")
print("By the way, you should login on VK with a group token or your page.")
time.sleep(1)
print("WARNING! DONT REPORT ME BUGS!!! IS A BETA VERSION OF BOT.")
time.sleep(1)
print("VTB 0.1 (BetaPublicTest)")

types = input("What login type? 1 - Group Token / 2 - Page. ")
if types == "1":

	tokenl = input("Token: ")

	vk = vk_api.VkApi(token=tokenl)
 
	vk._auth_token()

if types == "2":
	number = input("Login: ")
	password = input("Password: ")

	vk_session = vk_api.VkApi(number, password)
	vk_session.auth()
	vk = vk_session.get_api()

while True:
	main = input(">")
	if main == "checkLink":
		firstlink = input("Link: ")
		print(vk.utils.checkLink(url= (firstlink)))
	if main == "help-commands":
		print("All supported commands:\ncheckLink, deleteFromLastShortened, getLastShortenedLinks, getLinkStats, getServerTime, getShortLink, resolveScreenName")
	
	#UTILS

	if main == "deleteFromLastShortened":
		key = input("Key: ")
		print(vk.utils.deleteFromLastShortened(key= (key)))
	if main == "getShortLink":
		url2 = input("Url: ")
		print(vk.utils.getShortLink(url= (url2)))
	if main == "getServerTime":
		print(vk.utils.getServerTime())
	if main == "getLastShortenedLinks":
		count = input("Count: ")
		offset = input("Offset: ")
		print(vk.utils.getLastShortenedLinks(count= (count), offset= (offset)))
	if main == "getLinkStats":
		key1 = input("Key: ")
		extended = input("Extended(Default is 0): ")
		print(vk.utils.getLinkStats(key= (key1), interval= "forever", extended= (extended)))
	if main == "resolveScreenName":
		key3 = input("Key(like ThisIsExample12): ")
		print(vk.utils.resolveScreenName(screen_name= (key3)))

	#SOON NEW...
