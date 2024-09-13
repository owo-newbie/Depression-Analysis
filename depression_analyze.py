import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("depression_data.csv", index_col=0)
#print(df.columns.to_list())

def main():
    while True:
        print("This is a system to show the graphs of a depression csv data (containing people who have depression only).")
        print("1. Depression and Age.")
        print("2. Number of people by Education Level.")
        print("3. Relationship Between Education Level and Employment Status.")
        print("4. Education Level and Income (Employed Only).")
        print("5. Physical Levels and Smoking Status in People Having Depression.")
        print("6. Alcohol Consumption and Substance Abuse History.")
        print("7. Marital Status Counts.")
        print("8. Number of Children Distribution of Married People.")
        print("9. Number of Children Distribution of Married People Who over 50 Ages.")
        print("10. Family Depression History and Personal Mental Illness History.")
        print("11. Exit.")
        user_input = input("Enter a number to show the graph: ")
        
        if user_input.isdigit():
            choice = int(user_input)

            if choice == 1:
                # relationship between depression and age
                age = df["Age"]
                age_counts = age.value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                plt.plot(age_counts.index, age_counts.values, marker='o', linestyle='-')
                plt.title('Depression and Age')
                plt.xlabel('Age')
                plt.ylabel('Depreesion People')
                plt.grid()
                plt.show()

            elif choice == 2:
                # education types number
                education = df["Education Level"]
                education_counts = education.value_counts()
                plt.figure(figsize=(10, 6))
                education_counts.plot(kind='bar')
                plt.title('Number of People by Education Level')
                plt.xlabel('Education Level')
                plt.ylabel('Number of People')
                plt.xticks(rotation=0)
                plt.grid(axis='y')
                plt.show()

            elif choice == 3:
                # relationship between depression and education and employment
                education_employment = df[['Education Level', 'Employment Status']]
                count_education_employment = education_employment.value_counts().unstack().fillna(0)
                count_education_employment.plot(kind='bar', figsize=(10, 6), width=0.8)
                plt.title('Education Level and Employment Status')
                plt.xlabel('Education Level')
                plt.ylabel('Count')
                plt.xticks(rotation=0)
                plt.grid(axis='y')
                plt.legend(title='Employment Status')
                plt.show()

            elif choice == 4:
                # Education Level and Income
                employed_df = df[df['Employment Status'] == 'Employed']
                median_income = employed_df.groupby('Education Level')['Income'].median().sort_values()
                sns.boxplot(data=employed_df, x='Education Level', y='Income', order=median_income.index)
                plt.title('Education Level and Income (Employed Only)')
                plt.grid(axis='y')
                plt.show()

            elif choice == 5:
                # The Count of Physical Levels and Smoking Status in People Having Depression
                physical = df["Physical Activity Level"]
                smoking = df["Smoking Status"]
                plt.hist(physical)
                plt.hist(smoking)
                plt.title('Physical Levels and Smoking Status in People Having Depression')
                plt.xlabel('Physical Level and Smoking Status')
                plt.ylabel('Counts')
                plt.grid(axis='y')
                plt.show()

            elif choice == 6:
                # alcohol and substance
                alcohol_order = ['High', 'Moderate', 'Low']
                grouped_data = df.groupby(['Alcohol Consumption', 'History of Substance Abuse']).size().unstack()
                grouped_data = grouped_data.reindex(alcohol_order)
                grouped_data.plot(kind='bar', width=0.8)
                plt.title('Alcohol Consumption and History of Substance Abuse')
                plt.xlabel('Alcohol Consumption Level')
                plt.ylabel('Number of Individuals')
                plt.legend(title='History of Substance Abuse')
                plt.xticks(rotation=0)
                plt.tight_layout()
                plt.grid(axis='y')
                plt.show()

            elif choice == 7:
                # marital status number
                marital_status_counts = df['Marital Status'].value_counts()
                plt.figure(figsize=(10, 6))
                plt.bar(marital_status_counts.index, marital_status_counts.values)
                plt.title('Marital Status Counts', fontsize=16)
                plt.xlabel('Marital Status', fontsize=14)
                plt.grid(axis='y')
                plt.tight_layout()
                plt.show()

            elif choice == 8:
                # children number of married people
                married_df = df[df['Marital Status'] == 'Married']
                children_counts = married_df['Number of Children'].value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                sns.barplot(x=children_counts.index, y=children_counts.values, palette='viridis')
                plt.title('Number of Children Distribution for Married Individuals', fontsize=16)
                plt.xlabel('Number of Children', fontsize=12)
                plt.ylabel('Frequency', fontsize=12)
                plt.xticks(children_counts.index)
                plt.grid(axis='y')
                plt.tight_layout()
                plt.show()

            elif choice == 9:
                # children number of married people that Age >= 50
                married_df_age_50 = df[(df['Marital Status'] == 'Married') & (df['Age'] >= 50)]
                children_counts_age_50 = married_df_age_50['Number of Children'].value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                sns.barplot(x=children_counts_age_50.index, y=children_counts_age_50.values, palette='viridis')
                plt.title('Number of Children Distribution of Married People Who over 50 Ages', fontsize=16)
                plt.xlabel('Number of Children', fontsize=12)
                plt.ylabel('Frequency', fontsize=12)
                plt.xticks(children_counts_age_50.index)
                plt.grid(axis='y')
                plt.tight_layout()
                plt.show()

            elif choice == 10:
                # relationship between family and illness history
                mental_family = df[['History of Mental Illness', 'Family History of Depression']]
                count_mental_family = mental_family.value_counts().unstack().fillna(0)
                count_mental_family.plot(kind='bar', figsize=(10, 6), width=0.8)
                plt.title('Family Depression History and Personal Mental Illness History')
                plt.xlabel('History of Mental Illness')
                plt.ylabel('Counts')
                plt.xticks(rotation=0)
                plt.grid(axis='y')
                plt.legend(title='Family History of Depression')
                plt.show()

            elif choice == 11:
                print("Exiting...")
                break

            else:
                print("That's not a valid number. Please try again.")

if __name__ == "__main__":
    main()
