#!/bin/python

from difflib import SequenceMatcher
from datetime import datetime
import subprocess
import shutil
import time
import sys
import os
from torrentool.api import Torrent

base = "/media"
movies = base+"/MOVIES"
tv = base+"/TV"
plex= base+"/plex"
movies_links = plex+"/movies"
tv_links = plex+"/tv"
completed_base = base+"/seedbox/complete"
incomplete_base = base+"/seedbox/incomplete"
torrents_base = base+"/seedbox/torrents"
torrents_bkp = base+"/seedbox/torrent-bkp"
seeding_torrents = base+"/seedbox/seeding/torrents"
seeding_data = base+"/seedbox/seeding"

def watch():
    # Link manually added movies
    # movies are added manually, it creates/updates a soft link at plex/movies
    print("checking movies...", flush=True)
    if len(os.listdir(movies)) == 0:
        return
    path = os.walk(movies)
    for root, dirs, files in path:
        for dir in dirs:
            if "(" in dir and ")" in dir:
                movie_dir = root + "/" + dir
                symlink = "../.." + root.split(base)[1] + "/" + dir
                link_dir = movies_links + "/" + dir
                if os.path.exists(link_dir) and os.path.islink(link_dir):
                    continue
                elif os.path.exists(link_dir):
                    print("{} ...updating".format(link_dir), flush=True)
                    shutil.rmtree(movie_dir)
                    shutil.move(link_dir, movie_dir)
                    os.symlink(symlink, link_dir)
                else:
                    print("{} ...creating".format(link_dir), flush=True)
                    os.symlink(symlink, link_dir)

    # Link automatically added movie
    # if movie added at plex/movie, moves and replaces with a soft link to original files
    # the original dir has date, so extracts date from folder name as well
    print("checking movie links...", flush=True)
    links = (link for link in os.listdir(movies_links) if os.path.islink(movies_links+"/"+link))
    for link in links:
        link_dir = os.readlink(movies_links+"/"+link)
        if not os.path.exists(base + link_dir.rpartition("..")[2]):
            print("{} is invalid link".format(link), flush=True)
            os.remove(movies_links+"/"+link)

    dirs = (dir for dir in os.listdir(movies_links) if os.path.isdir(movies_links+"/"+dir) and not os.path.islink(movies_links+"/"+dir))
    for dir in dirs:
        link_dir = movies_links+"/"+dir
        movies_dir = "{}/{}/{}".format(movies, dir.rpartition("(")[2].partition(")")[0], dir)
        try:
            shutil.rmtree(movies_dir)
            print("{} ...overwriting ...linking".format(link_dir), flush=True)
            shutil.move(link_dir, movies_dir)
        except:
            print("{} ...moving ...linking".format(link_dir), flush=True)
            shutil.move(link_dir, movies_dir)
        symlink = "../.." + movies_dir.split(base)[1]
        os.symlink(symlink, link_dir)

    # Link manually added tv shows
    print("checking shows...", flush=True)
    if len(os.listdir(tv)) == 0:
        return
    dirs = (dir for dir in os.listdir(tv) if os.path.isdir(tv+"/"+dir))
    for dir in dirs:
        tv_dir = tv + "/" + dir
        link_dir = tv_links+"/"+dir
        symlink = "../.." + tv.split(base)[1] + "/" + dir
        if os.path.exists(link_dir) and os.path.islink(link_dir):
            continue
        elif os.path.exists(link_dir):
            print("{} ...updating".format(link_dir), flush=True)
            shutil.rmtree(tv_dir)
            shutil.move(link_dir, tv_dir)
            os.symlink(symlink, link_dir)
        else:
            print("{} ...creating".format(link_dir), flush=True)
            os.symlink(symlink, link_dir)

    # Link automatically added tv shows
    print("checking show links...", flush=True)
    links = (link for link in os.listdir(tv_links) if os.path.islink(tv_links+"/"+link))
    for link in links:
        link_dir = os.readlink(tv_links+"/"+link)
        if not os.path.exists(base + link_dir.rpartition("..")[2]):
            print("{} is invalid link".format(link), flush=True)
            os.remove(tv_links+"/"+link)
    dirs = (dir for dir in os.listdir(tv_links) if os.path.isdir(tv_links+"/"+dir) and not os.path.islink(tv_links+"/"+dir))
    for dir in dirs:
        link_dir = tv_links+"/"+dir
        tv_dir = "{}/{}".format(tv, dir)
        try:
            shutil.rmtree(tv_dir)
            print("{} ...overwriting ...linking".format(link_dir), flush=True)
            shutil.move(link_dir, tv_dir)
        except:
            print("{} ...moving ...linking".format(link_dir), flush=True)
            shutil.move(link_dir, tv_dir)
        symlink = "../.." + tv_dir.split(base)[1]
        os.symlink(symlink, link_dir)

    # for completed downloads, creates a soft link to collection and adds to transmission
    print("checking completed downloads...", flush=True)
    for torrent in os.listdir(torrents_base):
        mytorrent = Torrent.from_file(torrents_base+"/"+torrent)
        if os.path.exists(completed_base+"/"+mytorrent.name):
            if os.path.isdir(completed_base+"/"+mytorrent.name):
                all_vid = set([file for file in os.listdir(completed_base+"/"+mytorrent.name) if file.endswith("mp4") or file.endswith("mkv") or file.endswith("avi")])
            elif os.path.isfile(completed_base+"/"+mytorrent.name):
                all_vid = set([mytorrent.name])
            else:
                continue
            links = (link for link in os.listdir(movies_links) if os.path.islink(movies_links+"/"+link))
            for link in links:
                link_dir = movies_links+"/"+link
                link_dest = os.readlink(link_dir)
                movie_dest = base + link_dest.rpartition("..")[2]
                if os.path.exists(movie_dest):
                    files = set(os.listdir(movie_dest))
                    if files & all_vid:
                        if os.path.isdir(completed_base+"/"+mytorrent.name):
                            symlink = "../.."+ link_dir.split(base)[1]
                        else:
                            symlink = "../.."+ link_dir.split(base)[1] + "/" + mytorrent.name
                        try:
                            os.symlink(symlink, seeding_data+"/"+mytorrent.name)
                            print(symlink, " => ", seeding_data+"/"+mytorrent.name, flush=True)
                            shutil.copy(torrents_base+"/"+torrent, movie_dest)
                            shutil.move(torrents_base+"/"+torrent, seeding_torrents+"/"+torrent)
                            break
                        except Exception as e:
                            print(e)
        elif os.path.exists(incomplete_base+"/"+mytorrent.name):
            continue
        else:
            shutil.copy(torrents_base+"/"+torrent, torrents_bkp)
            os.remove(torrents_base+"/"+torrent)

while True:
    # subprocess.run("chmod ugo+rw -R {}/*".format(base), shell=True)
    try:
        watch()
    except Exception as e:
        print(e, flush=True)
    time.sleep(1800)
