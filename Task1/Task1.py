import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./student/student-mat.csv", sep=";")


print("Columns in dataset:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Shape (rows, columns):", df.shape)

df.fillna(df.median(numeric_only=True), inplace=True)
df.drop_duplicates(inplace=True)

# Step 5: Data Analysis


avg_score = df['G3'].mean()
print("\n1. Average final grade (G3):", avg_score)

high_scorers = df[df['G3'] > 15].shape[0]
print("2. Students scoring above 15 in G3:", high_scorers)

correlation = df['studytime'].corr(df['G3'])
print("3. Correlation between studytime and G3:", correlation)

plt.scatter(df['studytime'], df['G3'], color="blue", alpha=0.6)
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs Final Grade (G3)")
plt.show()


avg_gender_score = df.groupby('sex')['G3'].mean()
print("4. Average G3 by Gender:\n", avg_gender_score)


avg_gender_score.plot(kind='bar', color=['skyblue', 'pink'])
plt.title("Average Final Grade by Gender")
plt.ylabel("Average G3")
plt.xlabel("Gender")
plt.show()
