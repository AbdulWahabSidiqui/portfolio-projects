# 🔎 Fatal Force — Advanced Analysis of Police Killings in the United States

> **Turning raw data into meaningful insights about police killings in the United States.**

An advanced **Data Analysis & Visualization** project exploring fatal police shootings in the United States using data collected by **The Washington Post**.

This project started as a Python data analysis course project and was later upgraded into a more comprehensive, portfolio-ready analysis with deeper exploration, statistical comparisons, and interactive visualizations.

---

## 📊 Project Overview

Police killings are a complex social issue involving demographic, geographic, economic, and behavioral factors.

The goal of this project is **not simply to count fatalities**, but to explore the data and identify patterns that can help answer questions such as:

* 📈 How have police killings changed over time?
* 👥 Which demographic groups are most represented?
* ⚧️ How do fatalities differ by gender?
* 🗺️ Which states and cities have the highest numbers of incidents?
* 🧠 How frequently are signs of mental illness reported?
* 🔫 What role does the victim's armed status play?
* 📷 How common are body cameras in these incidents?
* 💰 Is there a relationship between police killings and local socioeconomic conditions?
* 🎓 How does education level vary across affected communities?
* 🏙️ How do racial demographics of cities compare with fatality patterns?

The analysis combines **exploratory data analysis, data cleaning, visualization, and statistical investigation** to uncover these patterns.

---

## 🚀 What Makes This Version "Advanced"?

This isn't just the original course analysis.

I expanded the project by building on the initial exploration and adding a more portfolio-focused analytical workflow.

### Original Analysis

The original analysis explores:

* Race distribution
* Gender distribution
* Age distribution
* Armed vs. unarmed victims
* Mental illness
* Geographic distribution
* Police killings over time
* State-level patterns

### Advanced Analysis

The upgraded version goes further by exploring:

* 📊 Deeper demographic comparisons
* 📈 Time-series trends
* 🗺️ Geographic patterns
* 💵 Income and poverty relationships
* 🎓 Education-level comparisons
* 👥 Population race comparisons
* 📉 Statistical relationships between variables
* 🖱️ Interactive Plotly visualizations
* 🔍 More detailed exploratory analysis

---

## 🧰 Technologies & Libraries

| Technology      | Purpose                           |
| --------------- | --------------------------------- |
| 🐍 Python       | Core programming language         |
| 🐼 Pandas       | Data manipulation & analysis      |
| 🔢 NumPy        | Numerical computing               |
| 📊 Matplotlib   | Data visualization                |
| 🎨 Seaborn      | Statistical visualization         |
| 📈 Plotly       | Interactive visualizations        |
| ☁️ Google Colab | Notebook environment              |
| 🐙 GitHub       | Version control & project hosting |

---

## 📂 Dataset

The project works with multiple datasets covering different aspects of the analysis.

### Main Dataset

**Deaths by Police in the United States**

Contains information including:

* Name
* Date
* Manner of death
* Armed status
* Age
* Gender
* Race
* City
* State
* Signs of mental illness
* Threat level
* Flee status
* Body camera status

The main dataset contains **2,535 records and 14 columns** in the version analyzed in the notebook.

### Supporting Datasets

Additional datasets are used to investigate socioeconomic and demographic context:

* Median Household Income
* Percentage of People Below Poverty Level
* Percentage Completing High School
* Share of Race by City

---

## 🔬 Analysis Workflow

The project follows a structured data-analysis pipeline:

```text
Raw Data
   │
   ▼
Data Loading
   │
   ▼
Data Exploration
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Demographic Analysis
   │
   ▼
Geographic Analysis
   │
   ▼
Socioeconomic Analysis
   │
   ▼
Statistical Investigation
   │
   ▼
Interactive Visualization
   │
   ▼
Insights & Conclusions
```

---

## 📈 Key Areas of Investigation

### 👥 Demographics

Analysis of:

* Race
* Gender
* Age
* Armed status
* Mental illness indicators

### 🗺️ Geography

Investigation of:

* States with the highest number of fatalities
* Cities with the highest number of incidents
* Geographic distribution of killings
* Population-adjusted comparisons

### 📅 Time

Time-series analysis examining:

* Fatalities by year
* Year-over-year changes
* Long-term trends
* Changes in incident characteristics

