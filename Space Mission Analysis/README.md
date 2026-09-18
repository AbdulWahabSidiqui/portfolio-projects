# 🚀 Space Mission Analysis

## Exploring the History of Space Exploration

This project analyzes historical space missions from the beginning of the Space Race in 1957 through the latest records available in the dataset.

The analysis explores launch activity, mission outcomes, organizations, launch locations, launch costs, and the historical comparison between the United States and the Soviet Union.

---

## 📊 Project Overview

The project uses historical space mission records scraped from **Next Spaceflight** to investigate patterns in the development of the global space-launch industry.

### Key Questions

* Which organizations launched the most missions?
* How has launch activity changed over time?
* Which countries accounted for the most launch activity?
* How are mission outcomes distributed?
* How have recorded launch costs varied over time?
* Which organizations led launch activity during different periods?
* How did USA and USSR launch activity compare during the Space Race?

---

## 🎯 Objectives

The main objectives of this project were to:

* Clean and prepare historical space mission data
* Explore the structure and quality of the dataset
* Analyze mission outcomes and rocket status
* Investigate launch activity by country and organization
* Examine launch trends over time
* Analyze recorded launch costs
* Study failure patterns
* Compare USA and USSR launch activity and mission success
* Communicate findings through interactive visualizations

---

## 🧹 Data Cleaning & Preparation

The dataset initially contained several unnecessary index columns, duplicate records, missing values, and launch-price values stored in a format requiring conversion.

The cleaning process included:

* Removing unnecessary index columns
* Removing duplicate records
* Converting launch prices to numeric values
* Handling missing launch-price data
* Converting dates into a proper datetime format
* Extracting year and month features
* Extracting and standardizing countries from launch locations

Launch-cost analysis is limited to missions where price information is available.

---

## 📈 Analysis & Visualizations

The project contains a variety of visualizations designed to examine different aspects of space-launch history.

### 🚀 Mission Outcomes

Mission records are analyzed by outcome, including successful, failed, partially failed, and prelaunch-failed missions.

### 🏢 Organization Analysis

The project examines:

* Organizations with the highest number of recorded launches
* Changes in organizational leadership over time
* The distribution of launch activity among major organizations

### 🌍 Geographic Analysis

Interactive maps show the distribution of launches and unsuccessful missions by launch location.

> Launch location represents where the mission was launched and should not automatically be interpreted as the nationality of the organization conducting the mission.

### 💰 Launch Cost Analysis

Recorded launch costs are analyzed using:

* Distribution analysis
* Outlier analysis
* Average recorded launch cost over time

Because launch prices are missing for many records, cost analysis represents only missions with available price information.

### 📈 Launch Trends

Yearly launch activity is visualized alongside a 5-year rolling average to highlight longer-term patterns while reducing the effect of individual-year fluctuations.

### 🌳 Hierarchical Analysis

A Plotly Sunburst chart explores the relationship between:

**Country → Organization → Mission Outcome**

### 🇺🇸🇷🇺 USA vs USSR

The project compares USA launch activity with the USSR and former Soviet launch locations.

The comparison examines:

* Launch activity over time
* Mission success rates

Launch volume and mission success are treated as separate measures rather than using either one as a complete measure of historical space-program performance.

---

## 🔍 Key Findings

### 🚀 Space launches are concentrated among major organizations

A relatively small number of organizations account for a large share of recorded launches, demonstrating the concentration of historical launch capabilities among major space programs and companies.

### 📈 Launch activity changed significantly over time

Yearly launch activity varies considerably across different periods. The 5-year rolling average helps reveal longer-term patterns that are less obvious from individual yearly values.

### 🌍 Launch activity is geographically concentrated

A limited number of countries account for a large proportion of recorded launch activity.

### 💰 Launch costs vary considerably

Recorded launch prices show substantial variation across missions. However, many records do not contain price information, so cost-related conclusions apply only to the available price data.

### 🏢 Organizational leadership changed over time

The organizations responsible for the highest number of launches changed across different periods, reflecting changes in the global space-launch industry.

### 🇺🇸🇷🇺 USA and USSR launch activity varied across periods

The USA vs USSR comparison shows substantial changes in launch activity across different periods represented in the dataset.

### ✅ Launch volume and mission success are different measures

The organization or country with the highest launch volume is not necessarily the one with the highest mission success rate. Considering both measures provides a broader view of historical launch activity.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Plotly**
* **ISO 3166**

---

## 📂 Project Structure

```text
Space Mission Analysis/
│
├── Space_Missions_Analysis.ipynb
├── mission_launches.csv
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/AbdulWahabSidiqui/portfolio-projects.git
```

### 2. Navigate to the project

```bash
cd portfolio-projects/Selected Projects/Space Mission Analysis
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn plotly iso3166 jupyter
```

### 4. Open the notebook

```bash
jupyter notebook Space_Missions_Analysis.ipynb
```

Run the notebook cells from top to bottom to reproduce the analysis.

---

## 📌 Conclusion

This project explores historical space missions to understand how launch activity, mission outcomes, organizations, countries, and launch costs changed over time.

Through data cleaning, exploratory analysis, statistical summaries, and interactive visualizations, the project presents multiple perspectives on the evolution of the space-launch industry from the early Space Race to the modern era.

The analysis demonstrates why multiple measures—such as launch volume, mission success, geographic distribution, and recorded cost—are useful when studying the development of space exploration.

---

## 👤 Author

**Abdul Wahab Sidiqui**

Data Analysis • Python • Pandas • Data Visualization
