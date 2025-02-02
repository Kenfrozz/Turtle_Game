import turtle
import random
import math
import time

# ---------------------------
# Oyun Parametreleri ve Global Değişkenler
# ---------------------------
GAME_DURATION = 60         # Oyun süresi (saniye)
MAX_TURTLES = 5            # Ekranda aynı anda bulunan kaplumbağa sayısı

score = 0                  # Başlangıç skoru
game_active = True         # Oyunun devam edip etmediğini kontrol eder
active_turtles = []        # Aktif kaplumbağa nesnelerini tutar
start_time = None          # Oyun başlangıç zamanı

# ---------------------------
# Ekran ve Yazı Nesnelerinin Ayarlanması
# ---------------------------
screen = turtle.Screen()
screen.title("Kaplumbağa Yakalama Oyunu")
screen.setup(width=800, height=600)  # Pencere boyutunu ayarlayabilirsiniz

# Skor ve zaman bilgisini gösterecek kalemler (pen)
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
# Ekranın sol üst köşesine yerleştiriyoruz:
score_pen.goto(-screen.window_width()//2 + 20, screen.window_height()//2 - 40)

timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
# Ekranın üst ortasına yerleştiriyoruz:
timer_pen.goto(0, screen.window_height()//2 - 40)

def update_score():
    """Skoru ekranda günceller."""
    score_pen.clear()
    score_pen.write(f"Skor: {score}", align="left", font=("Arial", 16, "normal"))

def update_timer():
    """Zamanı ekranda günceller; süre bittiğinde oyunu sonlandırır."""
    global game_active
    if not game_active:
        return
    elapsed = time.time() - start_time
    remaining = GAME_DURATION - elapsed
    timer_pen.clear()
    timer_pen.write(f"Zaman: {int(remaining)}", align="center", font=("Arial", 16, "normal"))
    if remaining > 0:
        # Her saniye güncelle
        screen.ontimer(update_timer, 1000)
    else:
        game_active = False
        end_game()

def end_game():
    """Oyun bittiğinde kaplumbağaları durdurur ve final skoru gösterir."""
    # Aktif tüm kaplumbağaları gizle
    for sprite in active_turtles:
        sprite.t.hideturtle()
    score_pen.clear()
    timer_pen.clear()
    final_pen = turtle.Turtle()
    final_pen.hideturtle()
    final_pen.penup()
    final_pen.goto(0, 0)
    final_pen.write(f"Oyunu Bitirdiniz!\nFinal Skor: {score}", align="center", font=("Arial", 24, "bold"))

def spawn_new_turtle():
    """Yeni bir kaplumbağa oluşturur (oyun aktifse)."""
    if not game_active:
        return
    sprite = TurtleSprite()
    active_turtles.append(sprite)

# ---------------------------
# Kaplumbağa Sınıfı
# ---------------------------
class TurtleSprite:
    def __init__(self):
        # Kaplumbağa nesnesini oluştur
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.penup()
        self.alive = True

        # Rastgele başlangıç konumu (pencere sınırları içinde)
        self.start_x = random.randint(-300, 300)
        self.start_y = random.randint(-250, 250)
        self.t.goto(self.start_x, self.start_y)

        # Rastgele hedef konumu belirle
        self.target_x = random.randint(-300, 300)
        self.target_y = random.randint(-250, 250)

        # Hedefe doğru yönü hesapla
        angle = math.degrees(math.atan2(self.target_y - self.start_y, self.target_x - self.start_x))
        self.t.setheading(angle)

        # Hareket hızı (her güncellemede ilerleyecek mesafe)
        self.speed = random.uniform(2, 6)

        # Kaplumbağaya tıklanma olayını bağla
        self.t.onclick(self.catch)

        # Hareketi başlat
        self.move()

    def move(self):
        """Kaplumbağayı belirlenen hıza göre hareket ettirir ve hedefe ulaştığında 'kaçmış' olarak işler."""
        if not game_active or not self.alive:
            return
        self.t.forward(self.speed)
        current_x, current_y = self.t.position()
        # Hedefe kalan mesafeyi hesapla
        distance = math.hypot(self.target_x - current_x, self.target_y - current_y)
        if distance < self.speed:
            self.miss()
        else:
            # Yaklaşık 50 ms sonra tekrar hareket ettir
            screen.ontimer(self.move, 50)

    def miss(self):
        """Kaplumbağa hedefe ulaşırsa; skoru -1 yapar ve yerine yeni kaplumbağa doğar."""
        global score
        if self.alive:
            self.alive = False
            self.t.hideturtle()
            score -= 1
            update_score()
            spawn_new_turtle()

    def catch(self, x, y):
        """Kaplumbağa tıklanırsa; skoru +1 yapar ve yerine yeni kaplumbağa doğar."""
        global score
        if self.alive and game_active:
            self.alive = False
            self.t.hideturtle()
            score += 1
            update_score()
            spawn_new_turtle()

# ---------------------------
# Oyun Başlatma Fonksiyonu
# ---------------------------
def start_game():
    global start_time
    start_time = time.time()
    update_score()
    update_timer()

    # İlk kaplumbağaları oluştur
    for _ in range(MAX_TURTLES):
        spawn_new_turtle()

    # Turtle döngüsünü başlat (ekranı kapalı tutar)
    turtle.mainloop()

# ---------------------------
# Oyunu Başlat
# ---------------------------
start_game()