### 💰 Socioeconomic Factors

The project compares police killings with:

* Median household income
* Poverty levels
* High-school completion rates

### 🎨 Data Visualization

Visualizations are used to make patterns easier to understand, including:

* Bar charts
* Donut charts
* Histograms
* Scatter plots
* Time-series charts
* Choropleth maps
* Interactive Plotly charts

---

## 💡 Questions This Project Explores

> **Who?**
> What demographic patterns appear among people killed by police?

> **Where?**
> Which states and cities experience the most incidents?

> **When?**
> Are police killings increasing, decreasing, or remaining relatively stable?

> **Why might patterns differ?**
> How do socioeconomic and demographic characteristics vary across locations?

> **What relationships exist?**
> Are variables such as poverty, education, income, and race associated with differences in police-killing rates?

---

## 📊 Example Visualizations

The notebook includes multiple visualizations designed to turn complex datasets into understandable insights.

Some of the analysis includes:

* Race distribution
* Fatalities by gender
* Age distribution
* Armed vs. unarmed victims
* Police killings by state
* Police killings over time
* Geographic choropleth maps
* Socioeconomic comparisons
* Interactive Plotly visualizations

---

## ▶️ Run the Project

### Option 1 — Google Colab

The easiest way to run the notebook is with Google Colab.

**Requirements:**

```text
Python 3
Pandas
NumPy
Matplotlib
Seaborn
Plotly
```

Some visualizations use Plotly and may require the following:

```python
%pip install --upgrade plotly
```

### Option 2 — Jupyter Notebook

Clone the repository:

```bash
git clone https://github.com/AbdulWahabSidiqui/portfolio-projects.git
```

Navigate to the project:

```bash
cd portfolio-projects/Analyse\ Death\ Involving\ Police
```

Then open:

```text
Fatal_Force_Advanced_Analysis.ipynb
```

---

## 📁 Project Structure

```text
Analyse Death Involving Police/
│
├── Fatal_Force_Advanced_Analysis.ipynb
│
├── Deaths_by_Police_US.csv
├── Median_Household_Income_2015.csv
├── Pct_People_Below_Poverty_Level.csv
├── Pct_Over_25_Completed_High_School.csv
└── Share_of_Race_By_City.csv
```

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

* ✅ Data cleaning
* ✅ Data wrangling
* ✅ Exploratory Data Analysis (EDA)
* ✅ Grouping and aggregation
* ✅ Handling missing values
* ✅ Statistical analysis
* ✅ Correlation analysis
* ✅ Time-series analysis
* ✅ Geographic analysis
* ✅ Data visualization
* ✅ Interactive visualization
* ✅ Drawing insights from real-world data
* ✅ Communicating analytical findings

---

## 🧠 What I Learned

Working on this project helped me move beyond simply writing Python code and toward thinking like a data analyst.

I learned how to:

* Ask meaningful questions before analyzing data
* Clean messy real-world datasets
* Choose appropriate visualizations
* Compare multiple datasets
* Look for relationships rather than isolated numbers
* Interpret trends carefully
* Communicate findings through visualizations
* Turn a course assignment into a more complete portfolio project

One of the biggest lessons was that **data analysis is not just about creating charts — it's about asking better questions and using evidence to answer them.**

---

## ⚠️ Important Note

This dataset represents real-world deaths involving police and contains sensitive subject matter.

The analysis is intended for **educational and analytical purposes**. Observed associations in the data should not automatically be interpreted as causal relationships.

---

## 📚 Data Source

The original police shooting data was collected and maintained as part of **The Washington Post's police shootings database**.

Additional demographic and socioeconomic datasets are used to provide broader context for the analysis.

---

## 👨‍💻 Author

**Abdul Wahab Sidiqui**

Aspiring **Data Scientist | Python Developer**

Interested in:

```text
Python
Data Analysis
Data Science
Machine Learning
Artificial Intelligence
```

---

## ⭐ Project Status

**Status:** 🟢 Advanced Analysis Completed

This project represents an upgraded version of my original course analysis and is part of my growing **Data Science portfolio**.

---

### ⭐ If you found this project interesting

Feel free to explore the notebook, examine the analysis, and check out the other projects in my portfolio.

**Built with Python 🐍 and curiosity 📊**
