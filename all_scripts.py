# 如果要执行的脚本不在django project的根目录下记得修改path
import sys
# sys.path.append("/path")

# 引入django project环境
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banpick.settings.develop')
django.setup()


FIRE = 'fire'
ICE = 'ice'
THUNDER = 'thunder'
WATER = 'water'
GRASS = 'grass'
WIND = 'wind'
ROCK = 'rock'


def main():
    from draft.models import Champion
    all_roles = [
        {
            'no': None,
            'name': '八重神子',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '申鹤',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '云堇',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '荒泷一斗',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '五郎',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '托马',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '珊瑚宫心海',
            'lane': WATER,
        },
        {
            'no': None,
            'name': '雷电将军',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '九条裟罗',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '埃洛伊',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '宵宫',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '早柚',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '神里绫华',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '枫原万叶',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '优菈',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '烟绯',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '罗莎莉亚',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '胡桃',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '魈',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '甘雨',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '阿贝多',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '钟离',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '辛焱',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '达达利亚',
            'lane': WATER,
        },
        {
            'no': None,
            'name': '迪奥娜',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '可莉',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '温迪',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '刻晴',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '莫娜',
            'lane': WATER,
        },
        {
            'no': None,
            'name': '七七',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '迪卢克',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '琴',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '砂糖',
            'lane': WIND,
        },
        {
            'no': None,
            'name': '重云',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '诺艾尔',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '班尼特',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '菲谢尔',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '凝光',
            'lane': ROCK,
        },
        {
            'no': None,
            'name': '行秋',
            'lane': WATER,
        },
        {
            'no': None,
            'name': '北斗',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '香菱',
            'lane': FIRE,
        },
        {
            'no': None,
            'name': '雷泽',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '芭芭拉',
            'lane': WATER,
        },
        {
            'no': None,
            'name': '丽莎',
            'lane': THUNDER,
        },
        {
            'no': None,
            'name': '凯亚',
            'lane': ICE,
        },
        {
            'no': None,
            'name': '安柏',
            'lane': FIRE,
        },
    ]
    for ind, role_detail in enumerate(all_roles):
        print(role_detail)
        Champion(name=role_detail['name'], lane=role_detail['lane'], no=ind if not role_detail.get(
            'no') else role_detail.get('no')).save()


def check_arr():
    def repeat_num(arr):
        arr_dict = {}
        for item in arr:
            if not arr_dict.get(item):
                arr_dict.setdefault(item, 1)
            else:
                arr_dict[item] += 1
        return [k for k,v in arr_dict.items() if v > 1]
    s = '29/27/19/17/12/7/13/35/8/28/14/40/10/10/38/1'
    arr = s.split('/')
    print(repeat_num(arr))

if __name__ == "__main__":
    main()
