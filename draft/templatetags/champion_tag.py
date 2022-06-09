from django import template
from django.utils import timezone
from draft.models import Draft
import re, os, datetime

register = template.Library()


@register.filter
def sp_position(no):
    return -int(no)*82

@register.simple_tag
def player_name(name, no):
    name_list = name.split('//')
    # lane_list = ['[TOP]', '[JG]', '[MID]', '[ADC]', '[SUP]']
    lane_list = ['[角色1]', '[角色2]', '[角色3]', '[角色4]']
    no = int(no)
    return lane_list[no] + name_list[no] if name_list[no] else lane_list[no]

@register.simple_tag
def player_name_eight(name, no):
    print(11111, name, no)
    name_list = name.split('//')
    # lane_list = ['[TOP]', '[JG]', '[MID]', '[ADC]', '[SUP]']
    lane_list = ['[角色1]', '[角色2]', '[角色3]', '[角色4]', '[角色5]', '[角色6]', '[角色7]', '[角色8]']
    no = int(no)
    return lane_list[no] + name_list[no] if name_list[no] else lane_list[no]