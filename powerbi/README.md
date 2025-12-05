# Power BI Dashboard Files

## 📁 Contents

This folder contains Power BI related files for the Blinkit Analysis Dashboard.

### Files

**Blinkit_Dashboard.pbix** (To be created)
- Main Power BI dashboard file
- Contains all visualizations and data model
- Open with Power BI Desktop

**DAX_measures.txt**
- Custom DAX formulas and measures
- Copy-paste into Power BI
- Organized by category

**dashboard_screenshots/**
- Screenshots of dashboard pages
- For documentation and preview

---

## 🚀 How to Create the Dashboard

Since `.pbix` files are binary and large, here's how to create your own:

### Step 1: Open Power BI Desktop

Download and install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Free)

### Step 2: Import Data

1. Click **Get Data** → **Text/CSV**
2. Navigate to `data/processed/master_dataset.csv`
3. Click **Load**

Or import individual files:
- `data/processed/customers_clean.csv`
- `data/processed/products_clean.csv`
- `data/processed/sales_clean.csv`
- `data/processed/deliveries_clean.csv`

### Step 3: Create Relationships

In **Model View**:
1. Drag `CustomerID` from Sales to Customers
2. Drag `ProductID` from Sales to Products
3. Drag `OrderID` from Sales to Deliveries
4. Ensure all relationships are active

### Step 4: Create Date Table

```dax
Calendar = 
ADDCOLUMNS(
    CALENDAR(DATE(2023,1,1), DATE(2024,12,31)),
    "Year", YEAR([Date]),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "Quarter", QUARTER([Date]),
    "DayOfWeek", WEEKDAY([Date]),
    "DayName", FORMAT([Date], "dddd"),
    "IsWeekend", WEEKDAY([Date]) IN {1, 7}
)
```

### Step 5: Add DAX Measures

Copy measures from `DAX_measures.txt` and create them in Power BI:
1. Right-click on table → **New Measure**
2. Paste DAX formula
3. Rename measure appropriately

### Step 6: Build Visualizations

#### Page 1: Executive Overview

**KPI Cards:**
- Total Revenue
- Total Orders
- Average Order Value
- Customer Retention Rate

**Charts:**
- Line chart: Revenue trend over time
- Donut chart: Revenue by category
- Bar chart: Top 10 products
- Gauge: Target vs actual

**Slicers:**
- Date range
- City
- Customer segment

#### Page 2: Customer Analytics

**Visuals:**
- Scatter plot: RFM segmentation
- Heat map: Purchase patterns (day × hour)
- Column chart: Customer acquisition
- Table: Top customers

#### Page 3: Product Performance

**Visuals:**
- Tree map: Category contribution
- Bar chart: Top products
- Line chart: Product trends
- Matrix: Product details

#### Page 4: Delivery Operations

**Visuals:**
- Map: Delivery coverage
- Histogram: Delivery time distribution
- Gauge: On-time delivery rate
- Table: Delivery partner performance

#### Page 5: Regional Analysis

**Visuals:**
- Filled map: Sales by region
- Clustered column: City comparison
- Line chart: Regional growth
- Table: Area-wise metrics

### Step 7: Format Dashboard

**Theme:**
- Use built-in theme or create custom
- Consistent colors across pages
- Professional fonts

**Layout:**
- Align visuals properly
- Use white space effectively
- Add page navigation buttons

**Interactivity:**
- Enable cross-filtering
- Add drill-through pages
- Create bookmarks for views

### Step 8: Save Dashboard

1. Click **File** → **Save As**
2. Save as `Blinkit_Dashboard.pbix`
3. Place in this folder

---

## 📊 Dashboard Design Guidelines

### Color Scheme

**Primary Colors:**
- Blinkit Yellow: #FFD700
- Dark Blue: #1E3A8A
- Green: #10B981
- Red: #EF4444

**Usage:**
- Revenue/Positive: Green
- Costs/Negative: Red
- Neutral: Blue
- Highlights: Yellow

### Typography

**Fonts:**
- Headers: Segoe UI Bold, 16-20pt
- Body: Segoe UI, 10-12pt
- Numbers: Segoe UI Semibold, 14-18pt

### Visual Best Practices

1. **KPIs at Top** - Most important metrics first
2. **Consistent Layout** - Same structure across pages
3. **Clear Labels** - No ambiguous titles
4. **Appropriate Charts** - Right visual for data type
5. **Interactive Filters** - Easy to use slicers
6. **Mobile Friendly** - Responsive design

---

## 🎨 Page Templates

### Executive Page Template

```
┌─────────────────────────────────────────────────┐
│  [Date Slicer]  [City Slicer]  [Segment Slicer] │
├─────────────────────────────────────────────────┤
│  [Revenue]  [Orders]  [AOV]  [Retention]        │
├─────────────────────────────────────────────────┤
│  [Revenue Trend Chart - Full Width]             │
├─────────────────────────────────────────────────┤
│  [Category Donut]  │  [Top Products Bar Chart]  │
└─────────────────────────────────────────────────┘
```

### Analytics Page Template

```
┌─────────────────────────────────────────────────┐
│  [Filters]                                       │
├─────────────────────────────────────────────────┤
│  [Main Chart - 60% width]  │  [KPIs - 40%]      │
├─────────────────────────────────────────────────┤
│  [Supporting Chart 1]  │  [Supporting Chart 2]  │
└─────────────────────────────────────────────────┘
```

---

## 🔧 Troubleshooting

### Data Not Loading

**Issue:** "Couldn't load data"

**Solution:**
1. Check file paths in Power Query
2. Ensure CSV files exist in `data/processed/`
3. Run `python scripts/data_generation.py`
4. Refresh data source

### Relationships Not Working

**Issue:** Visuals not filtering correctly

**Solution:**
1. Go to Model View
2. Check relationship directions
3. Ensure cardinality is correct (1:Many)
4. Activate relationships

### Slow Performance

**Issue:** Dashboard is laggy

**Solution:**
1. Reduce data volume
2. Use aggregated tables
3. Optimize DAX measures
4. Remove unused columns
5. Use DirectQuery instead of Import

---

## 📚 Resources

**Power BI Learning:**
- [Microsoft Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [Power BI Community](https://community.powerbi.com/)
- [DAX Guide](https://dax.guide/)
- [Power BI YouTube](https://www.youtube.com/user/mspowerbi)

**Dashboard Design:**
- [Power BI Best Practices](https://docs.microsoft.com/power-bi/guidance/)
- [Dashboard Design Principles](https://www.tableau.com/learn/articles/dashboard-design-principles)

---

## 💡 Tips

1. **Start Simple** - Build basic visuals first, then enhance
2. **Test Filters** - Ensure all slicers work correctly
3. **Use Bookmarks** - Save different views
4. **Add Tooltips** - Provide context on hover
5. **Mobile Layout** - Create mobile-optimized version
6. **Performance** - Monitor query performance
7. **Documentation** - Add text boxes with instructions
8. **Version Control** - Save versions before major changes

---

## 🎯 Checklist

Before finalizing dashboard:
- [ ] All data sources connected
- [ ] Relationships created
- [ ] DAX measures added
- [ ] All 5 pages created
- [ ] Visuals formatted consistently
- [ ] Filters working correctly
- [ ] Cross-filtering enabled
- [ ] Drill-through configured
- [ ] Mobile layout created
- [ ] Performance optimized
- [ ] Tested with different data
- [ ] Screenshots taken
- [ ] Dashboard saved

---

**Need help?** Check [DASHBOARD_GUIDE.md](../DASHBOARD_GUIDE.md) or open an issue on GitHub.

**Questions?** Email akratimishra366@gmail.com