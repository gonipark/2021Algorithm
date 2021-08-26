from datetime import datetime

def changecode(music_):
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')
    return music_

def solution(m, musicinfos):
    answer = []
    for index, music in enumerate(musicinfos):
        start_time, end_time, title, song = music.split(',')
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")
        h,mi,s=str(end_time - start_time).split(':')
        play_time = int(h)*60+int(mi)
        # print(play_time)

        song = changecode(song)
        m=changecode(m)

        played_music = ['0'] * play_time
        temp=len(song)
        for i in range(play_time):
            if i < len(song):
                played_music[i] = song[i]
            else:
                played_music[i] = song[i - len(song)*(temp//len(song))]
                #print(i - len(song)*(temp//len(song)))
                temp += 1

        answer.append([title,play_time,''.join(played_music)])

    answer.sort(key=lambda x:x[1],reverse=True)
    # print(answer)
    # print(m)
    for song in answer:
        if m in song[2]:
            return song[0]

    return "(None)"

print(solution("CC#BCC#BCC#BCC#B",	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))