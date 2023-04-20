from django.apps import AppConfig
import sqlite3

class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='post';")
        table_exists = cursor.fetchone() is not None
        if not table_exists:
            conn.execute('''CREATE TABLE post
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER NOT NULL,
                        content TEXT NOT NULL,
                        datetime TEXT NOT NULL);''')
            conn.execute("INSERT INTO post (userid, content, datetime) VALUES ('1', '''春日已至，大街小巷百花盛开，让京城热闹不已。而此时，就在不远的北京山野，又有哪些傲骨凌然、气质绝佳的植物正在绽放花朵？你关注过崖壁上的精灵槭叶铁线莲的绝佳美貌吗？你看到过隐居在大树里的“小象“么？你尝试过有画笔记录大自然的美妙瞬间么？这个春天，和博物旅行一起走进云峰山，做一名植物侦探，探寻和记录春日风光。与此同时，我们还将带大家藏身树屋，住进童话世界。在清晨闻花香做瑜伽，疗愈身心；在下午一起读书朗诵，分享春天；在夜晚仰望星空，点亮心灯...''', '2023-04-11 15:13:22')")
            conn.execute("INSERT INTO post (userid, content, datetime) VALUES ('2', '''明天上午9:30，与地理君一同奔赴澳大利亚追日食。此次混合日食，将在东南亚和大洋洲的部分地区可见，陆地上能看到此次日全食的仅有三个地方，即西澳大利亚的埃克斯茅斯半岛、东帝汶和印尼的部分地区。我国仅东南沿海、南海及诸岛可见食分在0.2~0.5的日偏食。混合日食，也叫日全环食，是除日偏食、日环食、日全食之外的最为罕见的第四种日食，也是集合前三种日食在不同地区同时上演的奇观。据统计，每个世纪平均发生日偏食82.5次，日环食82.2次，日全食67.2次，而混合日食仅有4.8次，是难得一见的天文盛宴！''', '2023-04-21 9:13:22')")
            conn.execute("INSERT INTO post (userid, content, datetime) VALUES ('3', '''饮食是人类基本的生活需要，由此产生的生活美学，是考察一个民族历史文化的源泉。自古以来，中国先民不仅创造了琳琅满目的美味佳肴，更涵养了底蕴深厚的美食文化，其中蕴含的生活美学深深影响着中国人的日常生活，展现了中国古代文明的独特魅力。无论是美食命名、食材选择，还是烹调方法、饮食礼制等方面，古代饮食都呈现出别具一格的美学特征，其中诸多审美观念及其实践对现代饮食生活提供了有益的借鉴与启示。''', '2023-04-13 8:23:22')")
            
            conn.execute('''CREATE TABLE focus
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER NOT NULL,
                        focusid INTEGER NOT NULL);''')
            conn.execute("INSERT INTO focus (userid, focusid) VALUES ('1', '2')")
            conn.execute("INSERT INTO focus (userid, focusid) VALUES ('1', '3')")
            
            
            
            
            
            conn.commit()
            
        conn.close()