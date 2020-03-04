# Lyrics
Find the average number of lyrics per song by any artist

Ensure the following python modules are installed before running.

'requests', 'bs4', 'pandas', 'seaborn', 'matplotlib'

Execute program from cmd prompt by these commands;
    
    C:\file\path python alllyrics.py
    
In a linux environment, run from terminal by locating the file or entering the file path and then;

    ./alllyrics.py
    
Or, run from your favourite IDE (recommended for windows users)

Upon executing the script the user will be required to enter the name of a group or an artist

The program will find the url for that artist on lyrics.com, will then subsequently open all song urls for
that artist and parse the html information to leave only the lyric body.

A list containing the number of words per song is created, all integer elements in this list are summed and divided by the
number of songs.

A visualisation will be produced sowing each song, the number of words in that song and the year it was released.

Roughly takes 1-2 mins per 100 songs

Common error is exceeding the max number of url requests over a short period of time, this usually occurs for some artists
with very large discographies, in which case you may need to select another artist.
