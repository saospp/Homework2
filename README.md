 Reddit Data Pipeline (Analysis & Processing)

This project contains a set of tools (Python scripts and Jupyter Notebooks) for the full lifecycle of Reddit data processing: from merging raw files to filtering out bots and visualizing user activity.

Project Structure & File Descriptions

* **`to_csv.py`**: A script for preparing raw data. It automatically scans the specified directory, finds all files with the prefixes `RS_` (submissions) and `RC_` (comments), sorts them chronologically, and merges them into two large consolidated datasets: `combined_reddit_submissions.csv` and `combined_reddit_comments.csv`.


* **`bot_filter.py`**: A script for cleaning the consolidated datasets from automated content. It uses heuristic analysis: searching for the word `bot` or `AutoModerator` in the `author` column, and checking post and comment texts for typical bot template phrases (e.g., *"I am a bot"*, *"beep boop"*). The cleaned data is saved into new files with the `cleaned_` prefix.


* **`comments.ipynb`**: A Jupyter Notebook for Exploratory Data Analysis (EDA) of the comments. It performs basic data structure cleaning (keeping the 13-15 most important columns out of the initial 74 to save memory), calculates statistics by subreddits and top authors, and plots daily commenter activity highlighting anomalous peaks (above the 95th percentile).


* **`submissions.ipynb`**: A similar Jupyter Notebook for analyzing submissions (posts). It optimizes the initial 120 meta-columns, keeping only those necessary for text and time-series analysis. It builds bar charts by subreddits and line graphs of publication dynamics with color highlighting for periods of maximum activity.



 Environment Requirements (Dependencies)

To successfully run the project in your virtual environment (e.g., `.venv`), the following libraries must be installed:

* `pandas` (for dataframe manipulation)
* `matplotlib` and `seaborn` (for data visualization)

You can install them using the following command:

```bash
pip install pandas matplotlib seaborn

```

Usage Instructions

1. **Data Merging**: Configure the `folder_path` variable in the `to_csv.py` file to point to your raw data directory and run the script. This will create the initial merged `combined_*.csv` files.


2. **Bot Filtering**: Run the `bot_filter.py` script. It will analyze the generated files, filter out bots, and output the final datasets `cleaned_combined_*.csv`.


3. **Analytics**: Open `comments.ipynb` or `submissions.ipynb` in a Jupyter environment (or directly within PyCharm) and sequentially execute the cells to obtain statistics, reduce file memory footprint, and visualize user activity graphs.