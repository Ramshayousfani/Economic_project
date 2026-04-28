# Name: Ramsha
# Roll no: CF-89
# Section: B
# Project: ECONOMIC INDICATOR COMPARISON & PREDICTION SYSTEM 

# unemployment data from world bank (https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?end=2025&locations=PK&start=2000)
# poverty data from world bank and pakistan bureau of statistics (https://blogs.worldbank.org/en/endpovertyinsouthasia/pakistan-s-poverty-trajectory--progress--peril--and-the-path-for)
# (https://www.pbs.gov.pk/national-accounts-2/)
# gdp data from world bank (https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?end=2024&locations=PK&start=1961)

print("===== ECONOMIC INDICATOR SYSTEM FOR PAKISTAN =====")

import numpy as np
import matplotlib.pyplot as plt


# ------------------ STEP 1: COMPLETE DATASET (2000–2025) ------------------

gdp_data = {
2000:4.3, 2001:3.7, 2002:2.6, 2003:5.4, 2004:7.8,
2005:7.3, 2006:6.1, 2007:4.4, 2008:2.1, 2009:3.5,
2010:1.5, 2011:2.7, 2012:3.0, 2013:4.4, 2014:4.1,
2015:4.2, 2016:6.6, 2017:4.4, 2018:6.2, 2019:2.5,
2020:-1.3, 2021:6.5, 2022:4.8, 2023:-0.4, 2024:3.0,
2025:3.1
}

unemp_data = {
2000:0.6, 2001:0.6, 2002:0.6, 2003:0.6, 2004:0.6,
2005:0.6, 2006:0.6, 2007:0.4, 2008:0.4, 2009:0.5,
2010:0.7, 2011:0.8, 2012:3.7, 2013:3.0, 2014:1.8,
2015:3.6, 2016:2.3, 2017:3.2, 2018:4.1, 2019:4.8,
2020:6.0, 2021:6.3, 2022:5.3, 2023:5.2, 2024:5.5,
2025:5.4
}

poverty_data = {
2000:64.9, 2001:66.5, 2002:61.9, 2003:57.3, 2004:52.7,
2005:54.3, 2006:50.9, 2007:47.6, 2008:44.2, 2009:40.8,
2010:37.5, 2011:36.4, 2012:33.0, 2013:29.7, 2014:27.0,
2015:24.3, 2016:23.4, 2017:22.4, 2018:21.5, 2019:24.7,
2020:21.9, 2021:18.3, 2022:24.8, 2023:25.3, 2024:25.3,
2025:28.9
}


# ------------------ STEP 2: MERGE DATA ------------------

economic_data = {}

for year in range(2000, 2026):
    economic_data[year] = {
        "GDP": gdp_data[year],
        "Unemployment": unemp_data[year],
        "Poverty": poverty_data[year]
    }


# ------------------ STEP 3: DASHBOARD GRAPH ------------------

years = sorted(economic_data.keys())
indicators = ["GDP", "Unemployment", "Poverty"]

plt.figure(figsize=(12,6))

for indicator in indicators:
    values = [economic_data[y][indicator] for y in years]
    plt.plot(years, values, marker='o', label=indicator)

plt.title("Pakistan Economic Trends (2000–2025)")
plt.xlabel("Year")
plt.ylabel("Value (%)")
plt.legend()
plt.grid()
plt.show()


# ------------------ STEP 4: COMPARISON ------------------

year = int(input("Enter a year (2000–2024) to compare with 2025: "))

if year not in economic_data or year == 2025:
    print("Invalid year")
else:
    old = economic_data[year]
    new = economic_data[2025]

    print("\n----- Percentage Change -----")
    for ind in indicators:
        change = ((new[ind] - old[ind]) / old[ind]) * 100
        print(f"{ind}: {change:.2f}% change")

    print("\n--- Interpretation ---")
    for ind in indicators:
        if new[ind] > old[ind]:
            print(f"{ind}: Increased")
        elif new[ind] < old[ind]:
            print(f"{ind}: Decreased")
        else:
            print(f"{ind}: No change")

    # Comparison Graph
    plt.figure(figsize=(8,5))

    x = np.arange(len(indicators))
    old_values = [old[ind] for ind in indicators]
    new_values = [new[ind] for ind in indicators]

    plt.bar(x - 0.2, old_values, width=0.4, label=str(year))
    plt.bar(x + 0.2, new_values, width=0.4, label="2025")

    plt.xticks(x, indicators)
    plt.ylabel("Values")
    plt.title(f"Economic Comparison: {year} vs 2025")
    plt.legend()
    plt.grid(axis='y')
    plt.show()


# ------------------ STEP 5: PREDICTION (2026) ------------------

print("\n----- PREDICTED VALUES FOR 2026 -----")

x = np.array(years)
predicted = {}

for ind in indicators:
    y = np.array([economic_data[yr][ind] for yr in years])

    coeffs = np.polyfit(x, y, 2)   # Polynomial Regression
    model = np.poly1d(coeffs)

    pred_val = model(2026)
    predicted[ind] = pred_val

    print(f"{ind} Prediction 2026: {pred_val:.2f}")


# ------------------ STEP 6: PREDICTION GRAPHS ------------------

for ind in indicators:
    plt.figure()

    values = [economic_data[y][ind] for y in years]
    plt.plot(years, values, label="Actual Data")

    plt.scatter(2026, predicted[ind], label="Prediction 2026")

    plt.title(f"{ind} Prediction (2026)")
    plt.xlabel("Year")
    plt.ylabel(ind)
    plt.legend()
    plt.grid()
    plt.show()


print("===== PROJECT COMPLETED SUCCESSFULLY =====")