import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student ID number
student_id = 23001152

# Load datasets based on the last digit of the student ID
last_digit = student_id % 10
dataset_2020 = f"2020input{last_digit}.csv"
dataset_2024 = f"2024input{last_digit}.csv"

# Read datasets
data_2020 = pd.read_csv(dataset_2020, delimiter='    ', engine="python",
                        header=None, names=['Xleft', 'Xright', 'Count'])

data_2024 = pd.read_csv(dataset_2024, header=None, names=['Grade'])

# Calculate mean values and standard deviations for 2020 distribution
mean_2020 = np.sum((data_2020['Xleft'] + data_2020['Xright']) /
                   2 * data_2020['Count']) / np.sum(data_2020['Count'])
std_2020 = np.sqrt(np.sum(((data_2020['Xleft'] + data_2020['Xright']) /
                   2 - mean_2020) ** 2 * data_2020['Count']) / np.sum(data_2020['Count']))

# Calculate mean and standard deviation for 2024 distribution
mean_2024 = np.mean(data_2024['Grade'])
std_2024 = np.std(data_2024['Grade'])

# Calculate 'V' value (proportion of students with grade below 25 in 2024 exam)
v_value = np.sum(data_2024['Grade'] < 25) / len(data_2024['Grade'])

# Create histograms
plt.figure(figsize=(10, 6))

# Histogram for 2020
plt.bar((data_2020['Xleft'] + data_2020['Xright']) / 2, data_2020['Count'],
        width=data_2020['Xright'] - data_2020['Xleft'], alpha=0.7,
        label=f'2020 Exam Grades\nMean: {mean_2020:.2f}, SD: {std_2020:.2f}', color='blue')

# Histogram for 2024
plt.hist(data_2024['Grade'], bins=20, alpha=0.7,
         label=f'2024 Exam Grades\nMean: {mean_2024:.2f}, SD: {std_2024:.2f}', color='orange')

# Set plot labels and title
plt.xlabel('Exam Grades')
plt.ylabel('Number of Students')
plt.title('Exam Grade Distributions (2020 and 2024)')

# legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1),
           labels=[f'2020 Exam Grades\nMean: {mean_2020:.2f}, SD: {std_2020:.2f}',
                   f'2024 Exam Grades\nMean: {mean_2024:.2f}, SD: {std_2024:.2f}\nV: {v_value:.2f}'])

# Save the plot as a PNG image
plt.savefig(f'{student_id}.png', bbox_inches='tight')

# Display the plot
plt.show()
