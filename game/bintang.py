import tkinter as tk
import random

# Konstanta untuk ukuran kanvas dan kontrol permainan
WIDTH = 600
HEIGHT = 400
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
STAR_SIZE = 20

class CatchTheStarsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch The Falling Stars")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="darkblue")
        self.canvas.pack()
        
        self.basket = self.canvas.create_rectangle(
            WIDTH // 2 - BASKET_WIDTH // 2, HEIGHT - BASKET_HEIGHT - 10, 
            WIDTH // 2 + BASKET_WIDTH // 2, HEIGHT - 10, 
            fill="orange"
        )
        
        self.stars = []
        self.score = 0
        self.missed_stars = 0
        
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 16), text=f"Score: {self.score}")
        
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        
        self.running = True
        self.generate_star()  # Memulai pembuatan bintang pertama
        self.move_stars()  # Memulai pergerakan bintang
    
    def generate_star(self):
        """Menghasilkan bintang pada posisi acak di bagian atas kanvas."""
        x = random.randint(0, WIDTH - STAR_SIZE)
        star = self.canvas.create_oval(x, 0, x + STAR_SIZE, STAR_SIZE, fill="yellow", outline="")
        self.stars.append(star)
        if self.running:
            self.root.after(1500, self.generate_star)  # Membuat bintang baru setiap 1,5 detik
    
    def move_left(self, event):
        if self.canvas.coords(self.basket)[0] > 0:
            self.canvas.move(self.basket, -20, 0)
    
    def move_right(self, event):
        if self.canvas.coords(self.basket)[2] < WIDTH:
            self.canvas.move(self.basket, 20, 0)
    
    def move_stars(self):
        """Menggerakkan semua bintang ke bawah."""
        if not self.running:
            return
        
        for star in self.stars:
            self.canvas.move(star, 0, 5)  # Kecepatan jatuh bintang
            star_coords = self.canvas.coords(star)
            
            # Periksa jika bintang melewati bagian bawah layar
            if star_coords[3] >= HEIGHT:
                self.missed_stars += 1
                self.canvas.delete(star)
                self.stars.remove(star)
                if self.missed_stars >= 5:  # Jika terlalu banyak bintang yang terlewat
                    self.game_over()
                    return
            
            # Periksa tabrakan dengan keranjang
            if self.check_collision(self.basket, star_coords):
                self.score += 1
                self.canvas.delete(star)
                self.stars.remove(star)
                self.update_score()
        
        self.root.after(50, self.move_stars)  # Memanggil fungsi ini setiap 50ms
    
    def check_collision(self, obj, star_coords):
        """Memeriksa apakah bintang bertabrakan dengan keranjang."""
        obj_coords = self.canvas.coords(obj)
        return (star_coords[2] >= obj_coords[0] and star_coords[0] <= obj_coords[2] and
                star_coords[3] >= obj_coords[1] and star_coords[1] <= obj_coords[3])
    
    def update_score(self):
        """Memperbarui skor di layar."""
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
    
    def game_over(self):
        """Mengakhiri permainan dan menampilkan pesan 'Game Over'."""
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))
        
if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheStarsGame(root)
    root.mainloop()
