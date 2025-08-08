# 🐍📱 Nokia 3310 Snake Xenzia - Enhanced Edition

<div align="center">

![Nokia 3310](https://img.shields.io/badge/Nokia-3310-blue?style=for-the-badge&logo=nokia)
![Python](https://img.shields.io/badge/Python-3.6+-yellow?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**🎮 Authentic Nokia 3310 Snake Xenzia recreation with enhanced visuals, nostalgic boot sequence, and immersive terminal experience!**

*Relive the golden age of mobile gaming with pixel-perfect authenticity and modern enhancements*

</div>

---

## 🌟 Features

### 🚀 Enhanced Edition Exclusive:

| Feature | Description |
|---------|-------------|
| 🔄 **Authentic Boot Sequence** | Complete Nokia 3310 startup with logo animation and "Nostalgia Net" connection |
| 🎨 **Enhanced Phone Frame** | Detailed keypad with `┌─┐ │1│ └─┘` button styling and Nokia branding |
| 🐍 **Animated Snake** | Directional head indicators (`▲▼◄►`) and gradient body textures (`█▓▒░`) |
| ✨ **Visual Effects** | Blinking food (`●◉`), floating score popups, celebration animations |
| 🏆 **Level Progression** | Dynamic difficulty scaling - speed increases every 5 foods consumed |
| ⏸️ **Game Controls** | Pause functionality (`P` key), menu navigation, instant restart |
| 📊 **Score System** | Real-time scoring, high score persistence, achievement celebrations |
| 🕰️ **Real-time Clock** | Live time display on phone screen (`HH:MM` format) |
| 🎭 **Interactive Demo** | Feature showcase with typewriter effects and visual previews |
| 🔧 **Smart Launcher** | Auto-detection system with version fallbacks |

### 🎮 Core Gaming Features:

- 📱 **Pixel-perfect Nokia 3310 design** with authentic phone frame
- 🖥️ **Terminal-based graphics** using Unicode box drawing characters  
- 🎯 **Classic snake mechanics** with collision detection and growth system
- 🏁 **Progressive difficulty** with 10+ challenging levels
- 💾 **Cross-platform compatibility** (Linux, macOS, Windows)
- 🎨 **Monochrome aesthetic** true to original Nokia display

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git
cd nokia-3310-snake-xenzia-enhanced

# Run the enhanced version (recommended)
python3 snake_nokia_enhanced.py

# OR use smart launcher
./play_snake.sh

# OR see feature demo first
python3 demo.py
```

---

# �📱 Nokia 3310 Snake Xenzia - Enhanced Edition

<div align="center">

![Nokia 3310](https://img.shields.io/badge/Nokia-3310-blue?style=for-the-badge&logo=nokia)
![Python](https://img.shields.io/badge/Python-3.6+-yellow?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**🎮 Authentic Nokia 3310 Snake Xenzia recreation with enhanced visuals, nostalgic boot sequence, and immersive terminal experience!**

*Relive the golden age of mobile gaming with pixel-perfect authenticity and modern enhancements*

[🚀 Quick Start](#-quick-start) • [🎮 Features](#-features) • [📸 Screenshots](#-preview) • [🛠️ Installation](#️-installation) • [🎯 How to Play](#-how-to-play)

</div>

---

## 🌟 Features

### 🚀 Enhanced Edition Exclusive:

| Feature | Description |
|---------|-------------|
| 🔄 **Authentic Boot Sequence** | Complete Nokia 3310 startup with logo animation and "Nostalgia Net" connection |
| 🎨 **Enhanced Phone Frame** | Detailed keypad with `┌─┐ │1│ └─┘` button styling and Nokia branding |
| 🐍 **Animated Snake** | Directional head indicators (`▲▼◄►`) and gradient body textures (`█▓▒░`) |
| ✨ **Visual Effects** | Blinking food (`●◉`), floating score popups, celebration animations |
| 🏆 **Level Progression** | Dynamic difficulty scaling - speed increases every 5 foods consumed |
| ⏸️ **Game Controls** | Pause functionality (`P` key), menu navigation, instant restart |
| 📊 **Score System** | Real-time scoring, high score persistence, achievement celebrations |
| 🕰️ **Real-time Clock** | Live time display on phone screen (`HH:MM` format) |
| 🎭 **Interactive Demo** | Feature showcase with typewriter effects and visual previews |
| 🔧 **Smart Launcher** | Auto-detection system with version fallbacks |

#### Method 1: Direct Download
```bash
wget -O nokia-snake.zip https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced/archive/main.zip
unzip nokia-snake.zip && cd nokia-3310-snake-xenzia-enhanced-main
chmod +x *.py *.sh
python3 snake_nokia_enhanced.py
```

#### Method 2: Git Clone
```bash
git clone https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git
cd nokia-3310-snake-xenzia-enhanced
chmod +x *.py *.sh
./play_snake.sh
```

### 🐳 Docker Support (Optional)
```dockerfile
# Dockerfile example
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y ncurses-term
CMD ["python3", "snake_nokia_enhanced.py"]
```

---

## 🎯 How to Play

### 🕹️ Game Versions

| Version | Command | Description |
|---------|---------|-------------|
| 🌟 **Enhanced** | `python3 snake_nokia_enhanced.py` | Full Nokia experience with boot sequence |
| 🚀 **Smart Launch** | `./play_snake.sh` | Auto-detects and runs best available version |
| 📱 **Classic Nokia** | `python3 snake_nokia.py` | Original Nokia styling without enhancements |
| 🎮 **Basic** | `python3 snake_game.py` | Minimal snake game implementation |
| 📺 **Demo** | `python3 demo.py` | Interactive feature showcase |

### 🎮 Controls

| Key | Action | Description |
|-----|--------|-------------|
| `↑` `↓` `←` `→` | **Move Snake** | Navigate with precision control |
| `P` | **Pause/Resume** | Strategic planning mode |
| `Q` | **Quit** | Graceful exit with Nokia farewell |
| `Space` | **Restart** | Instant game restart after game over |
| `Enter` | **Select** | Menu navigation and confirmation |

### 🎯 Gameplay Mechanics

#### 📈 Scoring System
- **+10 points** per food consumed
- **Floating score popups** for visual feedback
- **High score persistence** across sessions
- **🎉 Celebration animations** for new records

#### 📊 Level Progression
| Level | Speed | Foods Required | Difficulty |
|-------|-------|----------------|------------|
| 1-2 | Gentle | 0-9 foods | 🟢 Beginner friendly |
| 3-5 | Medium | 10-24 foods | 🟡 Reflex testing |
| 6-8 | Fast | 25-39 foods | 🟠 Nokia veterans only |
| 9+ | Lightning | 40+ foods | 🔴 Legendary status |

#### 🐍 Snake Mechanics
- **Directional head indicators**: Visual movement feedback
- **Gradient body textures**: Realistic snake appearance
- **Smooth collision detection**: Pixel-perfect gameplay
- **No 180° turns**: Authentic Nokia behavior

---

## 📁 Project Structure

```
nokia-3310-snake-xenzia-enhanced/
├── 🐍 snake_nokia_enhanced.py    # Enhanced Nokia Snake (MAIN)
├── 📱 snake_nokia.py             # Classic Nokia version
├── 🎮 snake_game.py              # Basic snake implementation
├── 🚀 play_snake.sh              # Smart launcher script
├── 📺 demo.py                    # Interactive feature demo
├── 📚 README.md                  # This comprehensive guide
├── 📋 .gitignore                 # Git ignore rules
└── 📝 LICENSE                    # MIT License
```

---

## 🔧 Technical Details

### 🏗️ Architecture
- **Object-oriented design** with `Nokia3310` class encapsulation
- **Modular structure** supporting multiple game versions
- **Cross-platform compatibility** using Python `curses` library
- **Unicode rendering** for authentic Nokia aesthetic
- **Error handling** for terminal constraints and encoding issues

### ⚡ Performance
- **Optimized rendering** with minimal screen updates
- **Efficient collision detection** using coordinate comparison
- **Memory conscious** snake growth and food generation
- **Smooth animation** with configurable frame rates

### 🎨 Visual Technology
- **Unicode box drawing** for phone frame construction
- **ANSI color codes** for enhanced visual experience  
- **Cursor manipulation** for smooth animation effects
- **Screen buffer management** for flicker-free updates

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🔧 **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. 💻 **Commit** your changes: `git commit -m 'Add amazing feature'`
4. 📤 **Push** to branch: `git push origin feature/amazing-feature`
5. 🔄 **Open** a Pull Request

### 💡 Feature Ideas
- 🎵 Nokia ringtone sound effects
- 🌐 Multiplayer support
- 📊 Statistics and achievements system
- 🎨 Alternative phone themes (Nokia 1100, 6600, etc.)
- 💾 Save/load game states
- 🏆 Online leaderboard integration

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced/discussions)
- ⭐ **Star the repo** if you enjoyed the nostalgic experience!

---

<div align="center">

### 🎉 Ready to Experience Nostalgia?

**Relive the golden age of mobile gaming!**

```bash
git clone https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git
cd nokia-3310-snake-xenzia-enhanced && python3 snake_nokia_enhanced.py
```

*Made with ❤️ for retro gaming enthusiasts*

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=mfscpayload-690.nokia-3310-snake-xenzia-enhanced)

</div>
