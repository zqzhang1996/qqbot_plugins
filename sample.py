# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
	if content == '-restart' and bot.isMe(contact, member):
		bot.SendTo(contact, '5秒后重新启动QQ机器人')
		bot.Restart()
	elif content == '举高高':
		bot.SendTo(contact, '放我下来！')
	elif (not bot.isMe(contact, member))and('嘤' in content):
		bot.SendTo(contact, ('@' + (member.name if (contact.ctype != 'buddy') else contact.name) + ' ')+'一拳一个嘤嘤怪')