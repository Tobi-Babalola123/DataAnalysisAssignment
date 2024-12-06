import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with tab as the delimiter
data = pd.read_csv('sales_data.csv', delimiter='\t')

# Print column names to check for issues
print("Column Names:", data.columns)

# Remove any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Print each column name with its index for better debugging
for i, col in enumerate(data.columns):
    print(f"Column {i}: {repr(col)}")

# Check if the required columns exist
if "Category_Column" in data.columns and "Numerical_Column" in data.columns:
    # Group by the cleaned column name and calculate the mean
    avg_values = data.groupby("Category_Column")["Numerical_Column"].mean()
    print(avg_values)

    # Plot average values across categories
    avg_values.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title("Average Value by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Value")
    plt.show()

    # Plot distribution of a numerical column
    plt.figure(figsize=(10, 6))
    plt.hist(data["Numerical_Column"], bins=20, color='orange', edgecolor='black')
    plt.title("Distribution of Numerical Column")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot for the relationship between two numerical columns
    if "Numerical_Column1" in data.columns and "Numerical_Column2" in data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x="Numerical_Column1", y="Numerical_Column2", hue="Category_Column")
        plt.title("Scatter Plot of Column1 vs Column2")
        plt.xlabel("Column1")
        plt.ylabel("Column2")
        plt.legend()
        plt.show()
    else:
        print("One or both of 'Numerical_Column1' and 'Numerical_Column2' are missing.")
else:
    print("One or both of 'Category_Column' and 'Numerical_Column' are missing.")
