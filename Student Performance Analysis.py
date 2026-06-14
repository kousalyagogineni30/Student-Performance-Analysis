import pandas as pd
df = pd.read_csv("student.csv")
df.columns = df.columns.str.strip()
print(df)
df["Total"] = df["Maths"] + df["Science"] + df["English"] + df["Telugu"]
df["Average"] = df["Total"] / 4
print("\nStudent Performance:")
print(df)
topper = df.loc[df["Total"].idxmax()]
print("\nTop performer:")
print(topper)
lowest_student = df.loc[df["Total"].idxmin()]
print("\nLowest Performer:")
print(lowest_student)
df["Rank"] = df["Total"].rank(ascending=False)
print("\nStudent Rankings:")
print(df[["Name","Total", "Rank"]])
print("\nSubject Averages:")
print("Maths Average:", df["Maths"].mean())
print("Science Average:", df["Science"].mean())
print("English Average:", df["English"].mean())
print("Telugu Average:", df["Telugu"].mean())
import matplotlib.pyplot as plt
plt.bar(df["Name"], df["Total"])
plt.xlabel("students")
plt.ylabel("Total Marks")
plt.title("Student Total Marks")
plt.show()
subject_totals = [df["Maths"].sum(),df["Science"].sum(),df["English"].sum(),df["Telugu"].sum()]
subjects = ["Maths","Science","English","Telugu"]
plt.pie(subject_totals,labels=subjects, autopct="%1.1f%%")
plt.title("subject-wise Marks Distribution")
plt.show()

