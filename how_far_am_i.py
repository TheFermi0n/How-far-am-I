"""
How far am I?
A Python program to calculate how much time you
need to reach a certain AR level in Genshin Impact

author: Riasat
env details:
    compiler -- pyhton v3.8.15
    OS       -- macOS 13.1 arm64
    Kernel   -- Darwin 22.2.0
"""

# *-----------------------------------------------------------------
# User input required here

# adventurer details
adventurer_current_EXP = 141915
adventurer_current_rank = 55
adventurer_desired_rank = 56

# activity details for resin usage calculation
number_of_domain = 4
number_of_leyline = 0
number_of_weekly = 0
number_of_elite = 4

# *-----------------------------------------------------------------


# main process begins here, don't touch this area unless you want to add something
import pandas as pd
from IPython.display import Markdown, display
from datetime import datetime as dt
from datetime import timedelta as td


def printmd(string):
    display(Markdown(string))


todays_date = dt.today()
file_name = "ar_data.csv"

adventure_rank_data = pd.read_csv(file_name, delimiter="\t")

# resin usage categories
domain_EXP_per_20_resin = 100
leyline_EXP_per_20_resin = 100
weekly_EXP_per_30_resin = 300
elite_EXP_per_40_resin = 200

# total resin used per day
resin_usage_per_day = (
    20 * number_of_domain + 20 * number_of_leyline + 30 * number_of_weekly + 40 * number_of_elite
)

# extracting required adventurer detials for available data
ar_des, _, exp_des = adventure_rank_data.loc[
    adventure_rank_data["rank"] == adventurer_desired_rank
].values[0]
ar_cur, next_ar_exp, exp_cur = adventure_rank_data.loc[
    adventure_rank_data["rank"] == adventurer_current_rank
].values[0]

resin_EXP_per_day = (
    domain_EXP_per_20_resin * number_of_domain
    + leyline_EXP_per_20_resin * number_of_leyline
    + weekly_EXP_per_30_resin * number_of_weekly
    + elite_EXP_per_40_resin * number_of_elite
)

overall_comission_EXP = 500
inidvidual_comission_EXP = 250
daily_commission_EXP = overall_comission_EXP + (4 * inidvidual_comission_EXP)

exp_earned_per_day = daily_commission_EXP + resin_EXP_per_day
total_EXP_required = exp_des - exp_cur - adventurer_current_EXP
estimate_days = total_EXP_required / exp_earned_per_day

approximate_date = todays_date + td(days=estimate_days)


def result_display():
    print(f"\033[1mCurrent Details\033[0m")
    print(f"AR  = {adventurer_current_rank}")
    print(f"EXP = {adventurer_current_EXP} / {next_ar_exp}")
    print()
    print(f"\033[1mResin usage Details\033[0m")
    print(f"Number of Domians cleared per day = {number_of_domain}")
    print(f"Number of leyline blessings claimed per day = {number_of_leyline}")
    print(f"Number of weekly boss killed = {number_of_weekly}")
    print(f"Number of elite boss reward claimed per day = {number_of_elite}")
    print()
    print(f"Total resin used per day = {resin_usage_per_day}")
    print(f"Total resin EXP earned per day = {resin_EXP_per_day}")
    print()
    print(f"\033[1mCalculated Result\033[0m")
    print(f"Total Exp required: {total_EXP_required}")
    print(f"Estimate time to reach AR {adventurer_desired_rank}: {round(estimate_days)} days")
    print(f"Approximate date: {approximate_date.strftime('%a %b %d,%Y %H:%M:%S')}")


# output
result_display()
