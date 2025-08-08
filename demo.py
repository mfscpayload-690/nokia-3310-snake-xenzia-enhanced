#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo script showing the enhanced Nokia 3310 Snake features
"""

import time
import sys

def print_slow(text, delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def demo_features():
    """Show demo of enhanced features"""
    print("\n" + "="*70)
    print_slow("🐍 NOKIA 3310 SNAKE XENZIA - ENHANCED EDITION DEMO 🐍")
    print("="*70)
    
    print_slow("\nWelcome to the most nostalgic Snake experience ever created!")
    time.sleep(1)
    
    print_slow("\n🚀 ENHANCED FEATURES SHOWCASE:")
    time.sleep(0.5)
    
    features = [
        ("🔄 Nokia 3310 Boot Sequence", "Experience authentic startup with Nokia logo animation"),
        ("🎨 Enhanced Phone Frame", "Detailed keypad with ┌─┐ │1│ └─┘ button design"),
        ("🐍 Animated Snake Head", "Directional indicators: ▲ Up, ▼ Down, ◄ Left, ► Right"),
        ("✨ Blinking Food Effects", "Alternating ● ◉ symbols for enhanced visibility"),
        ("🏆 Level Progression", "Game speeds up every 5 foods - can you handle level 10?"),
        ("⏸️ Pause Functionality", "Press P anytime to pause and take a nostalgic break"),
        ("📊 Score Popups", "Floating '+10' notifications appear when you eat food"),
        ("🎉 High Score Celebration", "🎉 NEW HIGH SCORE! 🎉 animations with blinking effects"),
        ("🕰️ Real-time Clock", "Shows current time HH:MM on the phone display"),
        ("🌈 Gradient Snake Body", "█ ▓ ▒ ░ textures make your snake look more realistic")
    ]
    
    for i, (feature, description) in enumerate(features, 1):
        print(f"\n{i:2d}. {feature}")
        print_slow(f"    → {description}", 0.03)
        time.sleep(0.3)
    
    time.sleep(1)
    print_slow("\n🎮 ENHANCED CONTROLS:")
    controls = [
        "Arrow Keys (↑↓←→) - Move snake with precision",
        "P - Pause/Resume for strategic planning", 
        "Q - Quit gracefully with Nokia farewell",
        "Space - Restart instantly after game over",
        "Enter - Navigate menus like a true Nokia user"
    ]
    
    for control in controls:
        print_slow(f"   • {control}", 0.03)
        time.sleep(0.2)
    
    time.sleep(1)
    print_slow("\n🎯 GAME PROGRESSION:")
    progression = [
        "Level 1-2: Gentle start, perfect for warming up",
        "Level 3-5: Speed increases, reflexes get tested",
        "Level 6-8: Nokia veterans only, lightning fast!",
        "Level 9+: Legendary status - only true masters survive"
    ]
    
    for prog in progression:
        print_slow(f"   🔥 {prog}", 0.03)
        time.sleep(0.3)
    
    time.sleep(1)
    print_slow("\n📱 AUTHENTIC NOKIA EXPERIENCE:")
    print_slow("   ╭─────────────────────╮")
    print_slow("   │    NOKIA 3310       │")
    print_slow("   ├─────────────────────┤")
    print_slow("   │ ┏━━━━━━━━━━━━━━━━━┓ │")
    print_slow("   │ ┃ SCORE:0000 12:34 ┃ │")
    print_slow("   │ ┃     ►●●●          ┃ │")
    print_slow("   │ ┃        ◉         ┃ │")
    print_slow("   │ ┃                 ┃ │")
    print_slow("   │ ┗━━━━━━━━━━━━━━━━━┛ │")
    print_slow("   │ ◄MENU     ●SEL●  EXIT► │")
    print_slow("   │ ┌─┐ ┌─┐ ┌─┐       │")
    print_slow("   │ │1│ │2│ │3│       │")
    print_slow("   │ └─┘ └─┘ └─┘       │")
    print_slow("   ╰─────────────────────╯")
    
    time.sleep(2)
    print_slow("\n🌟 READY TO EXPERIENCE NOSTALGIA?")
    print_slow("\nRun any of these commands to start:")
    print(f"\n   🚀 {sys.executable} snake_nokia_enhanced.py  (Full Enhanced Experience)")
    print(f"   🎮 ./play_snake.sh                    (Smart Auto-Launch)")
    print(f"   📱 {sys.executable} snake_nokia.py           (Classic Nokia Style)")
    
    print_slow("\n" + "="*70)
    print_slow("🎉 Get ready to relive the golden age of mobile gaming! 🎉")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        demo_features()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Ready to play the real game?")
