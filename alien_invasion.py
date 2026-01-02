import sys
import pygame
from ship import Ship
from bullet import Bullet
from settings import Settings
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        #设置屏幕尺寸
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #设置飞船
        self.ship = Ship(self)#调用实例
        #设置子弹编组
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self.check_events()#检查事件，如按键和鼠标事件
            self.update_screen()#更新屏幕
            self.bullets.update()#更新子弹位置
            self.ship.update()#更新飞船位置
            self._update_bullets()#删除已消失的子弹
            self.clock.tick(60)
            

    #更新子弹位置
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    #开火，创建一颗子弹，并将其加入编组
    def _fire_bullet(self):
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
           

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()