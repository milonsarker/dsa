class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        total_move = 0
        for i in range(len(students)):
            total_move += abs(students[i] - seats[i])
        return total_move