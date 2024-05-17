#import numpy as np

# Sale Prices and Counts
sale_price = 15 ## Alter when changing sale price
sales_count_quarterly = 500 ## Alter when quarterly amount sold changes
inventory_count_target = sales_count_quarterly * 1.2 ## Alter when changing % overage

# Operational Costs
wax_oz_per_candle = 8 ## Alter when changing jar size
wax_price_wholesale = 37 ## Alter when ordering new wax
wax_oz_wholesale = 160 ## Alter when ordering new wax
wax_price_per_oz = wax_price_wholesale / wax_oz_wholesale
wax_price_per_candle = wax_oz_per_candle * wax_price_per_oz

wick_per_candle = 1 ## Alter when changing wicks per candle
wick_price_wholesale = 5 ## Alter when ordering new wicks
wick_count_wholesale = 100 ## Alter when ordering new wicks
wick_price_per_candle = wick_price_wholesale / wick_count_wholesale

fragrance_oz_per_candle = wax_oz_per_candle * 0.05 ## Alter when changing fragrance concentration
fragrance_price_wholesale = 10 ## Alter when ordering new fragrances
fragrance_oz_wholesale = 4 ## Alter when ordering new fragrances
fragrance_price_per_oz = fragrance_price_wholesale / fragrance_oz_wholesale
fragrance_price_per_candle = fragrance_oz_per_candle * fragrance_price_per_oz

dye_oz_per_candle = wax_oz_per_candle * 0.005 ## Alter when changing dye concentration
dye_price_wholesale = 2 ## Alter when ordering new dye
dye_oz_wholesale = 20 ## Alter when ordering new dye
dye_price_per_oz = dye_price_wholesale / dye_oz_wholesale
dye_price_per_candle = dye_oz_per_candle * dye_price_per_oz

jar_price_wholesale = 10 ## Alter when ordering new jars
jar_count_wholesale = 12 ## Alter when ordering new jars
jar_price_per_candle = jar_price_wholesale / jar_count_wholesale

brand_label_price_wholesale = 13 ## Alter when ordering new brand labels
brand_label_count_wholesale = 16 ## Alter when ordering new brand labels
warning_label_price_wholesale = 3 ## Alter when ordering new warning labels
warning_label_count_wholesale = 100 ## Alter when ordering new warning labels
label_price_per_candle = (brand_label_price_wholesale / brand_label_count_wholesale) + \
                         (warning_label_price_wholesale / warning_label_count_wholesale)

labor_hours_per_batch = 2 ## Alter when changing time spent per batch
candles_per_batch = 6 ## Alter when changing batch size
hourly_rate = 20 ## Alter when changing hourly rate
rate_per_batch = labor_hours_per_batch * candles_per_batch * hourly_rate
rate_per_candle = rate_per_batch / 6

raw_materials_per_candle = wax_price_per_candle + wick_price_per_candle + fragrance_price_per_candle + \
                           dye_price_per_candle
raw_materials_quarterly = (wax_price_per_candle + wick_price_per_candle + fragrance_price_per_candle +
                           dye_price_per_candle) * inventory_count_target
packaging_materials_per_candle = jar_price_per_candle + label_price_per_candle
packaging_materials_quarterly = (jar_price_per_candle + label_price_per_candle) * inventory_count_target
labor_quarterly = rate_per_candle * inventory_count_target
marketing_quarterly = 400 ## Alter when changing marketing tactics
farmers_market_registration_quarterly = 65 / 4 ## Alter when farmers market registration fee changes

costs_quarterly = raw_materials_quarterly + packaging_materials_quarterly + \
                  marketing_quarterly + farmers_market_registration_quarterly

gross_profit_quarterly = (sale_price * sales_count_quarterly) - costs_quarterly
net_profit_quarterly = gross_profit_quarterly - costs_quarterly
net_profit_per_sale = net_profit_quarterly / sales_count_quarterly
net_profit_annual = net_profit_quarterly * 4
break_even_count = costs_quarterly / gross_profit_quarterly

# Start-up Costs
initial_candle_count = 50 ## Alter when initial batch size changes

equipment_initial = 200 ## Alter when initial equipment costs change
raw_materials_initial = (raw_materials_per_candle) * initial_candle_count
packaging_materials_initial = (packaging_materials_per_candle) * initial_candle_count
marketing_initial = 200 ## Alter when initial marketing costs change
farmers_market_registration = 65 ## Alter when initial farmers market registration fee changes
legal_initial = 500 ## Alter when initial legal fees change

costs_initial = equipment_initial + raw_materials_initial + packaging_materials_initial + marketing_initial + \
                legal_initial

# Summary
print(f"Initial Investment (Assuming {initial_candle_count} Initial Candles):${int(costs_initial)}")
print(f"Quarterly Gross Profit (Assuming {sales_count_quarterly} Quarterly Sales): ${int(gross_profit_quarterly)}")
print(f"Quarterly Operating Costs (Assuming {sales_count_quarterly} Quarterly Sales): ${int(costs_quarterly)}")
print(f"Quarterly Profit (Assuming {sales_count_quarterly} Quarterly Sales): ${int(net_profit_quarterly)}")
print(f"Break-even Sales Count: {break_even_count:.2f} sales per quarter")
print(f"Annual Profit: ${int(net_profit_annual)}")