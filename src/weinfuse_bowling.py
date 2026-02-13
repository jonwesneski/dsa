from typing import List, Union

def get_frame(frame: List[Union[int, str]], last_frame: bool):
    results = []
    strike_indices = []
    is_spare = False
    for i in range(len(frame)):
        roll = frame[i]
        if roll == 'X':
            results.append(10)
            strike_indices.append(i)
        elif roll == '/':
            results.append(10 - results[(len(results)-1)])
            is_spare = True
        else:
            results.append(roll)

    size = 2 if not last_frame else 3
    if size == 3 and not strike_indices and not is_spare:
        size = 2
    is_complete = len(results) == size
    return results, is_complete, strike_indices, is_spare


def scoring(rolls: List[Union[int, str]]) -> List[int]:
    frames = []
    strikes = {}
    spares = {}
    i = 0
    last_frame = False
    while i < len(rolls) and not last_frame:
        frames.append(None)

        remaining_rolls = len(rolls) - i
        rolls_in_frame =  2 if remaining_rolls >= 2 else remaining_rolls
        last_frame = len(frames) >= 10
        if last_frame and remaining_rolls >= 3:
            rolls_in_frame = 3

        results, is_complete, strike_indices, is_spare = get_frame(rolls[i:i+rolls_in_frame], last_frame)

        current_frame = len(frames)-1
        if strikes:
            for k in list(strikes.keys()):
                ri = 0
                while len(strikes[k]) < 3 and ri < len(results):
                    strikes[k].append(results[ri])
                    ri += 1
                if len(strikes[k]) == 3:
                    frames[k] = sum(strikes[k])
                    del strikes[k]

        if spares:
            k = list(spares.keys())[0]
            spare = spares[k]
            if strike_indices:
                spare.append(10)
            elif not is_complete:
                spare.append(results[0])
            else:
                spare.append(rolls[i])
            frames[k] = sum(spare)
            del spares[k]

        if strike_indices:
            if last_frame and is_complete:
                frames[current_frame] = sum(results)
            else:
                strikes[current_frame] = [results[0]]
                i += 1
        elif is_spare and not last_frame:
            spares[current_frame] = results
            i += 2
        elif results and is_complete:
            frames[current_frame] = sum(results)
            i += rolls_in_frame
        else:
            i+= len(results) if len(results) else 1

    return frames



if __name__ == '__main__':
    test_cases = [
    ([3, 4], [7]),
    ([3, 4, 5, 2], [7, 7]),
    ([0, 0], [0]),
    ([0, 0, 0, 0], [0, 0]),

    # incomplete frames
    ([4], [None]),
    (["X"], [None]),
    (["X", 3], [None, None]),
    ([7, "/"], [None]),
    ([7, "/", 3], [13, None]),


    ([7, "/", 3, 2], [13, 5]),
    # Spare followed by a strike
    ([6, "/", "X"], [20, None]),
    # # Consecutive spares
    ([5, "/", 5, "/", 3], [15, 13, None]),
    ([0, "/", 5, 3], [15, 8]),


    (["X", 3, 4], [17, 7]),
    (["X", "X"], [None, None]),
    (["X", "X", 5], [25, None, None]),
    (["X", "X", 5, 3], [25, 18, 8]),
    (["X", "X", "X"], [30, None, None]),
    (["X", "X", "X", 2], [30, 22, None, None]),
    (["X", "X", "X", 2, 5], [30, 22, 17, 7]),

    ([4, 5, "X", 8], [9, None, None]),
    ([4, 5, "X", 8, 1], [9, 19, 9]),

     # 10 frames
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([1,1, 1,1, 1,1, 1,1, 1,1, 1,1, 1,1, 1,1, 1,1, 1,1],
     [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 5,"/",3],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 13]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 5,"/"],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, None]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, "X",3,4],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 17]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, "X"],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, None]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, "X", 5],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, None]),

    (["X","X","X","X","X","X","X","X","X","X","X","X"],
     [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]),

    (["X", 5, "/", "X", 5, "/", 3, 2],
     [20, 20, 20, 13, 5]),
    ([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, "X", 3,4],
     [0, 0, 0, 0, 0, 0, 0, 0, 17, 7]),
    ([], []),
]
    for test in test_cases:
        actual = scoring(test[0])
        print(actual, str(test[1]), str(actual) == str(test[1]))
