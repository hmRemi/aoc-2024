import os

def create_advent_folders():
    """
    Creates folders for each day (1 to 24) in the current directory.
    """
    for day in range(1, 25):
        day_folder = f"day-{day:02}"
        if not os.path.exists(day_folder):
            os.mkdir(day_folder)
            print(f"Created folder: {day_folder}")
        else:
            print(f"Folder already exists: {day_folder}")

if __name__ == "__main__":
    create_advent_folders()