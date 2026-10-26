import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated inventory data
np.random.seed(42)

products = [
    "Product_A",
    "Product_B",
    "Product_C",
    "Product_D",
    "Product_E"
]

average_daily_demand = np.array([120, 85, 150, 65, 100])
demand_std = np.array([18, 12, 25, 10, 16])
lead_time_days = np.array([7, 10, 6, 12, 8])
current_inventory = np.array([1100, 760, 1050, 620, 880])

# Service level assumption: approximately 95%
z_score = 1.65

# Safety stock calculation
safety_stock = (
    z_score
    * demand_std
    * np.sqrt(lead_time_days)
)

# Reorder point
reorder_point = (
    average_daily_demand * lead_time_days
    + safety_stock
)

# Days of inventory
days_of_inventory = (
    current_inventory / average_daily_demand
)

# Stockout risk
stockout_risk = np.where(
    current_inventory < reorder_point,
    "High",
    "Low"
)

# Build dataframe
data = pd.DataFrame({
    "Product": products,
    "Average_Daily_Demand": average_daily_demand,
    "Demand_Std": demand_std,
    "Lead_Time_Days": lead_time_days,
    "Current_Inventory": current_inventory,
    "Safety_Stock": np.round(safety_stock, 1),
    "Reorder_Point": np.round(reorder_point, 1),
    "Days_of_Inventory": np.round(days_of_inventory, 1),
    "Stockout_Risk": stockout_risk
})

print(data)

# Save results
data.to_csv("inventory_analysis_results.csv", index=False)

# Visualization
plt.figure(figsize=(10, 6))

x = np.arange(len(products))
width = 0.35

plt.bar(
    x - width / 2,
    current_inventory,
    width,
    label="Current Inventory"
)

plt.bar(
    x + width / 2,
    reorder_point,
    width,
    label="Reorder Point"
)

plt.xticks(x, products)
plt.ylabel("Units")
plt.title("Current Inventory vs Reorder Point")
plt.legend()
plt.grid(axis="y")
plt.tight_layout()

plt.savefig(
    "inventory_optimization_plot.png",
    dpi=300
)

plt.show()
