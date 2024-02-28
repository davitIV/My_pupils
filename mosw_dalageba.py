import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import json

def analyze_mosw_data():
    # Connect to the SQLite database
    connection = sqlite3.connect('mosw')

    # Read data from the "mosw" table
    df = pd.read_sql_query("SELECT * FROM users", connection)

    # Print column names to identify the correct names
    print("Column names in the DataFrame:", df.columns)

    # Define weights for scoring
    weights = {
        'age': 0.3,
        'grade': 0.4,
        'point': 0.7,
    }

    # Check if all required columns are present
    required_columns = ['age', 'grade', 'point']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the DataFrame.")

    total_weight = sum(weights.values())
    norm_weights = {k: v / total_weight for k, v in weights.items()}

    # Calculate the score
    df['Calculated_Score'] = (
            df['age'] * norm_weights['age'] +
            df['grade'] * norm_weights['grade'] +
            df['point'] * norm_weights['point']
    )

    # Filter candidates based on gender
    filtered_df = df[df['gender'].isin(['male', 'female'])]

    if not filtered_df.empty:
        # Sort candidates by calculated score
        sorted_mosw = filtered_df.sort_values(by='Calculated_Score', ascending=False)

        print("Candidates sorted by calculated score:")
        print(sorted_mosw[['name', 'age', 'grade', 'gender', 'point', 'Calculated_Score']])

        # Plotting the bar chart
        plt.bar(sorted_mosw['name'], sorted_mosw['Calculated_Score'], color='skyblue')

        # Adding labels and title
        plt.xlabel('Name')
        plt.ylabel('Calculated Score')
        plt.title('Moswavleebi Scores')

        plt.show()
    else:
        print("No candidates match the criteria.")

    if not filtered_df.empty:
        sorted_mosw_data = sorted_mosw[['name', 'age', 'grade', 'gender', 'point', 'Calculated_Score']].to_dict(orient='records')
        # print(json.dumps(sorted_mosw_data))
    else:
        print("No candidates match the criteria.")

    # Close the database connection
    connection.close()

# Run the analysis if this script is executed
if __name__ == "__main__":
    analyze_mosw_data()
