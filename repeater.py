# -- coding utf-8 --

messageDict = {}

def onQQMessage(bot, contact, member, content):
	if(not bot.isMe(contact, member)):
		uid = contact.ctype + contact.name
		if(not messageDict.__contains__(uid)):
			messageDict[uid]=[content,]
		else:
			messageDict[uid].append(content)
		if(len(messageDict[uid]) > 10):
			messageDict[uid].pop(0)
		if(messageDict[uid].count(content) > 1):
			bot.SendTo(contact, content)
			while(messageDict[uid].count(content) > 0):
				messageDict[uid].remove(content)