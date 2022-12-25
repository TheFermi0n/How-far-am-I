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
# fmt: off
# *-----------------------------------------------------------------
# User input required here

# adventurer details
adventurer_current_EXP = int(input("What is your current EXP? "))
adventurer_current_rank = int(input("What is your current Adventure Rank? "))
adventurer_desired_rank = int(input("What is your desired Adventure Rank? "))

# activity details for resin usage calculation
number_of_domain = int(input("How many domains you have cleared today? "))  # 20 resin per run
number_of_leyline = int(input("How many leyline blessings you have claimed today? "))  # 20 resin per run
number_of_weekly = int(input("How many weekly domains you have calimed today? "))  # 30 resin per run
number_of_elite = int(input("How many elite bosses you have killed today? "))  # 40 resin per run

# *-----------------------------------------------------------------
# fmt: on

# main process begins here, don't touch this area unless you want to add something
import pandas as pd
from IPython.display import Markdown, display
from datetime import datetime as dt
from datetime import timedelta as td


def printmd(string):
    display(Markdown(string))


todays_date = dt.today()

# fmt: off
rnk = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
nxt = [375,500,625,725,850,950,1075,1175,1300,1425,1525,1650,1775,1875,2000,2375,2500,2625,2775,2825,3425,3725,4000,4300,4575,4875,5150,5450,5725,6025,6300,6600,6900,7175,7475,7750,8050,8325,8625,10550,11525,12475,13450,14400,15350,16325,17275,18250,19200,26400,28800,31200,33600,36000,232350,258950,285750,312825,340125,"MAX"]
cum = [0,375,875,1500,2225,3075,4025,5100,6275,7575,9000,10525,12175,13950,15825,17825,20200,22700,25325,28100,30925,34350,38075,42075,46375,50950,55825,60975,66425,72150,78175,84475,91075,97975,105150,112625,120375,128425,136750,145375,155925,167450,179925,193375,207775,223125,239450,256725,274975,294175,320575,349375,380575,414175,450175,682525,941475,1227225,1540050,1880175]
# fmt: on

adventure_dict = {"rank": rnk, "next": nxt, "cummulative": cum}
adventure_rank_data = pd.DataFrame(adventure_dict, columns=["rank", "next", "cummulative"])

# resin usage categories
domain_EXP_per_20_resin = 100
leyline_EXP_per_20_resin = 100
weekly_EXP_per_30_resin = 300
elite_EXP_per_40_resin = 200


# consedering you have used condensed resin for domain and leylines.
yes_choices = ["yes", "y"]
no_choices = ["no", "n"]

while True:
    condensed_resin_used = input(
        "Have you used condensed resin for your domain and leylines? (yes/no): "
    )
    if condensed_resin_used.lower() in yes_choices:
        condensed_multiplier = 2
        break
    elif condensed_resin_used.lower() in no_choices:
        condensed_multiplier = 1
        break
    else:
        print("Type yes or no. You can also type y or n in short.")
        continue

# total resin used per day
resin_usage_per_day = (
    20 * condensed_multiplier * number_of_domain
    + 20 * condensed_multiplier * number_of_leyline
    + 30 * number_of_weekly
    + 40 * number_of_elite
)

# extracting required adventurer detials for available data
ar_des, _, exp_des = adventure_rank_data.loc[
    adventure_rank_data["rank"] == adventurer_desired_rank
].values[0]
ar_cur, next_ar_exp, exp_cur = adventure_rank_data.loc[
    adventure_rank_data["rank"] == adventurer_current_rank
].values[0]

resin_EXP_per_day = (
    condensed_multiplier * domain_EXP_per_20_resin * number_of_domain
    + condensed_multiplier * leyline_EXP_per_20_resin * number_of_leyline
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
    print()
    print("-------------------------------------------------------------------")
    print(f"\033[1mCurrent Details\033[0m")
    print(f"AR  = {adventurer_current_rank}")
    print(f"EXP = {adventurer_current_EXP} / {next_ar_exp}")

    print()
    print(f"\033[1mResin usage Details\033[0m")
    print(f"Number of Domains cleared per day = {number_of_domain}")
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
    print()
    print(
        """
    Note: This calculation is assuming that you're going to use
        the same amount of resin each day earned from the same categories 
        as per the values you entered today until you reach your desired adventure rank.
    """
    )
    print("-------------------------------------------------------------------")


# output
result_display()
