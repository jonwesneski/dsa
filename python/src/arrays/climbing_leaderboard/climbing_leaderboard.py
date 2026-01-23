"""
Problem: Climbing Leaderboard
Difficulty: Medium
Time Complexity: O(N + M)
Space Complexity: O(N)
"""

def climbing_leaderboard(ranked: list[int], players: list[int]) -> list[int]:
    places = [1]

    for i in range(1, len(ranked)):
        if ranked[i-1] == ranked[i]:
            places.append(places[i-1])
        else:
            places.append(places[i-1]+1)

    answer = []
    for player in players[::-1]:
        answer_found = False
        for i in range(len(ranked)):
            if player >= ranked[i]:
                answer.append(places[i])
                answer_found = True
                break
        if not answer_found:
            answer.append(places[len(ranked)-1]+1)

    return answer[::-1]
