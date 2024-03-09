MAX_STUD_NUM = "Max number of students reached"


class MaxStudentsReachedError(Exception):
    def __init__(self, message=MAX_STUD_NUM):
        self.message = message
        super().__init__(self.message)
