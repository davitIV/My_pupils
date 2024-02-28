import sqlite3
import pandas as pd

def insert_new_pupil(name, age, grade, gender, point):


    with sqlite3.connect('mosw') as connection:
        try:
            new_pupil = pd.DataFrame({
                'name': [name],
                'age': [age],
                'grade': [grade],
                'gender': [gender],
                'point': [point]
            })

            new_pupil.to_sql('users', connection, index=False, if_exists='append')

            print("New pupil information inserted successfully.")
        except Exception as e:
            print(f"Error inserting new pupil: {e}")

def mosw_sheyvana():

    name = input("Enter pupil's name: ")
    age = int(input("Enter pupil's age: "))
    grade = int(input("Enter pupil's grade: "))
    gender = input("Enter pupil's gender: ")
    point = float(input("Enter pupil's point: "))

    insert_new_pupil(name, age, grade, gender, point)

if __name__ == "__main__":
    mosw_sheyvana()
