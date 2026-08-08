# ============================================
# Day 18 - Program 49
# Topic: Type Hints Practice
# Concepts: basic type hints, List, Dict,
#           Optional, function return types
# ============================================

from typing import List, Dict, Optional


def calculate_total(prices: List[float]) -> float:
    # I add up all the prices in the list.
    return sum(prices)


def calculate_average(marks: List[int]) -> float:
    # I calculate the average of a list of marks.
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def build_student_record(name: str, age: int, marks: List[int]) -> Dict[str, object]:
    # I build a dictionary record for one student.
    return {
        "name": name,
        "age": age,
        "average": calculate_average(marks),
    }


def find_topper(records: List[Dict[str, object]]) -> Optional[Dict[str, object]]:
    # I return the record with the highest average.
    # I return None if the list is empty.
    if not records:
        return None

    topper = records[0]
    for record in records:
        if record["average"] > topper["average"]:
            topper = record
    return topper


def get_grade(marks: int) -> str:
    # I convert numeric marks into a letter grade.
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"


# --- TESTING ---

prices: List[float] = [199.5, 349.0, 89.99]
print(calculate_total(prices))

marks_list: List[int] = [85, 92, 78, 95, 60]
print(calculate_average(marks_list))

record1 = build_student_record("Harshit", 21, [85, 92, 78])
record2 = build_student_record("Priya", 20, [90, 95, 88])
record3 = build_student_record("Rahul", 22, [45, 55, 40])

all_records: List[Dict[str, object]] = [record1, record2, record3]

top = find_topper(all_records)
if top is not None:
    print(f"Topper: {top['name']} with average {top['average']:.2f}")

print(get_grade(85))

empty_list: List[Dict[str, object]] = []
result = find_topper(empty_list)
print(result)   # None


