class StudentsInMLOps:
    total_strength = 0

    @classmethod
    def enroll_students(cls, count):
        cls.total_strength += count

    @classmethod
    def drop_students(cls, count):
        cls.total_strength -= count
        if cls.total_strength < 0:
            cls.total_strength = 0

    @classmethod
    def get_total_strength(cls):
        return cls.total_strength

    @classmethod
    def get_class_name(cls):
        return "MLOps"
