import matplotlib.pyplot as plt
import pandas as pd

def plot_pe_zscore(fundamentals_df):
    """
    Plot the PE ratio Z-score analysis for a stock
    
    Parameters:
    fundamentals_df (pd.DataFrame): DataFrame containing PE Ratio, PE Mean, and PE Std columns
    """
    # Calculate PE Z-Score
    fundamentals_df['PE Z-Score'] = (fundamentals_df['PE Ratio'] - fundamentals_df['PE Mean']) / fundamentals_df['PE Std']
    fundamentals_df.dropna(inplace=True)
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(fundamentals_df.index, fundamentals_df['PE Z-Score'], label='P/E Z-Score', color='blue')
    plt.axhline(2, color='red', linestyle='dashed', label='Potential Bubble Threshold (Z=2)')
    plt.axhline(-2, color='green', linestyle='dashed', label='Undervalued Threshold (Z=-2)')
    plt.axhline(0, color='black', linestyle='dotted')
    plt.title('Nvidia P/E Z-Score')
    plt.legend()
    plt.xlabel('Time (Months)')
    plt.ylabel('Z-Score')
    plt.grid(True)
    plt.show()