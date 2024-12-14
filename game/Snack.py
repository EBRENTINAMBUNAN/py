# ===================================================================================
# 🐍 Permainan Ular (Snake Game)
# Proyek ini adalah implementasi sederhana dari 
# permainan Snake klasik menggunakan Python dan Tkinter sebagai antarmuka grafis.

# 🚀 Fitur Utama
# Ular dapat bergerak ke atas, bawah, kiri, atau kanan.
# Pemain dapat mengontrol ular menggunakan tombol panah keyboard.
# Ular bertambah panjang setiap kali memakan makanan.
# Permainan berakhir jika ular menabrak dinding atau tubuhnya sendiri.
# Skor akan ditampilkan di layar setelah permainan selesai.

# made by Ebren Tinambunan
# [github.com/ebrentinambunan]
# ======================================================================================

import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Permainan Ular")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.snake = [(100, 100), (80, 100), (60, 100)]  
        self.food_position = self.generate_food_position()  
        self.direction = 'Right'  
        
        self.running = True  
        self.score = 0  
        
        self.create_objects()  
        
        self.root.bind('<KeyPress>', self.change_direction) 
        
        self.move_snake()  
    
    def create_objects(self):
        """Membuat objek ular dan makanan di kanvas."""
        self.snake_parts = []
        for x, y in self.snake:
            part = self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", outline="")
            self.snake_parts.append(part)
        
        fx, fy = self.food_position
        self.food = self.canvas.create_oval(fx, fy, fx + GRID_SIZE, fy + GRID_SIZE, fill="red", outline="")
    
    def generate_food_position(self):
        """Menghasilkan posisi acak untuk makanan."""
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        return x, y
    
    def move_snake(self):
        """Menggerakkan ular dalam arah yang ditentukan."""
        if not self.running:
            return
        
        head_x, head_y = self.snake[0]
        
        if self.direction == 'Up':
            new_head = (head_x, head_y - GRID_SIZE)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + GRID_SIZE)
        elif self.direction == 'Left':
            new_head = (head_x - GRID_SIZE, head_y)
        elif self.direction == 'Right':
            new_head = (head_x + GRID_SIZE, head_y)
        
        self.snake.insert(0, new_head)  
        
        if new_head == self.food_position:  
            self.score += 1
            self.food_position = self.generate_food_position()
            self.canvas.delete(self.food)
            fx, fy = self.food_position
            self.food = self.canvas.create_oval(fx, fy, fx + GRID_SIZE, fy + GRID_SIZE, fill="red", outline="")
        else:
            tail = self.snake.pop()  
            self.canvas.delete(self.snake_parts.pop())
        
        if (new_head[0] < 0 or new_head[1] < 0 or 
            new_head[0] >= WIDTH or new_head[1] >= HEIGHT or 
            new_head in self.snake[1:]):
            self.game_over()
            return
        
        part = self.canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + GRID_SIZE, new_head[1] + GRID_SIZE, fill="green", outline="")
        self.snake_parts.insert(0, part)
        
        self.root.after(100, self.move_snake) 
    
    def change_direction(self, event):
        """Mengubah arah pergerakan ular berdasarkan input dari keyboard."""
        new_direction = event.keysym
        
        valid_directions = {
            'Up': 'Down',
            'Down': 'Up',
            'Left': 'Right',
            'Right': 'Left'
        }
        
        if new_direction in valid_directions and new_direction != valid_directions[self.direction]:
            self.direction = new_direction
    
    def game_over(self):
        """Menampilkan pesan akhir permainan dan menghentikan permainan."""
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Game Over! Skor Anda: {self.score}", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
