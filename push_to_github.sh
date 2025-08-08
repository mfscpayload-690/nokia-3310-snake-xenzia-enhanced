#!/bin/bash

# Script to push Nokia Snake Xenzia Enhanced files to GitHub repository
# Repository: https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git

echo "Setting up Git repository for Nokia 3310 Snake Xenzia Enhanced..."
echo "Repository: https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing new git repository..."
    git init
fi

# Set the correct remote repository
echo "Setting remote repository..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git

# Add all files
echo "Adding all files..."
git add .

# Check if there are any files to commit
if [ -z "$(git status --porcelain)" ]; then
    echo "No changes to commit. Repository might already be up to date."
else
    echo "Committing files..."
    git commit -m "Initial commit: Nokia 3310 Snake Xenzia Enhanced game files
    
    - Complete snake game implementation
    - Enhanced features for Nokia 3310 style gameplay
    - Multiple game modes and difficulty levels
    - High score tracking
    - Sound effects and visual improvements"
fi

# Create and switch to main branch
echo "Setting up main branch..."
git branch -M main

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main

echo "Done! Files have been pushed to https://github.com/mfscpayload-690/nokia-3310-snake-xenzia-enhanced.git"
