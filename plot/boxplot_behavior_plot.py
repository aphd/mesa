import matplotlib.pyplot as plt
import pandas as pd
import os

def boxplot_behavior_plot():
    # Load the data from the CSV file (assume it has b1, b2, ... bn columns)
    data = pd.read_csv('./data/survey.csv')
    
    # Extract all column names (this will handle any number of columns dynamically)
    columns = data.columns
    
    # Convert all columns' data into a list for plotting
    data_to_plot = [data[col] for col in columns]
    
    # Create a figure and axis
    plt.figure(figsize=(10, 6))  # You can adjust the size as needed

    # Create the boxplots
    plt.boxplot(data_to_plot, labels=columns)

    # Add title and labels
    plt.title(f'Comparison of the minimum incentives across {len(columns)} Behavior Categories')
    plt.ylabel('Tokens')

    # Save the plot to the specified directory
    fn = os.getenv("FN_DIR") + "/boxplot_behavior_plot.pdf"
    plt.savefig(fn)

    # Optionally, show the plot
    plt.show()

# Call the function to plot
boxplot_behavior_plot()
