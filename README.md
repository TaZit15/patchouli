# patchouli
Your anime librarian


This is a small python project about organizing my anime archive (it should work with every other video archive too).

I just started to learn python (3.7.7) recently, so my code could probably look better, so please tell me how to improve things, thanks.

(Idk if it works on other OS, I use Windows 10)

## Required stuff
- ffprobe.exe added to path

Anime / series have to be sorted in an order like this:
- some root folder
  - Title 1
    - Season 01
      - video files ...
    - Season 02
      - video files ...
    - ...    
  - Title 2
    - Season 01
    - Season 02
    - ...
   - Title ...



### Version 0.1.1
Patchouli can be used from terminal by opening 'patchouli.py'

She's able to
- display commands with 'help!'
- index your anime/video files into a json file
- edit settings like index.json save path and filename
- run in simulation mode (now only usable for simulating index)


#### What's planned:
- comments and documentation
- display stats like 'number of series', 'biggest file'
- display specific stats for a series like audio languages, subtitles
- help renaming folders, etc. to match the folder system described above
- monitor changes to files/folders and refresh the index automatically
- strip the video files of unwanted stuff like foreign subtitles/sound, ... (v0.9)
- after providing a download folder to monitor, automatically sort the files downloaded by your favourite into your archive and update the index (v1.0)
- be able to scrape direct download links from specific sites (v2.0)
