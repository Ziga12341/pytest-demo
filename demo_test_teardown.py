import os
import shutil


def move_files_to_archive(source_dir='data', dest_dir='archive'):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through all files and directories within the source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate the relative path to use for the same structure in the destination
        relative_path = os.path.relpath(root, source_dir)
        dest_path = os.path.join(dest_dir, relative_path)

        # Check if this path exists in the destination, if not, create it
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # Move each file in the current directory to the corresponding new location
        for file in files:
            original_file_path = os.path.join(root, file)
            new_file_path = os.path.join(dest_path, file)

            # Move the file
            shutil.move(original_file_path, new_file_path)

    print("Files have been moved successfully.")


if __name__ == "__main__":
    move_files_to_archive()