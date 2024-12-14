# ===================================================================================
# 🎮 Brick Breaker Game
# Program ini adalah implementasi sederhana dari 
# permainan Brick Breaker menggunakan Python dan Tkinter sebagai antarmuka grafis.

# 🚀 Fitur Utama
# - Pemain mengontrol paddle menggunakan tombol panah kiri dan kanan.
# - Bola bergerak secara otomatis dan memantul dari paddle, dinding, dan bricks.
# - Bricks akan hancur ketika bola mengenainya.
# - Permainan berakhir ketika semua bricks dihancurkan (menang) atau bola jatuh melewati paddle (kalah).
# - Tampilan "Game Over" atau "You Win" akan muncul di layar sesuai hasil permainan.

# made by Ebren Tinambunan
# [github.com/ebrentinambunan]
# ===================================================================================

import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 20

class BrickBreakerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker Game")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.paddle = self.canvas.create_rectangle(
            WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, 
            WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT - 20, 
            fill="blue"
        )
        
        self.ball = self.canvas.create_oval(
            WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, 
            WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2, 
            fill="red"
        )
        
        self.ball_dx = random.choice([-3, 3])
        self.ball_dy = -3
        
        self.create_bricks()
        
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        
        self.running = True
        self.move_ball()
    
    def create_bricks(self):
        self.bricks = []
        rows = 5
        cols = 10
        brick_width = WIDTH // cols
        brick_height = 20
        for row in range(rows):
            for col in range(cols):
                x1 = col * brick_width
                y1 = row * brick_height
                x2 = x1 + brick_width
                y2 = y1 + brick_height
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                self.bricks.append(brick)
    
    def move_left(self, event):
        if self.canvas.coords(self.paddle)[0] > 0:
            self.canvas.move(self.paddle, -20, 0)
    
    def move_right(self, event):
        if self.canvas.coords(self.paddle)[2] < WIDTH:
            self.canvas.move(self.paddle, 20, 0)
    
    def move_ball(self):
        if not self.running:
            return
        
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        
        if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:  
            self.ball_dx *= -1
        
        if ball_coords[1] <= 0:  
            self.ball_dy *= -1
        
        if ball_coords[3] >= HEIGHT:  
            self.game_over()
            return
        
        if self.check_collision(self.paddle, ball_coords):  
            self.ball_dy *= -1
        
        for brick in self.bricks:
            if self.check_collision(brick, ball_coords):  
                self.ball_dy *= -1
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                if not self.bricks:  
                    self.win_game()
                break
        
        self.root.after(20, self.move_ball)
    
    def check_collision(self, obj, ball_coords):
        obj_coords = self.canvas.coords(obj)
        return (ball_coords[2] >= obj_coords[0] and ball_coords[0] <= obj_coords[2] and
                ball_coords[3] >= obj_coords[1] and ball_coords[1] <= obj_coords[3])
    
    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))
    
    def win_game(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="You Win!", fill="yellow", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreakerGame(root)
    root.mainloop()
