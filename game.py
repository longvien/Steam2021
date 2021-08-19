import pygame

class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Kích thước cửa (door) 60 x 60 px
        sprite = pygame.image.load("sprites/door.png")
        self.image = pygame.transform.scale(sprite, (80, 80))

class Robot:
    def __init__(self, x, y, x_heading, y_heading, hinh_anh):
        self.x = x
        self.y = y
        self.x_heading = x_heading
        self.y_heading = y_heading
        # Kích thước Robot 60 x 60 px
        sprite = pygame.image.load(hinh_anh)
        self.image = pygame.transform.scale(sprite, (60, 60))

    def move(self):
        self.x = self.x + self.x_heading
        self.y = self.y + self.y_heading
        
        if self.x > 440: self.x_heading = - self.x_heading
        if self.x < 0:   self.x_heading = - self.x_heading
        if self.y > 440: self.y_heading = - self.y_heading
        if self.y < 0:   self.y_heading = - self.y_heading

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Kích thước trẩu (player) 50 x 80 px
        sprite = pygame.image.load("sprites/trau.png")
        self.image = pygame.transform.scale(sprite, (50, 80))
    
    def move(self, change_x, change_y):
        new_x = self.x + change_x
        new_y = self.y + change_y

        if new_x > 0 and new_x < 450:
            self.x = new_x
        if new_y > 0 and new_y < 420:
            self.y = new_y

    def touch(self, obj):
        mask1 = pygame.mask.from_surface(self.image)
        mask2 = pygame.mask.from_surface(obj.image)
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        if mask1.overlap(mask2, (offset_x, offset_y)):
            return True
        else:
            return False

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 500   # Chiều ngang (W: Width)
        self.HEIGHT = 500  # Chiều dọc   (H: Height)
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])

        self.clock = pygame.time.Clock()
        self.FPS = 30      # Số cảnh mỗi giây (frame per second)
        self.font = pygame.font.SysFont("Times New Roman", 30, bold=True)

    def draw_background(self):
        # Vẽ hình nền
        BLACK = (0, 0, 0)
        self.screen.fill(BLACK)
        background = pygame.image.load("sprites/background.png").convert_alpha()
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(background, (0, 0))
    
    def draw_new_frame(self):
        # Vẽ cảnh mới
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def draw_object(self, obj):
        # Vẽ đối tượng
        self.screen.blit(obj.image, (obj.x, obj.y))

    def draw_result(self, win):
        # Hiện kết quả game

        YELLOW = (255, 255, 0)  # Màu Vàng
        if win:
            text = self.font.render("YOU WON!!", 1, YELLOW)
            self.screen.blit(text, (150, 250))
        else:
            text = self.font.render("YOU LOST!!", 1, YELLOW)
            self.screen.blit(text, (150, 250))

    def is_quit(self):
        # Người chơi có tắt màn hình game chưa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def start(self):
        # -------------- Mình viết code ở đây --------------------- 
        trau = Player(100, 250)
        door = Door(375, 20)

        robots = [
            Robot(100, 400, 5, 0, "sprites/robot1.png"),
            Robot(300, 300, 0, 5, "sprites/robot2.png"),
            Robot(200, 200, 10, 2, "sprites/robot3.png"),
            Robot(100, 100, -2, -5, "sprites/robot4.png")
        ]

        # Game kết thúc chưa
        end_game = False
        # Thắng / Thua
        is_won = False

        running = True
        while running:
            if self.is_quit():
                running = False

            self.draw_background()
            
            if not end_game:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]:    trau.move( 0, -5)
                if pressed[pygame.K_DOWN]:  trau.move( 0,  5)
                if pressed[pygame.K_LEFT]:  trau.move(-5,  0)
                if pressed[pygame.K_RIGHT]: trau.move( 5,  0)

                if trau.touch(door):
                    print("YOU WON!!")
                    end_game = True
                    is_won = True

                for robot in robots:
                    robot.move()

                    if trau.touch(robot):
                        print("YOU LOST!!")
                        end_game = True
                        is_won = False
            
            # Hiển thị vị trí của các đối tượng
            self.draw_object(trau)
            for robot in robots:
                self.draw_object(robot)
            self.draw_object(door)
            
            if end_game:
                # Vẽ chữ thắng / thua
                self.draw_result(is_won)

            # Vẽ cảnh mới
            self.draw_new_frame()
            
        # Kết Thúc Game
        pygame.quit()

#-------------------------------------------------------------------
# Tạo Đối tượng Game, và bắt đầu trò chơi
game = Game()
game.start()

