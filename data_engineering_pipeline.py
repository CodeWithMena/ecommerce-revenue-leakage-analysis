import pandas as pd

def run_data_pipeline(file_path):
    """
    Executes the data engineering pipeline for the E-Commerce Revenue Analysis.
    Cleans raw transaction logs and engineers customer retention & revenue validity flags.
    """
    print("🚀 Initializing Data Pipeline...")
    
    # 1. Load the raw data
    df = pd.read_csv(file_path)
    print(f"📊 Successfully loaded {len(df)} transactional records.")
    
    # 2. Engineer Customer Lifetime Order Counts
    # Group by Email to find out exactly how many times each customer has purchased
    df['UserLifetimeOrders'] = df.groupby('Email')['Email'].transform('count')
    
    # 3. Create 'CustomerSegment' Logic
    # 98.17% of the dataset consists of One-Time Buyers, highlighting a massive retention crisis
    df['CustomerSegment'] = df['UserLifetimeOrders'].apply(
        lambda x: 'One-Time Buyer' if x == 1 else 'Repeat Customer'
    )
    
    # 4. Create 'IsRevenueValid' Logic
    # Isolate actual retained cash from cancelled orders to track coupon cannibalization
    df['IsRevenueValid'] = df['OrderStatus'].apply(
        lambda x: 0 if x.strip().lower() == 'cancelled' else 1
    )
    
    print("✅ Feature engineering complete. Segments and Revenue Flags mapped.")
    
    # 5. Export cleaned dataset for Power BI ingestion
    output_path = "cleaned_ecommerce_data.csv"
    df.to_csv(output_path, index=False)
    print(f"💾 Cleaned data successfully exported to: {output_path}")
    
    return df

if __name__ == "__main__":
    # Replace this string with your local file path when executing locally
    DATA_PATH = "raw_ecommerce_data.csv" 
    try:
        run_data_pipeline(DATA_PATH)
    except FileNotFoundError:
        print("⚠️ Note: Run this script locally by pointing DATA_PATH to your raw data file.")