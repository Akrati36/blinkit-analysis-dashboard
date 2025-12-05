# 📊 Blinkit Analysis Dashboard

An interactive **Power BI dashboard** providing end-to-end visibility into customer behavior, product performance, and delivery operations for Blinkit (formerly Grofers).

![Dashboard](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Data%20Processing-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

---

## 🎯 Project Overview

This project delivers a comprehensive business intelligence solution for Blinkit, consolidating raw sales, customer, and logistics data into clear, actionable visualizations for management review.

### Key Objectives
- 📈 **Customer Behavior Analysis** - Understand purchasing patterns and preferences
- 🛍️ **Product Performance Tracking** - Identify top-performing and underperforming products
- 🚚 **Delivery Operations Monitoring** - Track delivery efficiency and logistics metrics
- 🎯 **Growth Opportunities** - Highlight areas for business expansion
- ⚠️ **Operational Bottlenecks** - Identify and resolve inefficiencies

---

## 🌟 Dashboard Features

### 1. Executive Summary
- **Total Revenue** - Overall sales performance
- **Total Orders** - Order volume trends
- **Average Order Value (AOV)** - Customer spending patterns
- **Customer Retention Rate** - Loyalty metrics
- **Delivery Success Rate** - Operational efficiency

### 2. Customer Analytics
- **Customer Segmentation** - RFM (Recency, Frequency, Monetary) analysis
- **Purchase Behavior** - Time-based patterns (hourly, daily, weekly)
- **Customer Lifetime Value (CLV)** - Long-term value prediction
- **Churn Analysis** - At-risk customer identification
- **Geographic Distribution** - Regional customer density

### 3. Product Performance
- **Top Selling Products** - Best performers by revenue and volume
- **Category Analysis** - Performance by product category
- **Product Trends** - Seasonal and trending items
- **Inventory Turnover** - Stock movement efficiency
- **Profit Margin Analysis** - High-margin vs low-margin products

### 4. Delivery Operations
- **Delivery Time Analysis** - Average delivery duration
- **On-Time Delivery Rate** - Punctuality metrics
- **Regional Performance** - Area-wise delivery efficiency
- **Peak Hours Analysis** - High-demand time slots
- **Delivery Partner Performance** - Individual rider metrics

### 5. Regional Insights
- **Sales by Region** - Geographic revenue distribution
- **Demand Heatmap** - High-demand areas visualization
- **Regional Growth** - Area-wise growth trends
- **Market Penetration** - Coverage analysis

---

## 📁 Project Structure

```
blinkit-analysis-dashboard/
├── data/
│   ├── raw/                      # Raw data files
│   │   ├── sales_data.csv
│   │   ├── customer_data.csv
│   │   ├── product_data.csv
│   │   └── delivery_data.csv
│   ├── processed/                # Cleaned data
│   │   └── blinkit_consolidated.csv
│   └── sample/                   # Sample datasets
│       └── sample_data.xlsx
├── scripts/
│   ├── data_generation.py       # Generate sample data
│   ├── data_cleaning.py         # Data preprocessing
│   ├── analysis.py              # Statistical analysis
│   └── visualizations.py        # Python visualizations
├── powerbi/
│   ├── Blinkit_Dashboard.pbix   # Power BI dashboard file
│   ├── dashboard_screenshots/   # Dashboard images
│   └── DAX_measures.txt         # Custom DAX formulas
├── reports/
│   ├── insights_summary.pdf     # Key findings report
│   └── recommendations.md       # Business recommendations
├── images/
│   └── dashboard_preview.png    # Dashboard preview
├── README.md
├── DASHBOARD_GUIDE.md
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
- **Power BI Desktop** (Free download from Microsoft)
- **Python 3.8+** (for data generation and analysis)
- **Excel** (optional, for data viewing)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Akrati36/blinkit-analysis-dashboard.git
cd blinkit-analysis-dashboard
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Generate sample data**
```bash
python scripts/data_generation.py
```

4. **Open Power BI Dashboard**
- Open `powerbi/Blinkit_Dashboard.pbix` in Power BI Desktop
- Refresh data sources
- Explore the interactive dashboard

---

## 📊 Key Metrics & KPIs

### Business Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| **Total Revenue** | Sum of all sales | ₹10M+ monthly |
| **Average Order Value** | Revenue per order | ₹500+ |
| **Order Volume** | Total orders placed | 50K+ monthly |
| **Customer Retention** | Repeat customer rate | 60%+ |
| **Gross Margin** | Profit percentage | 25%+ |

### Operational Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| **Avg Delivery Time** | Order to delivery duration | <15 minutes |
| **On-Time Delivery** | Orders delivered on time | 95%+ |
| **Order Fulfillment Rate** | Successfully completed orders | 98%+ |
| **Delivery Partner Efficiency** | Orders per hour per rider | 4+ |

### Customer Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| **Customer Lifetime Value** | Total customer value | ₹5,000+ |
| **Churn Rate** | Customer attrition | <10% |
| **Net Promoter Score** | Customer satisfaction | 50+ |
| **Active Users** | Monthly active customers | 100K+ |

---

## 📈 Sample Insights

### Customer Behavior
- 🕐 **Peak ordering hours**: 7-9 PM (dinner time)
- 📅 **Highest order days**: Weekends (Saturday & Sunday)
- 💰 **Average basket size**: ₹450-550
- 🔄 **Repeat purchase rate**: 65% within 7 days

### Product Performance
- 🥛 **Top category**: Dairy & Breakfast (35% of revenue)
- 🍎 **Fast-moving**: Fresh Fruits & Vegetables
- 📦 **High margin**: Personal Care & Beauty
- 📉 **Slow-moving**: Gourmet & World Food

### Delivery Operations
- ⚡ **Average delivery time**: 12.5 minutes
- ✅ **On-time rate**: 94.2%
- 🗺️ **Best performing region**: South Delhi
- ⏰ **Peak delivery hours**: 8-10 PM

### Regional Insights
- 🏙️ **Top revenue city**: Bangalore (28%)
- 📍 **Highest demand areas**: Tech parks & residential complexes
- 🌱 **Fastest growing**: Tier-2 cities (45% YoY growth)

---

## 🎨 Dashboard Visualizations

### Page 1: Executive Overview
- **KPI Cards** - Revenue, Orders, AOV, Retention
- **Trend Lines** - Monthly revenue and order trends
- **Gauge Charts** - Target vs actual performance
- **Donut Charts** - Revenue by category

### Page 2: Customer Analytics
- **Scatter Plot** - RFM segmentation
- **Heat Map** - Purchase patterns by day/hour
- **Bar Charts** - Customer demographics
- **Line Charts** - Customer acquisition trends

### Page 3: Product Performance
- **Tree Map** - Product category contribution
- **Waterfall Chart** - Revenue breakdown
- **Column Charts** - Top 10 products
- **Matrix Table** - Detailed product metrics

### Page 4: Delivery Operations
- **Map Visualization** - Geographic delivery coverage
- **Funnel Chart** - Order fulfillment stages
- **Area Charts** - Delivery time distribution
- **KPI Indicators** - Operational efficiency

### Page 5: Regional Analysis
- **Filled Map** - Sales by region
- **Clustered Columns** - Regional comparison
- **Ribbon Chart** - Regional trends over time

---

## 🔍 Data Analysis Process

### 1. Data Collection
- Sales transactions data
- Customer profile information
- Product catalog and inventory
- Delivery logs and timestamps
- Geographic and demographic data

### 2. Data Cleaning
- Remove duplicates
- Handle missing values
- Standardize formats
- Validate data integrity
- Merge datasets

### 3. Data Transformation
- Create calculated columns
- Build date hierarchies
- Generate customer segments
- Calculate KPIs
- Create relationships

### 4. Visualization
- Design dashboard layout
- Create interactive filters
- Build drill-through pages
- Add tooltips
- Implement bookmarks

### 5. Insights Generation
- Identify trends and patterns
- Perform comparative analysis
- Generate recommendations
- Create executive summary

---

## 💡 Business Recommendations

### Growth Opportunities
1. **Expand in Tier-2 Cities** - 45% YoY growth potential
2. **Increase Evening Inventory** - Peak demand 7-9 PM
3. **Focus on High-Margin Categories** - Personal care & beauty
4. **Weekend Promotions** - Capitalize on high order volume

### Operational Improvements
1. **Optimize Delivery Routes** - Reduce average delivery time
2. **Increase Rider Capacity** - During peak hours (8-10 PM)
3. **Improve Inventory Management** - Reduce stockouts in fast-moving items
4. **Regional Warehouses** - Better coverage in high-demand areas

### Customer Retention
1. **Loyalty Programs** - Reward repeat customers
2. **Personalized Recommendations** - Based on purchase history
3. **Subscription Plans** - For frequent buyers
4. **Re-engagement Campaigns** - Target churned customers

---

## 🛠️ Technologies Used

- **Power BI Desktop** - Dashboard creation and visualization
- **Python** - Data generation and analysis
  - Pandas - Data manipulation
  - NumPy - Numerical operations
  - Matplotlib/Seaborn - Visualizations
  - Faker - Sample data generation
- **DAX** - Custom measures and calculations
- **Power Query** - Data transformation
- **Excel** - Data storage and initial analysis

---

## 📚 DAX Measures Examples

```dax
// Total Revenue
Total Revenue = SUM(Sales[Amount])

// Average Order Value
AOV = DIVIDE([Total Revenue], [Total Orders], 0)

// Customer Retention Rate
Retention Rate = 
DIVIDE(
    CALCULATE(DISTINCTCOUNT(Sales[CustomerID]), Sales[IsRepeatCustomer] = TRUE),
    DISTINCTCOUNT(Sales[CustomerID]),
    0
) * 100

// On-Time Delivery Rate
On-Time Delivery % = 
DIVIDE(
    CALCULATE(COUNT(Delivery[OrderID]), Delivery[IsOnTime] = TRUE),
    COUNT(Delivery[OrderID]),
    0
) * 100

// Month-over-Month Growth
MoM Growth % = 
VAR CurrentMonth = [Total Revenue]
VAR PreviousMonth = CALCULATE([Total Revenue], DATEADD(Calendar[Date], -1, MONTH))
RETURN
DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth, 0) * 100
```

---

## 📸 Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

*Interactive Power BI dashboard with multiple pages and drill-through capabilities*

---

## 🎯 Use Cases

### For Management
- Monitor overall business performance
- Track KPIs against targets
- Identify growth opportunities
- Make data-driven decisions

### For Operations Team
- Optimize delivery routes
- Manage inventory levels
- Improve fulfillment efficiency
- Track operational metrics

### For Marketing Team
- Understand customer segments
- Plan targeted campaigns
- Analyze product trends
- Optimize pricing strategies

### For Sales Team
- Identify top-performing products
- Track regional performance
- Forecast demand
- Plan inventory

---

## 📖 Documentation

- [Dashboard User Guide](DASHBOARD_GUIDE.md) - How to use the dashboard
- [Data Dictionary](docs/data_dictionary.md) - Field descriptions
- [DAX Formulas](powerbi/DAX_measures.txt) - Custom calculations
- [Insights Report](reports/insights_summary.pdf) - Key findings

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 👤 Author

**Akrati Mishra**
- GitHub: [@Akrati36](https://github.com/Akrati36)
- Email: akratimishra366@gmail.com
- LinkedIn: [Akrati Mishra](https://linkedin.com/in/akrati-mishra)

---

## 🙏 Acknowledgments

- Blinkit for inspiration
- Power BI community for resources
- Open-source data analysis tools

---

## 📞 Contact

For questions or feedback:
- Open an issue on GitHub
- Email: akratimishra366@gmail.com

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

**Built with ❤️ using Power BI and Python**

</div>