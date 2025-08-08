import curses
import random
import time

def draw_nokia_frame(stdscr, sh, sw, score):
    """Draw the Nokia phone frame around the game area"""
    try:
        # Clear the screen first
        stdscr.clear()
        
        # Calculate phone dimensions
        phone_width = min(sw - 4, 50)
        phone_height = min(sh - 6, 25)
        start_x = (sw - phone_width) // 2
        start_y = (sh - phone_height) // 2
        
        # Draw phone body outline
        for y in range(start_y - 3, start_y + phone_height + 3):
            for x in range(start_x - 2, start_x + phone_width + 2):
                if y < 0 or y >= sh or x < 0 or x >= sw:
                    continue
                    
                # Phone body border
                if (y == start_y - 3 and x == start_x - 2):
                    stdscr.addch(y, x, '╭')
                elif (y == start_y - 3 and x == start_x + phone_width + 1):
                    stdscr.addch(y, x, '╮')
                elif (y == start_y + phone_height + 2 and x == start_x - 2):
                    stdscr.addch(y, x, '╰')
                elif (y == start_y + phone_height + 2 and x == start_x + phone_width + 1):
                    stdscr.addch(y, x, '╯')
                elif (y == start_y - 3 or y == start_y + phone_height + 2):
                    stdscr.addch(y, x, '─')
                elif (x == start_x - 2 or x == start_x + phone_width + 1):
                    stdscr.addch(y, x, '│')
        
        # Draw "NOKIA" brand at top
        nokia_text = "NOKIA 3310"
        try:
            stdscr.addstr(start_y - 2, start_x + (phone_width - len(nokia_text)) // 2, nokia_text)
        except curses.error:
            pass
        
        # Calculate screen area
        screen_start_y = start_y + 1
        screen_start_x = start_x + 2
        screen_width = phone_width - 4
        screen_height = phone_height - 8
        
        # Draw screen border
        for y in range(screen_start_y - 1, screen_start_y + screen_height + 1):
            for x in range(screen_start_x - 1, screen_start_x + screen_width + 1):
                if y < 0 or y >= sh or x < 0 or x >= sw:
                    continue
                    
                if (y == screen_start_y - 1 and x == screen_start_x - 1):
                    stdscr.addch(y, x, '┌')
                elif (y == screen_start_y - 1 and x == screen_start_x + screen_width):
                    stdscr.addch(y, x, '┐')
                elif (y == screen_start_y + screen_height and x == screen_start_x - 1):
                    stdscr.addch(y, x, '└')
                elif (y == screen_start_y + screen_height and x == screen_start_x + screen_width):
                    stdscr.addch(y, x, '┘')
                elif (y == screen_start_y - 1 or y == screen_start_y + screen_height):
                    stdscr.addch(y, x, '─')
                elif (x == screen_start_x - 1 or x == screen_start_x + screen_width):
                    stdscr.addch(y, x, '│')
        
        # Draw keypad buttons below screen
        button_start_y = screen_start_y + screen_height + 2
        buttons = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]
        
        for row, button_row in enumerate(buttons):
            for col, button in enumerate(button_row):
                btn_y = button_start_y + row
                btn_x = start_x + 5 + col * 4
                if btn_y < sh and btn_x < sw:
                    try:
                        stdscr.addstr(btn_y, btn_x, f'[{button}]')
                    except curses.error:
                        pass
        
        # Draw navigation buttons
        try:
            nav_y = button_start_y - 2
            stdscr.addstr(nav_y, start_x + 3, "Menu")
            stdscr.addstr(nav_y, start_x + phone_width - 7, "Exit")
            # Draw center button (OK)
            stdscr.addstr(nav_y + 1, start_x + phone_width // 2 - 1, "OK")
        except curses.error:
            pass
        
        # Draw score at the top of the screen area
        try:
            score_text = f"Score: {score}"
            stdscr.addstr(screen_start_y, screen_start_x + 1, score_text)
        except curses.error:
            pass
            
        return screen_start_x, screen_start_y + 1, screen_width, screen_height - 1
        
    except curses.error:
        # Fallback to simple display
        return 5, 5, sw - 10, sh - 10

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)       # Food
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Snake
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)     # Text
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)    # Nokia brand
    
    # Set up the window
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Don't wait for input
    stdscr.timeout(120) # Game speed (lower = faster)
    
    sh, sw = stdscr.getmaxyx()
    
    # Game variables
    score = 0
    
    # Draw Nokia phone frame and get game area
    game_area_x, game_area_y, game_area_width, game_area_height = draw_nokia_frame(stdscr, sh, sw, score)

    # Create game window area
    if game_area_width < 10 or game_area_height < 8:
        stdscr.clear()
        stdscr.addstr(0, 0, "Terminal too small! Need more space!")
        stdscr.refresh()
        stdscr.getch()
        return

    # Initialize snake in the game area
    mid_x = game_area_x + game_area_width // 2
    mid_y = game_area_y + game_area_height // 2
    
    snake = [
        [mid_y, mid_x],
        [mid_y, mid_x - 1],
        [mid_y, mid_x - 2]
    ]
    
    # Initial direction (right)
    direction = [0, 1]
    
    # Create food within the game area
    def generate_food():
        while True:
            food_y = random.randint(game_area_y, game_area_y + game_area_height - 1)
            food_x = random.randint(game_area_x, game_area_x + game_area_width - 1)
            if [food_y, food_x] not in snake:
                return [food_y, food_x]
    
    food = generate_food()
    
    # Game loop
    while True:
        # Redraw Nokia frame with updated score
        draw_nokia_frame(stdscr, sh, sw, score)
        
        # Draw food
        try:
            stdscr.addch(food[0], food[1], '●', curses.color_pair(1))
        except curses.error:
            try:
                stdscr.addch(food[0], food[1], '*')
            except curses.error:
                pass
        
        # Draw snake
        for i, segment in enumerate(snake):
            try:
                if i == 0:  # Head
                    stdscr.addch(segment[0], segment[1], '█', curses.color_pair(2))
                else:  # Body
                    stdscr.addch(segment[0], segment[1], '▓', curses.color_pair(2))
            except curses.error:
                try:
                    # Fallback characters
                    if i == 0:
                        stdscr.addch(segment[0], segment[1], 'O')
                    else:
                        stdscr.addch(segment[0], segment[1], 'o')
                except curses.error:
                    pass
        
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()
        
        # Handle direction changes (prevent 180-degree turns)
        if key == curses.KEY_UP and direction != [1, 0]:
            direction = [-1, 0]
        elif key == curses.KEY_DOWN and direction != [-1, 0]:
            direction = [1, 0]
        elif key == curses.KEY_LEFT and direction != [0, 1]:
            direction = [0, -1]
        elif key == curses.KEY_RIGHT and direction != [0, -1]:
            direction = [0, 1]
        elif key == ord('q'):  # Quit game
            break
        
        # Calculate new head position
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
        
        # Check collision with game area boundaries
        if (new_head[0] < game_area_y or new_head[0] >= game_area_y + game_area_height or 
            new_head[1] < game_area_x or new_head[1] >= game_area_x + game_area_width):
            break
        
        # Check collision with itself
        if new_head in snake:
            break
        
        # Add new head
        snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == food:
            score += 1
            food = generate_food()
        else:
            # Remove tail if no food eaten
            snake.pop()
    
    # Game over screen within Nokia frame
    draw_nokia_frame(stdscr, sh, sw, score)
    
    try:
        game_over_text = "GAME OVER!"
        final_score_text = f"Final Score: {score}"
        restart_text = "Press any key to exit"
        
        # Display game over in the screen area
        center_y = game_area_y + game_area_height // 2
        center_x = game_area_x + game_area_width // 2
        
        stdscr.addstr(center_y - 1, center_x - len(game_over_text) // 2, game_over_text, curses.color_pair(1))
        stdscr.addstr(center_y, center_x - len(final_score_text) // 2, final_score_text, curses.color_pair(3))
        stdscr.addstr(center_y + 1, center_x - len(restart_text) // 2, restart_text, curses.color_pair(3))
    except curses.error:
        try:
            # Simple fallback
            stdscr.addstr(2, 2, f"Game Over! Score: {score}. Press any key to exit.")
        except curses.error:
            pass
    
    stdscr.refresh()
    stdscr.nodelay(0)  # Wait for input
    stdscr.getch()

def show_instructions():
    print("\n" + "="*50)
    print("🐍 NOKIA 3310 SNAKE GAME 🐍")
    print("="*50)
    print("\nYou are about to play Snake on a virtual Nokia 3310!")
    print("\nControls:")
    print("  ↑ ↓ ← → : Move the snake")
    print("  q : Quit game")
    print("\nObjective:")
    print("  • Eat the red food (●) to grow and increase your score")
    print("  • Avoid hitting the walls or yourself")
    print("  • Try to beat your high score!")
    print("\nFeatures:")
    print("  • Authentic Nokia 3310 design")
    print("  • Classic monochrome display simulation")
    print("  • Retro gaming experience in your terminal")
    print("\n" + "="*50)
    print("Press Enter to start your nostalgic journey...")
    input()

if __name__ == "__main__":
    show_instructions()
    curses.wrapper(main)
