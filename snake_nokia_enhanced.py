#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nokia 3310 Snake Xenzia - Enhanced Edition
A nostalgic recreation with authentic boot sequence and enhanced visuals
"""

import curses
import random
import time
import sys
import os
from datetime import datetime

class Nokia3310:
    def __init__(self):
        self.high_score = 0
        self.current_score = 0
        self.game_speed = 150
        
    def boot_sequence(self, stdscr):
        """Authentic Nokia 3310 boot sequence"""
        curses.curs_set(0)
        stdscr.clear()
        sh, sw = stdscr.getmaxyx()
        
        # Initialize colors for boot
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        
        # Phase 1: Blank screen
        stdscr.clear()
        stdscr.refresh()
        time.sleep(1)
        
        # Phase 2: Nokia logo animation
        nokia_logo = [
            "    ███    █  █████  █  █  █████   █████",
            "    █  █   █  █   █  █ █      █    █   █",
            "    █   █  █  █   █  ██       █    █████",
            "    █  █   █  █   █  █ █      █    █   █",
            "    ███    █  █████  █  █  █████   █   █"
        ]
        
        # Animate Nokia logo appearing
        for i, line in enumerate(nokia_logo):
            try:
                y_pos = sh//2 - 3 + i
                x_pos = (sw - len(line)) // 2
                if y_pos >= 0 and y_pos < sh and x_pos >= 0:
                    stdscr.addstr(y_pos, x_pos, line, curses.color_pair(2) | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(0.3)
            except curses.error:
                pass
        
        time.sleep(1)
        
        # Phase 3: "Connecting to network" simulation
        status_messages = [
            "Starting up...",
            "Loading system...",
            "Connecting to network",
            "Searching for network.",
            "Searching for network..",
            "Searching for network...",
            "Network found: Nostalgia Net",
            "Signal strength: ████████",
            "Ready!"
        ]
        
        for msg in status_messages:
            try:
                stdscr.clear()
                # Redraw Nokia logo
                for i, line in enumerate(nokia_logo):
                    y_pos = sh//2 - 5 + i
                    x_pos = (sw - len(line)) // 2
                    if y_pos >= 0 and y_pos < sh and x_pos >= 0:
                        stdscr.addstr(y_pos, x_pos, line, curses.color_pair(2) | curses.A_BOLD)
                
                # Show status message
                status_y = sh//2 + 3
                status_x = (sw - len(msg)) // 2
                if status_y >= 0 and status_y < sh and status_x >= 0:
                    stdscr.addstr(status_y, status_x, msg, curses.color_pair(3))
                
                stdscr.refresh()
                time.sleep(0.5 if "network" in msg.lower() else 0.8)
            except curses.error:
                pass
        
        time.sleep(1)
        
        # Phase 4: Show Nokia 3310 welcome screen
        stdscr.clear()
        welcome_art = [
            "╭─────────────────────────────────────╮",
            "│                                     │",
            "│           ███    ██████████         │",
            "│          ██ ██   ██        ██       │",
            "│         ██   ██  ██        ██       │",
            "│        ██     ██  ████████████      │",
            "│       ███████████         ██       │",
            "│      ██       ██         ██        │",
            "│     ██         ██  ████████         │",
            "│                                     │",
            "│          N O K I A   3 3 1 0        │",
            "│                                     │",
            "│        🐍 S N A K E   X E N Z I A    │",
            "│                                     │",
            "╰─────────────────────────────────────╯"
        ]
        
        start_y = max(0, (sh - len(welcome_art)) // 2)
        for i, line in enumerate(welcome_art):
            try:
                y_pos = start_y + i
                x_pos = max(0, (sw - len(line)) // 2)
                if y_pos < sh and x_pos < sw:
                    stdscr.addstr(y_pos, x_pos, line, curses.color_pair(1) | curses.A_BOLD)
            except curses.error:
                pass
        
        # Add blinking "Press any key" text
        try:
            press_key_text = "Press any key to continue..."
            press_key_y = start_y + len(welcome_art) + 2
            press_key_x = (sw - len(press_key_text)) // 2
            if press_key_y < sh and press_key_x >= 0:
                stdscr.addstr(press_key_y, press_key_x, press_key_text, curses.color_pair(3) | curses.A_BLINK)
        except curses.error:
            pass
        
        stdscr.refresh()
        stdscr.getch()  # Wait for user input
        
    def draw_phone_frame(self, stdscr, sh, sw, score, level=1):
        """Enhanced Nokia 3310 phone frame with more details"""
        try:
            stdscr.clear()
            
            # Phone dimensions
            phone_width = min(sw - 6, 60)
            phone_height = min(sh - 8, 35)
            start_x = max(0, (sw - phone_width) // 2)
            start_y = max(0, (sh - phone_height) // 2)
            
            # Draw phone body with rounded corners
            for y in range(start_y - 4, start_y + phone_height + 4):
                for x in range(start_x - 3, start_x + phone_width + 3):
                    if y < 0 or y >= sh or x < 0 or x >= sw:
                        continue
                    
                    # Phone body design
                    if y == start_y - 4:
                        if x == start_x - 3:
                            stdscr.addch(y, x, '╭')
                        elif x == start_x + phone_width + 2:
                            stdscr.addch(y, x, '╮')
                        else:
                            stdscr.addch(y, x, '─')
                    elif y == start_y + phone_height + 3:
                        if x == start_x - 3:
                            stdscr.addch(y, x, '╰')
                        elif x == start_x + phone_width + 2:
                            stdscr.addch(y, x, '╯')
                        else:
                            stdscr.addch(y, x, '─')
                    elif x == start_x - 3 or x == start_x + phone_width + 2:
                        stdscr.addch(y, x, '│')
            
            # Nokia branding with style
            nokia_brand = "═══ NOKIA 3310 ═══"
            brand_y = start_y - 2
            brand_x = start_x + (phone_width - len(nokia_brand)) // 2
            if brand_y >= 0 and brand_x >= 0:
                try:
                    stdscr.addstr(brand_y, brand_x, nokia_brand, curses.color_pair(4) | curses.A_BOLD)
                except curses.error:
                    pass
            
            # Screen area calculation
            screen_start_y = start_y + 2
            screen_start_x = start_x + 4
            screen_width = phone_width - 8
            screen_height = phone_height - 12
            
            # Draw LCD screen with border
            for y in range(screen_start_y - 1, screen_start_y + screen_height + 1):
                for x in range(screen_start_x - 1, screen_start_x + screen_width + 1):
                    if y < 0 or y >= sh or x < 0 or x >= sw:
                        continue
                    
                    if y == screen_start_y - 1:
                        if x == screen_start_x - 1:
                            stdscr.addch(y, x, '┏')
                        elif x == screen_start_x + screen_width:
                            stdscr.addch(y, x, '┓')
                        else:
                            stdscr.addch(y, x, '━')
                    elif y == screen_start_y + screen_height:
                        if x == screen_start_x - 1:
                            stdscr.addch(y, x, '┗')
                        elif x == screen_start_x + screen_width:
                            stdscr.addch(y, x, '┛')
                        else:
                            stdscr.addch(y, x, '━')
                    elif x == screen_start_x - 1 or x == screen_start_x + screen_width:
                        stdscr.addch(y, x, '┃')
            
            # Enhanced keypad design
            keypad_start_y = screen_start_y + screen_height + 3
            keypad_buttons = [
                ['┌─┐', '┌─┐', '┌─┐'],
                ['│1│', '│2│', '│3│'],
                ['└─┘', '└─┘', '└─┘'],
                ['┌─┐', '┌─┐', '┌─┐'],
                ['│4│', '│5│', '│6│'],
                ['└─┘', '└─┘', '└─┘'],
                ['┌─┐', '┌─┐', '┌─┐'],
                ['│7│', '│8│', '│9│'],
                ['└─┘', '└─┘', '└─┘'],
                ['┌─┐', '┌─┐', '┌─┐'],
                ['│*│', '│0│', '│#│'],
                ['└─┘', '└─┘', '└─┘']
            ]
            
            for row_idx in range(0, len(keypad_buttons), 3):
                for sub_row in range(3):
                    for col in range(3):
                        if row_idx + sub_row < len(keypad_buttons):
                            btn_text = keypad_buttons[row_idx + sub_row][col]
                            btn_y = keypad_start_y + (row_idx // 3) * 4 + sub_row
                            btn_x = start_x + 8 + col * 8
                            if btn_y < sh and btn_x < sw - len(btn_text):
                                try:
                                    stdscr.addstr(btn_y, btn_x, btn_text, curses.color_pair(5))
                                except curses.error:
                                    pass
            
            # Navigation controls
            nav_y = keypad_start_y - 2
            try:
                stdscr.addstr(nav_y, start_x + 2, "◄MENU", curses.color_pair(6))
                stdscr.addstr(nav_y, start_x + phone_width - 8, "EXIT►", curses.color_pair(6))
                # Center navigation button
                stdscr.addstr(nav_y + 1, start_x + phone_width // 2 - 2, "●SEL●", curses.color_pair(6) | curses.A_BOLD)
            except curses.error:
                pass
            
            # Enhanced status bar
            status_line = f"SCORE:{score:04d}  LVL:{level}  HI:{self.high_score:04d}  {datetime.now().strftime('%H:%M')}"
            try:
                stdscr.addstr(screen_start_y, screen_start_x + 1, status_line, curses.color_pair(7) | curses.A_REVERSE)
            except curses.error:
                pass
            
            return screen_start_x, screen_start_y + 1, screen_width, screen_height - 1
            
        except curses.error:
            # Fallback for small terminals
            return 5, 5, sw - 10, sh - 10
    
    def show_game_menu(self, stdscr):
        """Show game selection menu"""
        sh, sw = stdscr.getmaxyx()
        stdscr.clear()
        
        menu_items = [
            "┌─────────────────────────┐",
            "│    🐍 SNAKE XENZIA 🐍    │",
            "├─────────────────────────┤",
            "│  ► New Game             │",
            "│    High Scores          │",
            "│    Settings             │",
            "│    About                │",
            "│    Exit                 │",
            "└─────────────────────────┘",
            "",
            "Use ↑↓ to navigate, ENTER to select"
        ]
        
        start_y = (sh - len(menu_items)) // 2
        selected = 0
        
        while True:
            stdscr.clear()
            
            for i, item in enumerate(menu_items):
                y_pos = start_y + i
                x_pos = (sw - len(item)) // 2
                
                if y_pos >= 0 and y_pos < sh and x_pos >= 0:
                    try:
                        if "New Game" in item and selected == 0:
                            stdscr.addstr(y_pos, x_pos, item, curses.color_pair(3) | curses.A_REVERSE)
                        else:
                            stdscr.addstr(y_pos, x_pos, item, curses.color_pair(1))
                    except curses.error:
                        pass
            
            stdscr.refresh()
            key = stdscr.getch()
            
            if key == ord('\n') or key == ord(' '):
                if selected == 0:  # New Game
                    return True
                else:
                    return False
            elif key == ord('q'):
                return False
    
    def play_game(self, stdscr):
        """Enhanced snake game with better visuals"""
        # Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)   # General text
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Snake
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Food
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)    # Nokia brand
        curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Keypad
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Navigation
        curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)   # Status bar
        curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Special effects
        
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(self.game_speed)
        
        sh, sw = stdscr.getmaxyx()
        
        # Game variables
        self.current_score = 0
        level = 1
        food_eaten = 0
        
        # Get game area from phone frame
        game_area_x, game_area_y, game_area_width, game_area_height = self.draw_phone_frame(
            stdscr, sh, sw, self.current_score, level
        )
        
        if game_area_width < 10 or game_area_height < 8:
            stdscr.clear()
            error_msg = "Terminal too small! Please resize and try again."
            stdscr.addstr(sh//2, (sw - len(error_msg))//2, error_msg, curses.color_pair(3) | curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()
            return
        
        # Initialize snake
        mid_x = game_area_x + game_area_width // 2
        mid_y = game_area_y + game_area_height // 2
        
        snake = [
            [mid_y, mid_x],
            [mid_y, mid_x - 1],
            [mid_y, mid_x - 2]
        ]
        
        direction = [0, 1]  # Moving right
        
        # Enhanced food generation
        def generate_food():
            while True:
                food_y = random.randint(game_area_y, game_area_y + game_area_height - 1)
                food_x = random.randint(game_area_x, game_area_x + game_area_width - 1)
                if [food_y, food_x] not in snake:
                    return [food_y, food_x]
        
        food = generate_food()
        food_blink = 0
        
        # Game loop
        while True:
            # Redraw phone frame with current stats
            self.draw_phone_frame(stdscr, sh, sw, self.current_score, level)
            
            # Enhanced food rendering with blinking effect
            food_blink += 1
            food_char = '●' if food_blink % 6 < 3 else '◉'
            try:
                stdscr.addch(food[0], food[1], food_char, 
                           curses.color_pair(3) | curses.A_BOLD)
            except curses.error:
                try:
                    stdscr.addch(food[0], food[1], '*', curses.color_pair(3))
                except curses.error:
                    pass
            
            # Enhanced snake rendering
            for i, segment in enumerate(snake):
                try:
                    if i == 0:  # Head
                        # Snake head with direction indicator
                        if direction == [-1, 0]:  # Up
                            head_char = '▲'
                        elif direction == [1, 0]:   # Down
                            head_char = '▼'
                        elif direction == [0, -1]:  # Left
                            head_char = '◄'
                        else:  # Right
                            head_char = '►'
                        stdscr.addch(segment[0], segment[1], head_char, 
                                   curses.color_pair(2) | curses.A_BOLD)
                    else:  # Body
                        body_chars = ['█', '▓', '▒', '░']
                        char_index = min(i-1, len(body_chars)-1)
                        stdscr.addch(segment[0], segment[1], body_chars[char_index], 
                                   curses.color_pair(2))
                except curses.error:
                    try:
                        # Fallback characters
                        stdscr.addch(segment[0], segment[1], 'O' if i == 0 else 'o', 
                                   curses.color_pair(2))
                    except curses.error:
                        pass
            
            stdscr.refresh()
            
            # Input handling
            key = stdscr.getch()
            
            if key == curses.KEY_UP and direction != [1, 0]:
                direction = [-1, 0]
            elif key == curses.KEY_DOWN and direction != [-1, 0]:
                direction = [1, 0]
            elif key == curses.KEY_LEFT and direction != [0, 1]:
                direction = [0, -1]
            elif key == curses.KEY_RIGHT and direction != [0, -1]:
                direction = [0, 1]
            elif key == ord('q'):
                break
            elif key == ord('p'):  # Pause
                self.pause_game(stdscr)
            
            # Calculate new head position
            new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
            
            # Collision detection
            if (new_head[0] < game_area_y or new_head[0] >= game_area_y + game_area_height or
                new_head[1] < game_area_x or new_head[1] >= game_area_x + game_area_width):
                break
            
            if new_head in snake:
                break
            
            snake.insert(0, new_head)
            
            # Food consumption
            if new_head == food:
                self.current_score += 10
                food_eaten += 1
                
                # Level progression
                if food_eaten % 5 == 0:
                    level += 1
                    self.game_speed = max(80, self.game_speed - 10)  # Increase speed
                    stdscr.timeout(self.game_speed)
                
                food = generate_food()
                
                # Show score popup
                self.show_score_popup(stdscr, "+10", new_head[0], new_head[1])
            else:
                snake.pop()
        
        # Update high score
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        
        # Game over screen
        self.show_game_over(stdscr, game_area_x, game_area_y, game_area_width, game_area_height)
    
    def show_score_popup(self, stdscr, text, y, x):
        """Show floating score popup"""
        try:
            stdscr.addstr(y-1, x-1, text, curses.color_pair(8) | curses.A_BOLD)
            stdscr.refresh()
        except curses.error:
            pass
    
    def pause_game(self, stdscr):
        """Pause game functionality"""
        sh, sw = stdscr.getmaxyx()
        pause_msg = "GAME PAUSED - Press P to continue"
        
        try:
            stdscr.addstr(sh//2, (sw - len(pause_msg))//2, pause_msg, 
                         curses.color_pair(7) | curses.A_BLINK)
            stdscr.refresh()
        except curses.error:
            pass
        
        while True:
            key = stdscr.getch()
            if key == ord('p') or key == ord('P'):
                break
    
    def show_game_over(self, stdscr, area_x, area_y, area_w, area_h):
        """Enhanced game over screen"""
        sh, sw = stdscr.getmaxyx()
        
        # Game over animation
        game_over_text = "GAME OVER!"
        score_text = f"Your Score: {self.current_score}"
        high_score_text = f"High Score: {self.high_score}"
        
        if self.current_score == self.high_score and self.current_score > 0:
            new_record_text = "🎉 NEW HIGH SCORE! 🎉"
        else:
            new_record_text = ""
        
        restart_text = "Press SPACE to play again, Q to quit"
        
        center_y = area_y + area_h // 2
        center_x = area_x + area_w // 2
        
        # Animate game over screen
        for frame in range(10):
            try:
                # Clear game area
                for y in range(area_y, area_y + area_h):
                    for x in range(area_x, area_x + area_w):
                        if y >= 0 and y < sh and x >= 0 and x < sw:
                            stdscr.addch(y, x, ' ')
                
                # Animated "GAME OVER" text
                if frame >= 3:
                    stdscr.addstr(center_y - 2, center_x - len(game_over_text)//2, 
                                game_over_text, curses.color_pair(3) | curses.A_BOLD)
                
                if frame >= 5:
                    stdscr.addstr(center_y, center_x - len(score_text)//2, 
                                score_text, curses.color_pair(1))
                
                if frame >= 6:
                    stdscr.addstr(center_y + 1, center_x - len(high_score_text)//2, 
                                high_score_text, curses.color_pair(4))
                
                if frame >= 7 and new_record_text:
                    stdscr.addstr(center_y - 3, center_x - len(new_record_text)//2, 
                                new_record_text, curses.color_pair(8) | curses.A_BLINK)
                
                if frame >= 8:
                    stdscr.addstr(center_y + 3, center_x - len(restart_text)//2, 
                                restart_text, curses.color_pair(6))
                
                stdscr.refresh()
                time.sleep(0.2)
                
            except curses.error:
                pass
        
        # Wait for user input
        stdscr.nodelay(0)
        while True:
            key = stdscr.getch()
            if key == ord(' '):
                return True  # Restart game
            elif key == ord('q') or key == ord('Q'):
                return False  # Quit
    
    def run(self, stdscr):
        """Main game runner"""
        # Show boot sequence
        self.boot_sequence(stdscr)
        
        while True:
            # Show menu
            if not self.show_game_menu(stdscr):
                break
            
            # Play game
            self.play_game(stdscr)
            
            # Check if user wants to play again
            if not self.show_game_over(stdscr, 0, 0, 0, 0):
                break

def main():
    """Main entry point"""
    try:
        nokia = Nokia3310()
        curses.wrapper(nokia.run)
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing Nokia 3310 Snake!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure your terminal supports the required characters and colors.")

if __name__ == "__main__":
    # Show intro message
    print("\n" + "="*60)
    print("🐍 NOKIA 3310 SNAKE XENZIA - ENHANCED EDITION 🐍")
    print("="*60)
    print("\nFeatures:")
    print("• Authentic Nokia 3310 boot sequence")
    print("• Enhanced phone frame with detailed keypad")
    print("• Animated snake with directional head")
    print("• Blinking food and score popups")
    print("• Level progression system")
    print("• Pause functionality (Press P)")
    print("• High score tracking")
    print("• Nostalgic Nokia experience")
    print("\nControls:")
    print("• Arrow Keys: Move snake")
    print("• P: Pause/Resume")
    print("• Q: Quit game")
    print("• Space: Restart after game over")
    print("\n" + "="*60)
    print("Starting Nokia 3310 Snake Xenzia...")
    print("Make sure your terminal is large enough for the best experience!")
    print("="*60)
    
    time.sleep(2)
    main()
