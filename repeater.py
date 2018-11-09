# -- coding utf-8 --

messageDict = {}
RepeatedMessageDict ={}

def onQQMessage(bot, contact, member, content):
	if(not bot.isMe(contact, member)):
		uid = contact.ctype + contact.name
		if(not messageDict.__contains__(uid)):
			messageDict[uid]=[content,]
		else:
			messageDict[uid].append(content)
		if(len(messageDict[uid]) > 10):
			messageDict[uid].pop(0)
		if(not RepeatedMessageDict.__contains__(uid)):
			RepeatedMessageDict[uid]=['',]
		if(messageDict[uid].count(content) > 1) and (RepeatedMessageDict[uid].count(content) == 0):
			bot.SendTo(contact, content)
			RepeatedMessageDict[uid].append(content)
			if(len(RepeatedMessageDict[uid]) > 3):
				RepeatedMessageDict[uid].pop(0)