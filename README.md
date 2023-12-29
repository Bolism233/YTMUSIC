# YTMUSIC
## How it works(OLD):
1. Takes Playlist URL
2. Get songs in the playlist
3. Get song name and artist by splitting song Name - Artist
    Limitations: 
        1. Only recognize format: {Artist} - {Song Name} 
        2. Can only recognize songs in lastfm database
4. Obtain the song label/category from lastfm.api?

## HOW IT SUPPOSE TO WORK(NEW)
1. Search for the song and singer in database
2. If not match, fetch every song from that singer into database
3. FuzzyMatch the song in playlist with songs in the database again
4. If hit, search in lastfm; if not, log to console and skip to next song

## Next Step:
1. Cannot find songs from a singer
Current Solution: 
2. Fetch all the song information from that singer and store to database
   1. WIP, need to get page info and loop through
3. Fuzzy match the song name to get the highest similarity
4. Store the song the database
5. Next time, Fuzzy match with databse first, go to api if not found

