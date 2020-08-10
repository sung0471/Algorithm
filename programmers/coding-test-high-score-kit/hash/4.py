# 해시/베스트 앨범

def solution(genres, plays):
    music_dict = dict()
    music_idx = dict()
    # genre를 key로 하여, play 시간 리스트를 저장하는 dict 사용
    # 각 play 시간값이 위치한 idx를 저장하는 dict 저장
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in music_dict:
            music_dict[genre] = [play]
            music_idx[genre] = [i]
        else:
            music_dict[genre] += [play]
            music_idx[genre] += [i]

    # 각 장르별 play 시간 합을 끝에 저장
    for genre in music_dict.keys():
        music_dict[genre].append(sum(music_dict[genre]))

    # 각 genre 별 play 시간의 합이 제일 큰 순서대로 정렬
    sorted_dict = sorted(music_dict.items(), key=lambda x: x[1][-1], reverse=True)
    print(sorted_dict)

    answer = list()
    for key, play_list in sorted_dict:
        sorted_play_list = sorted(play_list[:-1], reverse=True)     # 특정 장르의 play 시간을 내림차순으로 정렬
        # 제일 큰 2개를 뽑음 / 리스트가 1개면 1개만 뽑음
        temp_play = sorted_play_list[:2] if len(sorted_play_list) >= 2 else [sorted_play_list[0]]
        temp_idx = list()
        for play in temp_play:
            temp = play_list.index(play)    # 위에서 제일 큰 두 play time의 index를 각각 구함
            if temp not in temp_idx:    # 저장
                temp_idx.append(temp)
            else:                       # 만약 중복되어 있으면, 이미 뽑은 index 이후로 검색하여 저장
                temp = play_list.index(play, temp + 1, len(play_list))  # play_time이 있는 위치를 저장
                temp_idx.append(temp)
            answer.append(music_idx[key][temp_idx[-1]])     # 위에서 구한 위치에 있는 index를 저장

    return answer

# 불필요한 index 변수가 사용된 것 같음
# 수정 가능함

#   지연님, 상원님
#   music 정보 저장하는 dict
#   music 합을 저장하는 dict
#   정렬 시에 (-로)하면 큰 수 정렬

#   민기님
#   합, 장르 리스트, 인덱스
