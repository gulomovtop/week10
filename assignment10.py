def categorize_music(track_list):
    music_dictionary = {}
    for track in track_list:
        parts = track.split("-")
        artist = parts[0]
        song_name = parts[1]
        duration = int(parts[2])
        if artist not in music_dictionary:
            music_dictionary[artist] = []
        music_dictionary[artist].append((song_name, duration))
    return music_dictionary
def report_artist_time(music_dict):
    # music_dict=categorize_music(track_list)
    for artist in music_dict:
        total_duration = 0
        for song_name_tuple in music_dict[artist]:
            duration = song_name_tuple[1]
            total_duration+=duration
        print(f'{artist}: {total_duration} seconds total')


track_list = [
    "Taylor Swift-Shake it Off-240",
    "Queen-Bohemian Rhapsody-355",
    "Taylor Swift-Love Story-235",
    "Drake-God's Plan-200",
    "Queen-We Will Rock You-120",
    "Drake-Hotline Bling-260"
]
duration = categorize_music(track_list)
report_artist_time(duration)