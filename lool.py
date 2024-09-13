import pandas as pd
import random
import itertools
import matplotlib.pyplot as plt

# Load the historical draw data
# Assume the CSV file has columns: 'Draw_Number', 'Number1', 'Number2', 'Number3', 'Number4', 'Number5', 'Number6'
df = pd.read_csv('/home/mtirbelkaid/.local/bin:/opt/gradle/bin:/opt/maven/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/go/bin:/usr/local/node_packages/node_modules/.bin:/usr/local/rvm/bin:/google/go_appengine:/google/google_appengine:/home/mtirbelkaid/.gems/bin:/usr/local/rvm/bin:/home/mtirbelkaid/gopath/bin:/google/gopath/bin:/google/flutter/bin:/usr/local/nvm/versions/node/v20.17.0/bin south_korea_lotto.csv.csv')

# Frequency Analysis
def frequency_analysis(df):
    numbers = df.iloc[:, 1:].values.flatten()
    freq_series = pd.Series(numbers).value_counts().sort_index()
    print("Frequency of Each Number:")
    print(freq_series)

    # Plotting frequency
    freq_series.plot(kind='bar', figsize=(12, 6))
    plt.title('Frequency of Each Lotto Number')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.show()

# Pattern Analysis
def pattern_analysis(df):
    odd_count = df.iloc[:, 1:].applymap(lambda x: x % 2).sum(axis=1)
    even_count = 6 - odd_count

    print("Odd vs Even Number Distribution:")
    print(f"Odd Numbers: {odd_count.mean()} on average per draw")
    print(f"Even Numbers: {even_count.mean()} on average per draw")

    sum_numbers = df.iloc[:, 1:].sum(axis=1)
    print(f"Sum of Numbers (average): {sum_numbers.mean()}")

# Monte Carlo Simulation
def monte_carlo_simulation(num_simulations=10000):
    results = []
    for _ in range(num_simulations):
        draw = sorted(random.sample(range(1, 46), 6))
        results.append(draw)

    sim_df = pd.DataFrame(results, columns=[f"Number{i+1}" for i in range(6)])
    return sim_df

# Running the Analysis
if __name__ == "__main__":
    # Frequency Analysis
    frequency_analysis(df)

    # Pattern Analysis
    pattern_analysis(df)

    # Monte Carlo Simulation
    sim_df = monte_carlo_simulation()
    print("Sample of Monte Carlo Simulated Draws:")
    print(sim_df.head())

    # Optional: Save simulation results
    sim_df.to_csv('monte_carlo_simulation_results.csv', index=False)
