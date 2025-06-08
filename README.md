**Data Analytics Project – Ecommerce Product Rating Analysis**

This project analyzes user-product ratings from an ecommerce dataset. The goal is to identify product popularity, rating trends, and user behavior through data cleaning, exploration, and visual storytelling using Python.

**Dataset Used:**
- File: ratings.csv (subset of ratings_Beauty.csv from Kaggle)
- Modified to contain only userId, productId, and rating columns
- Limited to 15000 records for simplicity
- Timestamp column removed

**Requirements:**
- Python 3.10 or higher
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- jupyter notebook
- nbformat (required for interactive charts)

To install the required libraries, use:
pip install pandas numpy matplotlib seaborn plotly notebook nbformat

**What the Project Does:**
- Loads and cleans the dataset
- Removes duplicates and missing values
- Converts rating values to numeric
- Filters out users/products with very few reviews
- Applies data transformation (log scale) for better insights

**Visualizations and Insights:**
- Rating distribution histogram
- Bar chart of most-rated products
- Interactive bar chart using Plotly for improved clarity
- Heatmap of sample user-product ratings
- Clear labels, legends, and color schemes added
- Data storytelling through statistics and visual patterns

**How to Run:**
- Open Jupyter Notebook
- Open the analysis.ipynb file inside the Notebooks folder
- Run all cells one by one to perform the analysis and see the visualizations

**Author:**
**ByteSquad**
