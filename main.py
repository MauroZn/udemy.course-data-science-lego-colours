import pandas as pd
import matplotlib.pyplot as plt

def run_challenge(description, func):
    print(f"\nChallenge: {description}")
    input("Press ENTER to see the result...\n")
    func()

colors = pd.read_csv('data/colors.csv')
sets = pd.read_csv('data/sets.csv')
themes = pd.read_csv('data/themes.csv')

# Challenge 1: Count unique LEGO colours
def count_unique_colours():
    print(colors['name'].nunique())

# Challenge 2: Count transparent vs opaque colours
def transparent_vs_opaque():
    print(colors.groupby('is_trans').count())
    print(colors.is_trans.value_counts())

# Challenge 3: First LEGO sets ever released
def first_lego_sets():
    print(sets.sort_values('year').head())

# Challenge 4: Sets sold in LEGO’s first year (1949)
def sets_in_1949():
    print(sets[sets['year'] == 1949])

# Challenge 5: Top 5 LEGO sets with most parts
def top_sets_by_parts():
    print(sets.sort_values('num_parts', ascending=False).head())

# Challenge 6: Number of LEGO sets released per year
def show_sets_by_year():
    global sets_by_year
    sets_by_year = sets.groupby('year').count()
    print(sets_by_year['set_num'].head())
    print(sets_by_year['set_num'].tail())

# Challenge 7: Line chart of sets released per year
def plot_sets_by_year():
    plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
    plt.xlabel("Year")
    plt.ylabel("Number of Sets")
    plt.title("LEGO Sets Released Per Year")
    plt.show()

# Challenge 8: Number of unique themes released per year
def calc_themes_by_year():
    global themes_by_year
    themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
    themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
    print(themes_by_year.head())
    print(themes_by_year.tail())

# Challenge 9: Line chart of themes released per year
def plot_themes_by_year():
    plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
    plt.xlabel("Year")
    plt.ylabel("Number of Themes")
    plt.title("LEGO Themes Released Per Year")
    plt.show()

# Challenge 10: Dual-axis plot of sets and themes per year
def dual_axis_plot():
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='green')
    ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='blue')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Sets', color='green')
    ax2.set_ylabel('Number of Themes', color='blue')
    plt.title("Number of Sets and Themes Over the Years")
    plt.show()

# Challenge 11: Average number of parts per set over time
def avg_parts_per_set():
    global parts_per_set
    parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
    print(parts_per_set.head())
    print(parts_per_set.tail())

# Challenge 12: Scatter plot of average parts over time
def scatter_plot_parts():
    plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
    plt.xlabel("Year")
    plt.ylabel("Average Number of Parts")
    plt.title("Average Number of Parts per Set Over Time")
    plt.show()

# Challenge 13: Top 5 LEGO themes by number of sets
def top_themes_by_set_count():
    global set_theme_count
    set_theme_count = sets["theme_id"].value_counts()
    print(set_theme_count.head())

# Challenge 14: Bar chart of top 10 themes by set count
def plot_top_themes():
    set_theme_count_df = pd.DataFrame({
        'id': set_theme_count.index,
        'set_count': set_theme_count.values
    })
    merged_df = pd.merge(set_theme_count_df, themes, on='id')

    plt.figure(figsize=(14, 8))
    plt.xticks(fontsize=14, rotation=45)
    plt.yticks(fontsize=14)
    plt.ylabel('Nr of Sets', fontsize=14)
    plt.xlabel('Theme Name', fontsize=14)
    plt.title("Top 10 LEGO Themes by Number of Sets")
    plt.bar(merged_df.name[:10], merged_df.set_count[:10])
    plt.show()

# ------------------ Run Challenges ------------------

run_challenge("How many different colours does the LEGO company produce?", count_unique_colours)

run_challenge("Find the number of transparent colours vs opaque colours", transparent_vs_opaque)

run_challenge("Take a look at the first LEGO sets ever released", first_lego_sets)

run_challenge("How many different sets did LEGO sell in their first year (1949)?", sets_in_1949)

run_challenge("Find the top 5 LEGO sets with the most number of parts", top_sets_by_parts)

run_challenge("Show the number of LEGO sets released year-on-year", show_sets_by_year)

run_challenge("Show the number of LEGO releases on a line chart", plot_sets_by_year)

run_challenge("Calculate number of unique LEGO themes released per year", calc_themes_by_year)

run_challenge("Plot the number of themes released by year", plot_themes_by_year)

run_challenge("Show dual-axis plot for sets and themes per year", dual_axis_plot)

run_challenge("Compare average number of parts per set over the years", avg_parts_per_set)

run_challenge("Has the size of LEGO sets increased over time? Show a scatter plot", scatter_plot_parts)

run_challenge("Top 5 LEGO themes by number of sets", top_themes_by_set_count)

run_challenge("Plot the top 10 LEGO themes by number of sets", plot_top_themes)
