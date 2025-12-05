# 📊 Blinkit Dashboard User Guide

Complete guide to using the Blinkit Analysis Dashboard in Power BI.

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Pages](#dashboard-pages)
3. [Key Metrics](#key-metrics)
4. [Interactive Features](#interactive-features)
5. [Filters & Slicers](#filters--slicers)
6. [Drill-Through Pages](#drill-through-pages)
7. [Exporting Data](#exporting-data)
8. [Troubleshooting](#troubleshooting)

---

## 🚀 Getting Started

### Opening the Dashboard

1. **Install Power BI Desktop** (if not already installed)
   - Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
   - Free version is sufficient

2. **Open the Dashboard File**
   - Navigate to `powerbi/Blinkit_Dashboard.pbix`
   - Double-click to open in Power BI Desktop

3. **Refresh Data** (if needed)
   - Click **Home** → **Refresh**
   - Wait for data to load

### First-Time Setup

1. **Check Data Connections**
   - Go to **Home** → **Transform Data**
   - Verify all queries are loading correctly
   - Close & Apply

2. **Set Date Range**
   - Use the date slicer on each page
   - Default: Last 12 months

---

## 📄 Dashboard Pages

### Page 1: Executive Overview

**Purpose:** High-level business performance snapshot

**Key Visuals:**
- 📊 **KPI Cards** - Revenue, Orders, AOV, Retention
- 📈 **Revenue Trend** - Monthly revenue line chart
- 🥧 **Category Mix** - Revenue by product category
- 📉 **Order Status** - Completed vs Cancelled

**How to Use:**
1. View overall performance at a glance
2. Check if targets are being met
3. Identify trends over time
4. Compare current vs previous periods

**Filters Available:**
- Date Range
- City
- Customer Segment
- Order Status

---

### Page 2: Customer Analytics

**Purpose:** Deep dive into customer behavior and segmentation

**Key Visuals:**
- 👥 **Customer Segmentation** - RFM analysis scatter plot
- 📊 **Purchase Patterns** - Heatmap by day/hour
- 💰 **Customer Lifetime Value** - Distribution chart
- 🔄 **Retention Funnel** - New vs Repeat customers

**How to Use:**
1. **Identify High-Value Customers**
   - Look at Champions segment (top-right in RFM chart)
   - Note their characteristics

2. **Understand Purchase Patterns**
   - Check heatmap for peak times
   - Plan inventory and staffing accordingly

3. **Track Retention**
   - Monitor repeat customer percentage
   - Identify at-risk customers

**Filters Available:**
- Date Range
- City
- Customer Segment
- Registration Date

**Insights to Look For:**
- Which customer segments generate most revenue?
- What are peak shopping hours?
- How many customers are at risk of churning?

---

### Page 3: Product Performance

**Purpose:** Analyze product sales and inventory

**Key Visuals:**
- 🏆 **Top Products** - Best sellers by revenue
- 📦 **Category Performance** - Sales by category
- 📈 **Product Trends** - Trending items
- 💹 **Profit Margin** - High vs low margin products

**How to Use:**
1. **Identify Best Sellers**
   - Check top 10 products table
   - Ensure adequate stock levels

2. **Analyze Categories**
   - See which categories drive revenue
   - Identify underperforming categories

3. **Monitor Inventory**
   - Check stock status indicators
   - Plan restocking for popular items

**Filters Available:**
- Date Range
- Category
- Brand
- Stock Status

**Actions to Take:**
- Stock up on top sellers
- Promote slow-moving items
- Adjust pricing for low-margin products

---

### Page 4: Delivery Operations

**Purpose:** Monitor delivery efficiency and performance

**Key Visuals:**
- ⏱️ **Delivery Time Distribution** - Histogram
- 🎯 **On-Time Rate** - Gauge chart
- 🗺️ **Regional Performance** - Map visualization
- 👤 **Partner Performance** - Delivery partner metrics

**How to Use:**
1. **Track Delivery Speed**
   - Check average delivery time
   - Identify slow delivery areas

2. **Monitor On-Time Performance**
   - Target: 95%+ on-time delivery
   - Investigate areas below target

3. **Evaluate Partners**
   - Compare delivery partner performance
   - Reward top performers

**Filters Available:**
- Date Range
- City
- Area
- Delivery Partner
- Time Segment

**KPIs to Monitor:**
- Average delivery time: <15 minutes
- On-time rate: >95%
- Customer rating: >4.5/5

---

### Page 5: Regional Analysis

**Purpose:** Geographic performance insights

**Key Visuals:**
- 🗺️ **Sales Map** - Revenue by location
- 📊 **City Comparison** - Bar chart
- 🔥 **Demand Heatmap** - High-demand areas
- 📈 **Regional Growth** - Trend analysis

**How to Use:**
1. **Identify Top Markets**
   - See which cities generate most revenue
   - Focus expansion efforts

2. **Find Growth Opportunities**
   - Look for underserved areas
   - Plan new dark stores

3. **Optimize Coverage**
   - Ensure adequate delivery coverage
   - Reduce delivery times in key areas

**Filters Available:**
- Date Range
- City
- Area
- Pincode

---

## 🎯 Key Metrics Explained

### Revenue Metrics

**Total Revenue**
- Sum of all completed orders
- Excludes cancelled orders
- Formula: `SUM(TotalAmount) WHERE Status = 'Completed'`

**Average Order Value (AOV)**
- Revenue per order
- Formula: `Total Revenue / Total Orders`
- Target: ₹500+

**Month-over-Month Growth**
- Revenue change vs previous month
- Formula: `(Current Month - Previous Month) / Previous Month * 100`
- Target: 10%+ growth

### Customer Metrics

**Customer Retention Rate**
- Percentage of repeat customers
- Formula: `Repeat Customers / Total Customers * 100`
- Target: 60%+

**Customer Lifetime Value (CLV)**
- Average revenue per customer
- Formula: `Total Revenue / Total Customers`
- Target: ₹5,000+

### Operational Metrics

**On-Time Delivery Rate**
- Orders delivered within 15 minutes
- Formula: `On-Time Deliveries / Total Deliveries * 100`
- Target: 95%+

**Order Fulfillment Rate**
- Successfully completed orders
- Formula: `Completed Orders / Total Orders * 100`
- Target: 98%+

---

## 🎛️ Interactive Features

### Slicers (Filters)

**Date Range Slicer**
- Select custom date range
- Quick selections: Last 7 days, Last 30 days, Last 90 days
- Location: Top of each page

**City Slicer**
- Filter by specific cities
- Multi-select enabled
- Location: Left sidebar

**Category Slicer**
- Filter by product category
- Useful for category-specific analysis
- Location: Product Performance page

### Cross-Filtering

**How it Works:**
- Click on any visual element
- Other visuals automatically filter
- Example: Click "Bangalore" in city chart → All visuals show Bangalore data

**To Clear Filters:**
- Click the filter icon in top-right
- Select "Clear all filters"
- Or press Ctrl + Click on selected element

### Drill-Through

**Customer Details:**
1. Right-click on any customer segment
2. Select "Drill through" → "Customer Details"
3. View detailed customer information

**Product Details:**
1. Right-click on any product
2. Select "Drill through" → "Product Details"
3. See sales history and trends

---

## 📥 Exporting Data

### Export to Excel

1. Click on any visual
2. Click **...** (More options)
3. Select **Export data**
4. Choose **Summarized data** or **Underlying data**
5. Save as Excel file

### Export to PDF

1. Go to **File** → **Export** → **Export to PDF**
2. Select pages to export
3. Choose quality settings
4. Save PDF

### Export to PowerPoint

1. Go to **File** → **Export** → **Export to PowerPoint**
2. Dashboard pages become slides
3. Visuals remain interactive in PowerPoint

---

## 🔧 Troubleshooting

### Data Not Loading

**Problem:** Visuals show "No data available"

**Solutions:**
1. Check data source connections
2. Refresh data: **Home** → **Refresh**
3. Verify file paths in Power Query
4. Ensure CSV files are in correct location

### Slow Performance

**Problem:** Dashboard is slow or laggy

**Solutions:**
1. Reduce date range filter
2. Close other applications
3. Optimize data model (remove unused columns)
4. Use aggregated data instead of row-level

### Incorrect Calculations

**Problem:** Numbers don't match expectations

**Solutions:**
1. Check filter context
2. Verify DAX measure formulas
3. Ensure relationships are correct
4. Check for duplicate data

### Visuals Not Updating

**Problem:** Changes not reflecting in visuals

**Solutions:**
1. Click **Refresh** button
2. Check if filters are applied
3. Verify data source is updated
4. Close and reopen Power BI

---

## 💡 Best Practices

### Daily Use

1. **Morning Review**
   - Check yesterday's performance
   - Review on-time delivery rate
   - Identify any issues

2. **Weekly Analysis**
   - Compare week-over-week trends
   - Review top products
   - Check customer retention

3. **Monthly Planning**
   - Analyze monthly performance
   - Set targets for next month
   - Review regional growth

### Tips for Better Insights

1. **Use Date Comparisons**
   - Always compare to previous period
   - Look for trends, not just numbers

2. **Segment Your Analysis**
   - Don't just look at totals
   - Break down by city, category, time

3. **Focus on Actionable Metrics**
   - Identify what you can control
   - Set realistic targets

4. **Share Insights**
   - Export key findings
   - Share with stakeholders
   - Drive data-driven decisions

---

## 📞 Support

### Need Help?

- **Documentation:** Check README.md
- **DAX Formulas:** See DAX_measures.txt
- **Issues:** Open GitHub issue
- **Email:** akratimishra366@gmail.com

---

## 🎓 Learning Resources

### Power BI Tutorials
- [Microsoft Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [Power BI Community](https://community.powerbi.com/)
- [DAX Guide](https://dax.guide/)

### Dashboard Design
- [Power BI Best Practices](https://docs.microsoft.com/power-bi/guidance/)
- [Dashboard Design Principles](https://www.tableau.com/learn/articles/dashboard-design-principles)

---

**Happy Analyzing! 📊**