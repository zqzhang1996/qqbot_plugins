# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
	if content == '-restart' and bot.isMe(contact, member):
		bot.SendTo(contact, '5秒后重新启动QQ机器人')
		bot.Restart()
	elif content == '举高高':
		bot.SendTo(contact, '放我下来！')
	elif (not bot.isMe(contact, member))and('教练我想学' in content):
		bot.SendTo(contact, '你已经是个成熟的大学生了，应该学会自己使用搜索引擎')
#	elif (not bot.isMe(contact, member))and('嘤' in content):
#		bot.SendTo(contact, ('@' + (member.name if (contact.ctype != 'buddy') else contact.name) + ' ')+'一拳一个嘤嘤怪')
	elif content == '插件开发':
		bot.SendTo(contact, 'GitHub地址：https://github.com/zqzhang1996/qqbot_plugins')
	elif content == 'GitHub教程':
		bot.SendTo(contact, 'http://wiki.jikexueyuan.com/project/github-basics/')
	elif content == 'Python教程':
		bot.SendTo(contact, 'http://www.runoob.com/python/python-tutorial.html')
	elif content == '会长':
		bot.SendTo(contact,'真可爱！')
