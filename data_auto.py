import os
import shutil

# Define the file types and their corresponding folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar"],
}

def organize_files(directory):
    # Check if the target directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Create folders for each file type
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories and only process files
        if os.path.isfile(file_path):
            file_moved = False
            for folder, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination = os.path.join(directory, folder, filename)
                    shutil.move(file_path, destination)
                    print(f"Moved {filename} to {folder}")
                    file_moved = True
                    break
            
            # If file type doesn't match any folder, move to "Others" folder
            if not file_moved:
                other_folder = os.path.join(directory, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} to Others")
if __name__ == "__main__":
    target_directory = input("Enter the directory you want to organize: ")
    organize_files(target_directory)
    print("File organization complete.")
