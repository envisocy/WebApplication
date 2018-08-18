# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'envisocy'
__date__ = '2018/8/7 21:41'

import xadmin

from .models import *


class CourseAdmin(object):
	list_display = ["name", "desc", "detail", "degree", "learn_time", "student", "fav_number", "image", "click_nums", "add_time"]
	search_fields = ["name", "desc", "detail", "degree", "learn_time", "student", "fav_number", "image", "click_nums"]
	list_filter = ["name", "desc", "detail", "degree", "learn_time", "student", "fav_number", "image", "click_nums", "add_time"]


class LessonAdmin(object):
	list_display = ["course", "name", "add_time"]
	search_fields = ["course", "name"]
	list_filter = ["course", "name", "add_time"]

class VideoAdmin(object):
	list_display = ["lesson", "name", "add_time"]
	search_fields = ["lesson", "name", "add_time"]
	list_filter = ["lesson", "name", "add_time"]

class CourseResourceAdmin(object):
	list_display = ["course", "name", "download", "add_time"]
	search_fields = ["course", "name", "download", "add_time"]
	list_filter = ["course", "name", "download", "add_time"]

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
