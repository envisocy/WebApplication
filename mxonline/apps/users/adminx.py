# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'envisocy'
__date__ = '2018/8/7 20:50'

import xadmin

from .models import *

# xadmin.site.unregister(UserProfile)		# 解除绑定
#
#
# class UserProfileAdmin(object):
# 	list_display = ["nick_name", "birthday", "gender", "address", "mobile", "image"]
# 	search_fileds = ["nick_name", "birthday", "gender", "address", "mobile", "image"]
# 	list_filter = ["nick_name", "birthday", "gender", "address", "mobile", "image"]

class EmailVerifyRecordAdmin(object):
	list_display = ["code", "email", "send_type", "send_time"]
	search_fields = ["code", "email", "send_type"]
	list_filter = ["code", "email", "send_type", "send_time"]

class BannerAdmin(object):
	list_display = ["title", "image", "url", "index", "add_time"]
	search_fields = ["title", "image", "url", "index"]
	list_filter = ["title", "image", "url", "index", "add_time"]

# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

from xadmin import views

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
	site_title = "慕学后台管理系统"
	site_footer = "慕学在线网"
	menu_style = "accordion"            # 左侧列表可折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)