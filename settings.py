class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width  = 1000
        self.screen_height = 600
        self.bg_color      = (230, 230, 230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed  = 2
        self.bullet_width  = 3
        self.bullet_height = 15
        self.bullet_color  = (60, 60, 60)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction 为 1 表示右移，为 -1 表示左移
        self.fleet_direction = 1