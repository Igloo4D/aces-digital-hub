import os
import random

REPO_PATH = "C:/Users/YourUser/Documents/aces-digital-hub"

def enhance_css():
    """Adds a random color scheme improvement to styles.css"""
    css_file = os.path.join(REPO_PATH, "styles.css")
    with open(css_file, "a") as f:
        colors = ["#ff5733", "#33ff57", "#3357ff", "#f3ff33"]
        new_style = f"\nbody {{ background: {random.choice(colors)}; transition: all 0.5s ease-in-out; }}"
        f.write(new_style)
    print("✔ Added AI-generated style changes!")

if __name__ == "__main__":
    enhance_css()
