# 🚀 Quick Start Guide - Blinkit Analysis Dashboard

Get your dashboard running in 10 minutes!

---

## ⚡ Super Quick Start (3 Steps)

### Step 1: Clone Repository
```bash
git clone https://github.com/Akrati36/blinkit-analysis-dashboard.git
cd blinkit-analysis-dashboard
```

### Step 2: Generate Data
```bash
pip install -r requirements.txt
python scripts/data_generation.py
```

### Step 3: Open Dashboard
- Download [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Free)
- Open `powerbi/Blinkit_Dashboard.pbix`
- Click **Refresh** to load data
- Explore! 🎉

---

## 📋 Detailed Setup

### Prerequisites

**Required:**
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Power BI Desktop ([Download](https://powerbi.microsoft.com/desktop/))

**Optional:**
- Git ([Download](https://git-scm.com/downloads))
- Excel (for viewing CSV files)

---

### Installation Steps

#### 1. Get the Code

**Option A: Using Git**
```bash
git clone https://github.com/Akrati36/blinkit-analysis-dashboard.git
cd blinkit-analysis-dashboard
```

**Option B: Download ZIP**
1. Go to https://github.com/Akrati36/blinkit-analysis-dashboard
2. Click **Code** → **Download ZIP**
3. Extract the ZIP file
4. Open terminal/command prompt in extracted folder

#### 2. Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

**Packages installed:**
- pandas - Data manipulation
- numpy - Numerical operations
- faker - Sample data generation
- matplotlib - Visualizations
- seaborn - Statistical plots

#### 3. Generate Sample Data

```bash
# Generate realistic sample data
python scripts/data_generation.py
```

**What this does:**
- Creates 5,000 customers
- Generates 200 products
- Creates 20,000 sales transactions
- Generates delivery data
- Saves CSV files in `data/raw/`

**Expected output:**
```
======================================================================
BLINKIT ANALYSIS DASHBOARD - DATA GENERATOR
======================================================================

[1/4] Generating 5000 customers...
✓ Generated 5000 customers

[2/4] Generating 200 products...
✓ Generated 200 products across 6 categories

[3/4] Generating 20000 sales transactions...
✓ Generated 20000 sales transactions
  - Average order value: ₹485.23
  - Total revenue: ₹9,704,600.00

[4/4] Generating delivery data...
✓ Generated 18500 delivery records
  - Average delivery time: 12.3 minutes
  - On-time delivery rate: 94.5%

✅ Data generation complete!
```

**Runtime:** ~30 seconds

#### 4. (Optional) Clean Data

```bash
# Clean and preprocess data
python scripts/data_cleaning.py
```

This creates cleaned datasets in `data/processed/`

#### 5. Open Power BI Dashboard

**If you don't have Power BI Desktop:**
1. Download from [Microsoft](https://powerbi.microsoft.com/desktop/)
2. Install (it's free!)
3. Launch Power BI Desktop

**Open the Dashboard:**
1. Navigate to `powerbi/` folder
2. Double-click `Blinkit_Dashboard.pbix`
3. Power BI Desktop will open

**First Time Setup:**
1. Click **Home** → **Transform Data**
2. In Power Query Editor, click **Close & Apply**
3. Click **Home** → **Refresh**
4. Wait for data to load (~10 seconds)

**You're done!** 🎉

---

## 🎯 Quick Tour

### Dashboard Pages

**Page 1: Executive Overview**
- Total Revenue, Orders, AOV
- Revenue trends
- Category breakdown

**Page 2: Customer Analytics**
- Customer segmentation
- Purchase patterns
- Retention metrics

**Page 3: Product Performance**
- Top products
- Category analysis
- Inventory status

**Page 4: Delivery Operations**
- Delivery time analysis
- On-time rate
- Regional performance

**Page 5: Regional Analysis**
- Sales by city
- Demand heatmap
- Growth trends

### Try These Interactions

1. **Filter by Date**
   - Use date slicer at top
   - Select last 30 days

2. **Filter by City**
   - Click on any city in charts
   - All visuals update automatically

3. **Drill Down**
   - Right-click on any data point
   - Select "Drill through"

4. **Export Data**
   - Click on any visual
   - Click **...** → **Export data**

---

## 📊 Sample Insights

After opening the dashboard, you'll see:

**Revenue Metrics:**
- Total Revenue: ~₹97L
- Average Order Value: ₹485
- Total Orders: 20,000

**Customer Metrics:**
- Total Customers: 5,000
- Retention Rate: ~65%
- Repeat Customers: ~3,250

**Delivery Metrics:**
- Average Delivery Time: 12.3 min
- On-Time Rate: 94.5%
- Total Deliveries: 18,500

**Top Categories:**
1. Dairy & Breakfast (35%)
2. Fruits & Vegetables (22%)
3. Snacks & Beverages (18%)

---

## 🔧 Troubleshooting

### Issue: "Python not found"
```bash
# Check Python installation
python --version

# If not installed, download from python.org
```

### Issue: "pip not found"
```bash
# Use python -m pip instead
python -m pip install -r requirements.txt
```

### Issue: "Module not found"
```bash
# Install specific package
pip install pandas numpy faker matplotlib seaborn
```

### Issue: "Power BI won't open .pbix file"
- Ensure Power BI Desktop is installed
- Try right-click → Open with → Power BI Desktop
- Check file isn't corrupted (re-download if needed)

### Issue: "No data in dashboard"
1. Check if CSV files exist in `data/raw/`
2. Run `python scripts/data_generation.py` again
3. In Power BI, click **Refresh**

### Issue: "Dashboard is slow"
1. Reduce date range filter
2. Close other applications
3. Use a more powerful computer
4. Reduce data volume (edit data_generation.py)

---

## 💡 Next Steps

### Customize the Data

**Edit `scripts/data_generation.py`:**

```python
# Change these values
NUM_CUSTOMERS = 10000  # More customers
NUM_PRODUCTS = 500     # More products
NUM_ORDERS = 50000     # More orders
```

Then regenerate:
```bash
python scripts/data_generation.py
```

### Use Your Own Data

1. **Prepare CSV files** with these columns:

**sales_data.csv:**
- OrderID, CustomerID, OrderDateTime, TotalAmount, etc.

**customer_data.csv:**
- CustomerID, Name, Email, City, etc.

**product_data.csv:**
- ProductID, ProductName, Category, Price, etc.

2. **Place in `data/raw/`**

3. **Open Power BI** and refresh

### Learn Power BI

**Free Resources:**
- [Microsoft Learn - Power BI](https://docs.microsoft.com/learn/powerbi/)
- [Power BI YouTube Channel](https://www.youtube.com/user/mspowerbi)
- [DAX Guide](https://dax.guide/)

**Recommended Courses:**
- Power BI Desktop for Business Intelligence
- DAX Fundamentals
- Data Modeling in Power BI

---

## 📚 Documentation

- **[README.md](README.md)** - Full project documentation
- **[DASHBOARD_GUIDE.md](DASHBOARD_GUIDE.md)** - How to use the dashboard
- **[DAX_measures.txt](powerbi/DAX_measures.txt)** - Custom formulas
- **[recommendations.md](reports/recommendations.md)** - Business insights

---

## 🎓 Learning Path

### Beginner (Week 1)
- ✅ Set up dashboard
- ✅ Explore all pages
- ✅ Try filters and slicers
- ✅ Export some data

### Intermediate (Week 2-3)
- ✅ Understand DAX measures
- ✅ Modify existing visuals
- ✅ Create new visuals
- ✅ Customize colors/themes

### Advanced (Week 4+)
- ✅ Create custom measures
- ✅ Build new pages
- ✅ Implement drill-through
- ✅ Add bookmarks
- ✅ Publish to Power BI Service

---

## 🆘 Get Help

**Issues with setup?**
- Check [Troubleshooting](#troubleshooting) section
- Open GitHub issue
- Email: akratimishra366@gmail.com

**Want to contribute?**
- Fork the repository
- Make improvements
- Submit pull request

---

## ✅ Checklist

Before you start:
- [ ] Python 3.8+ installed
- [ ] Power BI Desktop installed
- [ ] Repository cloned/downloaded
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Sample data generated (`python scripts/data_generation.py`)
- [ ] Dashboard opened in Power BI
- [ ] Data refreshed

You're ready to analyze! 🚀

---

## 🎉 Success!

If you can see the dashboard with data, you're all set!

**What to do next:**
1. Explore all 5 dashboard pages
2. Try different filters
3. Export some insights
4. Read the [Dashboard Guide](DASHBOARD_GUIDE.md)
5. Check [Business Recommendations](reports/recommendations.md)

**Share your success:**
- Star the repository ⭐
- Share on LinkedIn
- Tag @Akrati36

---

**Happy Analyzing! 📊**

Questions? Open an issue or email akratimishra366@gmail.com