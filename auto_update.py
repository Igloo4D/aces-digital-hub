import os
import time
import subprocess

# Set up your repo path
REPO_PATH = "C:/Program Files/Ace's Digital Hub"
CHECK_INTERVAL = 30  # Check every 30 seconds

def git_push():
    """Pushes the latest changes to GitHub automatically."""
    os.chdir(REPO_PATH)
    print("\n🚀 Pushing updates to GitHub...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Automated update from AI"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Update successfully pushed to GitHub.")

def watch_files():
    """Watches for file changes and triggers git updates."""
    print("👀 Watching for changes in your website files...\n")
    
    prev_mtime = {}
    while True:
        changed = False

        for root, _, files in os.walk(REPO_PATH):
            for file in files:
                if file.endswith(('.html', '.css', '.js', '.py')):  # Track relevant files
                    filepath = os.path.join(root, file)
                    mtime = os.path.getmtime(filepath)

                    if filepath not in prev_mtime or mtime > prev_mtime[filepath]:
                        prev_mtime[filepath] = mtime
                        print(f"📝 Detected change in: {file}")
                        changed = True

        if changed:
            git_push()

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    watch_files()
