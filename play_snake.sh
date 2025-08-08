#!/bin/bash

# Enhanced Nokia 3310 Snake Xenzia Launcher
echo "🐍 NOKIA 3310 SNAKE XENZIA - ENHANCED EDITION 🐍"
echo "================================================"
echo "Loading nostalgic gaming experience..."
echo ""

# Check if enhanced version exists, otherwise fall back
if [ -f "snake_nokia_enhanced.py" ]; then
    echo "Starting Enhanced Nokia 3310 Snake..."
    python3 snake_nokia_enhanced.py
elif [ -f "snake_nokia.py" ]; then
    echo "Starting Nokia 3310 Snake..."
    python3 snake_nokia.py
else
    echo "Starting Classic Snake..."
    python3 snake_game.py
fi

echo ""
echo "Thanks for playing! 📱🎮"
