# Algorithm:
# Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368

age_years = int(input())
weight_pounds = int(input())
heart_bpm = int(input())
time_minutes = int(input())

calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (heart_bpm * 1.0781) - 75.4991) * time_minutes / 8.368

print(f'Calories: {calories:.2f} calories')
