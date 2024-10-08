from plot.plot_tokens import plot_tokens
import matplotlib.pyplot as plt

def compare_tokens_plot(models):
    # Create a single figure and axis for all plots
    plt.figure(figsize=(12, 8))
    ax = plt.gca()  # Get the current axis
    
    for index, model in enumerate(models):
        print(model.get_name())
        print(f"Index: {index}, Element: {model}")
        plot_tokens(ax, model)
    
    plt.legend([model.get_name() for model in models], loc='upper right')
    plt.tight_layout()
    plt.show()
