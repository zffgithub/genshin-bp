from django.urls import path

from . import views

app_name = 'draft'

urlpatterns = [
    #   入口
    path('entry/<str:room_code>', views.draft_entry, name='draft_entry'),
    #   房间
    path('room/<str:room_code>', views.draft_room, name='draft_room'),
    #   房间 生成 结果
    path('result', views.draft_result, name="draft_result"),
    #   禁选 GET / POST 
    path('draft/<str:room_code>', views.draft_draft, name="draft_draft"),
    #   角色 GET / POST
    path('champion', views.draft_champion, name="draft_champion"),
    #   完成选择
    path('lane/<str:room_code>', views.draft_lane, name="draft_lane"),
    #   获取当前时间
    path('now', views.get_timestamp, name="now")
]