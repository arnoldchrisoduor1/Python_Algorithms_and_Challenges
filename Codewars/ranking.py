
#  ---------------------------- Incomplete ----------------------------------

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def validate_rank(self, rank):
        valid_ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        if rank not in valid_ranks:
            raise ValueError("Invalid rank. Valid ranks are: " + ", ".join(map(str, valid_ranks)))

    def inc_progress(self, activity_rank):
        self.validate_rank(activity_rank)

        rank_diff = activity_rank - self.rank

        if rank_diff == 0:
            progress = 3
        elif rank_diff == -1:
            progress = 1
        elif rank_diff > 0:
            progress = 10 * rank_diff * rank_diff
        else:
            progress = 0

        self.progress += progress

        while self.progress >= 100:
            if self.rank == -1:
                self.rank += 2
            else:
                self.rank += 1

            self.progress -= 100

        if self.rank == 8:
            self.progress = 0  # Progress is capped at 8

        return self.progress
