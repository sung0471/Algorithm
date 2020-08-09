# 해시/베스트 앨범

def solution(genres, plays):
    music_dict = dict()
    music_idx = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in music_dict:
            music_dict[genre] = [play]
            music_idx[genre] = [i]
        else:
            music_dict[genre] += [play]
            music_idx[genre] += [i]

    for genre in music_dict.keys():
        music_dict[genre].append(sum(music_dict[genre]))

    sorted_dict = sorted(music_dict.items(), key=lambda x: x[1][-1], reverse=True)
    print(sorted_dict)

    answer = list()
    for key, play_list in sorted_dict:
        sorted_play_list = sorted(play_list[:-1], reverse=True)
        temp_play = sorted_play_list[:2] if len(sorted_play_list) >= 2 else [sorted_play_list[0]]
        temp_idx = list()
        for play in temp_play:
            temp = play_list.index(play)
            if temp not in temp_idx:
                temp_idx.append(temp)
            else:
                temp = play_list.index(play, temp + 1, len(play_list))
                temp_idx.append(temp)
            answer.append(music_idx[key][temp_idx[-1]])

    return answer
