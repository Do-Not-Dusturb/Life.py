import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Economy Simulator - Slash Commands")
clock = pygame.time.Clock()
FPS = 30

# Colors and font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
font = pygame.font.SysFont(None, 36)

# Starting balance and message variables
balance = 1000
message = ""
msg_timer = 0  # Duration (in seconds) to show the message

# Input text for command entry
input_text = ""

# Define robbery targets with specific success and failure scenarios
robbery_targets = [
    {
        "name": "bank",
        "success_message": "You successfully robbed a bank and got away with ${amount}!",
        "failure_message": "The bank heist failed! You were caught and fined ${amount}.",
        "success_amount": (5000, 10000),  # Range of money gained on success
        "failure_amount": (1000, 5000),   # Range of money lost on failure
        "success_rate": 20                # Success rate in percentage
    },
    {
        "name": "old lady",
        "success_message": "You stole ${amount} from an old lady's purse.",
        "failure_message": "The old lady caught you! You lost ${amount} in embarrassment.",
        "success_amount": (50, 100),
        "failure_amount": (20, 50),
        "success_rate": 80
    },
    {
        "name": "convenience store",
        "success_message": "You held up a convenience store and took ${amount}.",
        "failure_message": "The store clerk fought back! You lost ${amount} in the scuffle.",
        "success_amount": (200, 500),
        "failure_amount": (100, 200),
        "success_rate": 50
    },
    {
        "name": "jewelry store",
        "success_message": "You successfully robbed a jewelry store and escaped with precious gems worth ${amount}!",
        "failure_message": "The jewelry store's silent alarm was triggered! You were apprehended and fined ${amount}.",
        "success_amount": (10000, 20000),
        "failure_amount": (5000, 10000),
        "success_rate": 25
    },
    {
        "name": "art gallery",
        "success_message": "You stealthily stole a valuable painting from the art gallery, selling it for ${amount}.",
        "failure_message": "Security caught you attempting to steal artwork! You were fined ${amount}.",
        "success_amount": (15000, 30000),
        "failure_amount": (7500, 15000),
        "success_rate": 20
    },
    {
        "name": "businessman",
        "success_message": "You mugged a wealthy businessman and took ${amount} from his wallet.",
        "failure_message": "The businessman fought back, and the police arrived! You lost ${amount} in the ensuing chaos.",
        "success_amount": (500, 1500),
        "failure_amount": (250, 500),
        "success_rate": 60
    },
    {
        "name": "carjacking",
        "success_message": "You successfully carjacked a luxury vehicle and sold it for ${amount}.",
        "failure_message": "The car had a tracking device! You were caught and fined ${amount}.",
        "success_amount": (20000, 40000),
        "failure_amount": (10000, 20000),
        "success_rate": 30
    },
    {
        "name": "pickpocketing",
        "success_message": "You deftly pickpocketed tourists, collecting ${amount} in cash.",
        "failure_message": "A tourist noticed your attempt and alerted the police! You were fined ${amount}.",
        "success_amount": (200, 800),
        "failure_amount": (100, 200),
        "success_rate": 70
    },
    {
        "name": "gas station",
        "success_message": "You held up a gas station and took ${amount} from the register.",
        "failure_message": "The clerk activated the alarm! You were caught and fined ${amount}.",
        "success_amount": (1000, 2000),
        "failure_amount": (500, 1000),
        "success_rate": 50
    },
    {
        "name": "home invasion",
        "success_message": "You broke into a wealthy neighborhood home and stole valuables worth ${amount}.",
        "failure_message": "The homeowners were present and called the police! You were fined ${amount}.",
        "success_amount": (5000, 15000),
        "failure_amount": (2500, 5000),
        "success_rate": 40
    }
]

# Economy functions
def work(balance):
    earnings = random.randint(100, 500)
    balance += earnings
    return balance, f"You worked and earned ${earnings}!"

def steal(balance):
    # Randomly select a robbery target
    target = random.choice(robbery_targets)
    success_chance = random.randint(1, 100)
    
    if success_chance <= target["success_rate"]:
        stolen = random.randint(*target["success_amount"])
        balance += stolen
        msg = target["success_message"].replace("${amount}", str(stolen))
    else:
        penalty = random.randint(*target["failure_amount"])
        balance -= penalty
        if balance < 0:
            balance = 0
        msg = target["failure_message"].replace("${amount}", str(penalty))
    
    return balance, msg

def casino(balance, bet=100):
    if bet > balance:
        return balance, "Not enough money for the bet!"
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        balance += bet
        return balance, f"Casino win! Gained ${bet}!"
    else:
        balance -= bet
        return balance, f"Casino loss! Lost ${bet}!"

def draw_text(surface, text, color, x, y):
    img = font.render(text, True, color)
    surface.blit(img, (x, y))

# Main game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000  # Delta time in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # When Enter is pressed, process the input command
            if event.key == pygame.K_RETURN:
                command = input_text.strip().lower()
                if command == "/work":
                    balance, message = work(balance)
                elif command == "/steal":

::contentReference[oaicite:0]{index=0}
 
