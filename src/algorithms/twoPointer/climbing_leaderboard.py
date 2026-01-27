"""
Problem: Climbing Leaderboard
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

def climbing_leaderboard(ranked: list[int], players: list[int]) -> list[int]:
    # Remove duplicates and build unique ranks
    unique_ranked = []
    for score in ranked:
        if not unique_ranked or score != unique_ranked[-1]:
            unique_ranked.append(score)
    
    answer = []
    rank_idx = len(unique_ranked) - 1  # Start from lowest rank
    
    # Process players in ascending order
    for player_score in players:
        # Move pointer up while player score is higher
        while rank_idx >= 0 and player_score >= unique_ranked[rank_idx]:
            rank_idx -= 1
        
        answer.append(rank_idx + 2)  # +2 because: 0-indexed + next rank
    
    return answer
