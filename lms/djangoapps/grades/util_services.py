"A light weight interface to grading helper functions"


from .grade_utils import are_grades_frozen


class GradesUtilService(object):

    def __init__(self, **kwargs):
        super(GradesUtilService, self).__init__()
        self.course_id = kwargs.get('course_id', None)

    def are_grades_frozen(self):
        "Check if grades are frozen for given course key"
        return are_grades_frozen(self.course_id)
