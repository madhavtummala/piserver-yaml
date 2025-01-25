import os
import time
import shutil
from torrentool.api import Torrent

def is_video_file(file_name):
    """Check if the file is a video file based on its extension."""
    video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"}
    return os.path.splitext(file_name)[1].lower() in video_extensions

def find_movie_folder(torrent_files, media_base):
    if len(torrent_files) > 2:
        return None
    """Find the movie folder to move the torrent file to."""
    movies_folder = os.path.join(media_base, "movies")
    for movie_folder in os.listdir(movies_folder):
        movie_folder_path = os.path.join(movies_folder, movie_folder)
        if os.path.isdir(movie_folder_path):
            movie_files = set(os.listdir(movie_folder_path))
            if torrent_files & movie_files:
                return movie_folder_path  # Return matched movie folder
    return None

def find_show_folder(torrent_files, media_base):
    """Find the show folder to move the torrent file to."""
    shows_folder = os.path.join(media_base, "tv")
    for show_folder in os.listdir(shows_folder):
        show_folder_path = os.path.join(shows_folder, show_folder)
        if os.path.isdir(show_folder_path):
            matching_seasons = [
                os.path.join(show_folder_path, season_folder)
                for season_folder in os.listdir(show_folder_path)
                if os.path.isdir(os.path.join(show_folder_path, season_folder)) and
                torrent_files & set(os.listdir(os.path.join(show_folder_path, season_folder)))
            ]
            if len(matching_seasons) == 1:
                return matching_seasons[0]  # If exactly one season matched, return that season
            elif matching_seasons:
                return show_folder_path  # If multiple seasons matched, return the show folder itself
    return None

def process_torrents(torrents_base, torrents_bkp, media_base):
    """Process all torrent files in the torrents_base directory."""
    for torrent_file in os.listdir(torrents_base):
        print(f"Processing {torrent_file}...", flush=True)
        torrent_file_path = os.path.join(torrents_base, torrent_file)
        torrent = Torrent.from_file(torrent_file_path)
        torrent_files = {os.path.basename(file.name) for file in torrent.files if is_video_file(file.name)}
        parent_folder = find_movie_folder(torrent_files, media_base) or find_show_folder(torrent_files, media_base) or torrents_bkp
        print(f"Backing up {torrent_file} to {parent_folder}...", flush=True)
        shutil.copy2(torrent_file_path, parent_folder)
        os.remove(torrent_file_path)

if __name__ == "__main__":
    torrents_base = "/downloads/torrents"
    torrents_bkp = "/downloads/torrents-bkp"
    media_base = "/media"

    while True:
        process_torrents(torrents_base, torrents_bkp, media_base)
        time.sleep(3600)