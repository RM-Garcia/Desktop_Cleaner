import os
import time
import shutil

# Path to desktop & folders for each file type
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []  # any files that don't match above types
}

# Create the folders (if dont exsist)
for folder in folders:
    folder_path = os.path.join(desktop, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Keep track of files that have already been processed
processed_files = set()

def move_files():
    global processed_files
    for filename in os.listdir(desktop):
        src_path = os.path.join(desktop, filename)

        # Skip if it's a directory a hidden file or already processed
        if os.path.isdir(src_path) or filename.startswith('.') or filename in processed_files:
            continue

        # Destination folder based on file extension
        file_extension = os.path.splitext(filename)[1].lower()
        destination_folder = "Others"
        for folder, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = folder
                break

        dest_path = os.path.join(desktop, destination_folder, filename)

        # Move the file if it doesn't already exist at the destination
        if not os.path.exists(dest_path):
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {destination_folder}")
        else:
            print(f"{filename} already exists in {destination_folder}. Skipping...")

        # Mark the file as processed
        processed_files.add(filename)

if __name__ == "__main__":
    try:
        print(f"Watching for changes on {desktop}...")
        while True:
            move_files()
            time.sleep(10)  # Check for new files every 10 seconds
    except KeyboardInterrupt:
        print("Stopping the desktop cleaner.")
