#https://leetcode.com/problems/minimum-health-to-beat-game/description/


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        closeness = -9
        tot_damage = sum(damage)
        max_damage = max(damage)
        return tot_damage - min(max_damage, armor) + 1