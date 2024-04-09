import hashlib
import time
import random

game_memory = bytearray([random.randint(0, 255) for _ in range(1024)])

def calculate_memory_hash():
    game_memory = b"game_memory_snapshot"
    return hashlib.sha256(game_memory).hexdigest()

def validate_memory_integrity(expected_hash): 
    current_hash = calculate_memory_hash()
    return current_hash == expected_hash

def detect_cheats():
    return random.random() < 0.05  # will add this in later

def analyze_behavior():
    return random.random() < 0.1 # will add this in later

def detect_aimbot():
    player_angle = random.uniform(0, 360)
    expected_angle = random.unifrom(0, 360)

    angle_difference = abs(player_angle - expected_angle)
    if angle_difference > 30:
        return True 
    
def detect_bunnyhop():
    # Bunnyhop detection, scans for inhuman rapid spacebar clicking.
    spacebar_press_rate = random.uniform(0, 10) 
    if spacebar_press_rate > 5:
          return True

def main_game_loop():
    expected_memory_hash = "expected_hash_from_server"
    while True:
        if not validate_memory_integrity(expected_memory_hash):
            print("Unauthorized memory modification detected.")
            break
        if detect_cheats():
            print("Cheating detected")
            break
        if detect_aimbot():
            print("Aimbot Detected")
            break
        if detect_bunnyhop():
            print("Bunnyhop script detected.")
            break
        if analyze_behavior():
            print("Suspicious behaivor detected.")
            break
        print("Game is running...")
        time.sleep(1)

if __name__ == "__main__":  
    main_game_loop()
