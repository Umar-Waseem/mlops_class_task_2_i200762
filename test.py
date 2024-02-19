from main import StudentsInMLOps 

def test_enroll_students():
    StudentsInMLOps.enroll_students(5)
    assert StudentsInMLOps.get_total_strength() == 5

def test_drop_students():
    StudentsInMLOps.enroll_students(10)
    StudentsInMLOps.drop_students(3)
    assert StudentsInMLOps.get_total_strength() == 12

def test_drop_students_below_zero():
    StudentsInMLOps.enroll_students(5)
    StudentsInMLOps.drop_students(10)
    assert StudentsInMLOps.get_total_strength() == 7
