import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GermanMania")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

# Fonts
title_font = pygame.font.SysFont("comicsansms", 60)
section_font = pygame.font.SysFont("arial", 40)
text_font = pygame.font.SysFont("verdana", 28)

# Background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(LIGHT_BLUE)

# Content
sections = [
    ("Welcome to GermanMania", "This app will help you learn German in a fun and interactive way!"),
    ("Basic Words", ["Hello - Hallo", "coffee - Kaffee", "water - Wasser", "please - bitte", "thank you - danke", "yes - ja", "no - nein", "milk - Milch", "bread - Brot", "cheese - Käse", "beer - Bier", "wine - Wein", "juice - Saft"]),
    ("Intermediate Words", ["friend - Freund", "family - Familie", "school - Schule", "work - Arbeit", "city - Stadt", "country - Land", "car - Auto", "bicycle - Fahrrad", "book - Buch", "music - Musik", "movie - Film", "computer - Computer", "phone - Telefon", "table - Tisch"]),
    ("Advanced Words", ["environment - Umwelt", "development - Entwicklung", "technology - Technologie", "education - Bildung", "government - Regierung", "community - Gemeinschaft", "opportunity - Gelegenheit", "responsibility - Verantwortung", "achievement - Leistung", "challenge - Herausforderung", "solution - Lösung", "innovation - Innovation", "sustainability - Nachhaltigkeit"]),
    ("Basic Sentences", ["kaffee oder tee? - coffee or tea?", "Bier bitte - beer please", "wasser und brot - water and bread", "danke schön - thank you very much", "ja, ich möchte - yes, I would like", "nein, danke - no, thank you", "ich hätte gern - I would like to have", "milch und käse - milk and cheese", "ein glas wein - a glass of wine", "ein saft, bitte - a juice, please", "ich mag musik - I like music"]),
    ("Intermediate Sentences", ["Wie geht's? - How are you?", "Ich heiße... - My name is...", "Ich komme aus... - I come from...", "Ich spreche ein bisschen Deutsch - I speak a little German", "Können Sie das bitte wiederholen? - Can you please repeat that?", "Sprechen Sie Englisch? - Do you speak English?", "Wo ist die Toilette? - Where is the bathroom?", "Wie viel kostet das? - How much does that cost?", "Ich hätte gern... - I would like...", "Können Sie mir helfen? - Can you help me?", "Ich verstehe nicht - I don't understand", "Was empfehlen Sie? - What do you recommend?", "Ich bin hungrig - I am hungry", "Ich bin durstig - I am thirsty"]),
    ("Advanced Sentences", ["Wie geht es Ihnen? - How are you?", "Könnten Sie das bitte wiederholen? - Could you please repeat that?", "Ich habe eine Frage - I have a question", "Können Sie mir helfen? - Can you help me?", "Ich verstehe nicht - I don't understand", "Was empfehlen Sie? - What do you recommend?", "Ich bin hungrig - I am hungry", "Ich bin durstig - I am thirsty", "Können Sie das bitte langsamer sprechen? - Can you please speak more slowly?", "Wo ist die nächste U-Bahn-Station? - Where is the nearest subway station?", "Wie komme ich zum Flughafen? - How do I get to the airport?", "Ich hätte gern einen Tisch für zwei Personen - I would like a table for two people", "Könnten Sie mir die Speisekarte bringen? - Could you bring me the menu?", "Die Rechnung, bitte - The bill, please"])
]

# Animation variables
clock = pygame.time.Clock()
section_index = 0
line_index = 0
line_delay = 30
frame_count = 0

def draw_section(title, lines):
    screen.blit(background, (0, 0))
    title_surface = title_font.render(title, True, GOLD)
    screen.blit(title_surface, (WIDTH//2 - title_surface.get_width()//2, 50))

    for i, line in enumerate(lines[:line_index]):
        line_surface = text_font.render(line, True, BLACK)
        screen.blit(line_surface, (80, 150 + i * 40))

    pygame.display.update()

# Main loop
running = True
while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if section_index < len(sections):
        title, content = sections[section_index]
        if isinstance(content, str):
            draw_section(title, [content])
            if frame_count > 180:
                section_index += 1
                frame_count = 0
        else:
            draw_section(title, content)
            if frame_count % line_delay == 0 and line_index < len(content):
                line_index += 1
            if line_index == len(content) and frame_count > len(content) * line_delay + 120:
                section_index += 1
                line_index = 0
                frame_count = 0
    else:
        screen.fill(WHITE)
        end_text = section_font.render("🎉 You're ready to speak German! 🎉", True, BLACK)
        screen.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2))
        pygame.display.update()

pygame.quit()
sys.exit()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GermanMania")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

