# E-Commerce Revenue Leakage & Retention Analysis



## Project Overview

This project analyzes an e-commerce platform to understand why customers don’t return and where revenue is being lost. The analysis uncovered two critical business problems — a severe customer retention issue and significant revenue loss from a specific promotional code.

## Tools Used

- Python (Pandas) — data cleaning and feature engineering
- Power BI — dashboard and visualization
- Dataset: E-commerce transaction records

## Business Question

Why are customers not returning and where is revenue being lost?

## Data Cleaning & Engineering

- Created customer order count per unique user
- Segmented customers into One-Time Buyers vs Repeat Customers
- Flagged valid vs cancelled transactions to isolate actual revenue

## Key Findings

**Finding 1 — Customer Retention Crisis:**

- 98.17% of customers never returned after their first purchase
- Only 1.83% made repeat purchases
- Business growth depends entirely on expensive new customer acquisition

**Finding 2 — Revenue Loss:**

|Metric                 |Amount    |
|-----------------------|----------|
|Gross Revenue          |$1,260,000|
|Actual Retained Revenue|$988,370  |
|Lost Revenue           |$271,630  |

- WINTER15 promotional code showed unusually high correlation with cancelled orders
- Likely caused by discount-driven non-committal purchasing behavior

## Business Recommendations

1. Temporarily suspend WINTER15 coupon code and investigate cancellation pattern
1. Implement email follow-up sequence targeting first-time buyers within 14 days of purchase — converting even 5% to repeat customers would significantly reduce acquisition costs
1. Shift portion of acquisition budget toward retention marketing

## Dashboard

# Dashboard.png 

## Dataset Source

Kaggle — E-commerce transactions dataset