# Fonts
title_font = pygame.font.SysFont("comicsansms", 60)
section_font = pygame.font.SysFont("arial", 40)
text_font = pygame.font.SysFont("verdana", 28)

# Background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(LIGHT_BLUE)

# Content
sections = [
    ("Welcome to GermanMania", "This app will help you learn German in a fun and interactive way!"),
    ("Basic Words", ["Hello - Hallo", "coffee - Kaffee", "water - Wasser", "please - bitte", "thank you - danke", "yes - ja", "no - nein", "milk - Milch", "bread - Brot", "cheese - Käse", "beer - Bier", "wine - Wein", "juice - Saft"]),
    ("Intermediate Words", ["friend - Freund", "family - Familie", "school - Schule", "work - Arbeit", "city - Stadt", "country - Land", "car - Auto", "bicycle - Fahrrad", "book - Buch", "music - Musik", "movie - Film", "computer - Computer", "phone - Telefon", "table - Tisch"]),
    ("Advanced Words", ["environment - Umwelt", "development - Entwicklung", "technology - Technologie", "education - Bildung", "government - Regierung", "community - Gemeinschaft", "opportunity - Gelegenheit", "responsibility - Verantwortung", "achievement - Leistung", "challenge - Herausforderung", "solution - Lösung", "innovation - Innovation", "sustainability - Nachhaltigkeit"]),
    ("Basic Sentences", ["kaffee oder tee? - coffee or tea?", "Bier bitte - beer please", "wasser und brot - water and bread", "danke schön - thank you very much", "ja, ich möchte - yes, I would like", "nein, danke - no, thank you", "ich hätte gern - I would like to have", "milch und käse - milk and cheese", "ein glas wein - a glass of wine", "ein saft, bitte - a juice, please", "ich mag musik - I like music"]),
    ("Intermediate Sentences", ["Wie geht's? - How are you?", "Ich heiße... - My name is...", "Ich komme aus... - I come from...", "Ich spreche ein bisschen Deutsch - I speak a little German", "Können Sie das bitte wiederholen? - Can you please repeat that?", "Sprechen Sie Englisch? - Do you speak English?", "Wo ist die Toilette? - Where is the bathroom?", "Wie viel kostet das? - How much does that cost?", "Ich hätte gern... - I would like...", "Können Sie mir helfen? - Can you help me?", "Ich verstehe nicht - I don't understand", "Was empfehlen Sie? - What do you recommend?", "Ich bin hungrig - I am hungry", "Ich bin durstig - I am thirsty"]),
    ("Advanced Sentences", ["Wie geht es Ihnen? - How are you?", "Könnten Sie das bitte wiederholen? - Could you please repeat that?", "Ich habe eine Frage - I have a question", "Können Sie mir helfen? - Can you help me?", "Ich verstehe nicht - I don't understand", "Was empfehlen Sie? - What do you recommend?", "Ich bin hungrig - I am hungry", "Ich bin durstig - I am thirsty", "Können Sie das bitte langsamer sprechen? - Can you please speak more slowly?", "Wo ist die nächste U-Bahn-Station? - Where is the nearest subway station?", "Wie komme ich zum Flughafen? - How do I get to the airport?", "Ich hätte gern einen Tisch für zwei Personen - I would like a table for two people", "Könnten Sie mir die Speisekarte bringen? - Could you bring me the menu?", "Die Rechnung, bitte - The bill, please"])
]

# Animation variables
clock = pygame.time.Clock()
section_index = 0
line_index = 0
line_delay = 30
frame_count = 0

def draw_section(title, lines):
    screen.blit(background, (0, 0))
    title_surface = title_font.render(title, True, GOLD)
    screen.blit(title_surface, (WIDTH//2 - title_surface.get_width()//2, 50))

    for i, line in enumerate(lines[:line_index]):
        line_surface = text_font.render(line, True, BLACK)
        screen.blit(line_surface, (80, 150 + i * 40))

    pygame.display.update()

# Main loop
running = True
while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if section_index < len(sections):
        title, content = sections[section_index]
        if isinstance(content, str):
            draw_section(title, [content])
            if frame_count > 180:
                section_index += 1
                frame_count = 0
        else:
            draw_section(title, content)
            if frame_count % line_delay == 0 and line_index < len(content):
                line_index += 1
            if line_index == len(content) and frame_count > len(content) * line_delay + 120:
                section_index += 1
                line_index = 0
                frame_count = 0
    else:
        screen.fill(WHITE)
        end_text = section_font.render("🎉 You're ready to speak German! 🎉", True, BLACK)
        screen.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2))
        pygame.display.update()

pygame.quit()
sys.exit()