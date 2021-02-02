# Imports
import csv
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import pandas as pd

# Defining df and finding all lists
df = pd.read_csv("StudentsPerformance.csv")
reading_score_list = df["reading score"]

# Figuring out mean, median, mode and standard deviation
mean_reading_score = statistics.mean(reading_score_list)
median_reading_score = statistics.median(reading_score_list)
mode_reading_score = statistics.mode(reading_score_list)
standard_deviation_reading_score = statistics.stdev(reading_score_list)

# 3 Standard deviation starts and ends
reading_score_first_std_deviation_start, reading_score_first_std_deviation_end = mean_reading_score - standard_deviation_reading_score, mean_reading_score + standard_deviation_reading_score
reading_score_second_std_deviation_start, reading_score_second_std_deviation_end = mean_reading_score - (2*standard_deviation_reading_score), mean_reading_score + (2*standard_deviation_reading_score)
reading_score_third_std_deviation_start, reading_score_third_std_deviation_end = mean_reading_score - (3*standard_deviation_reading_score), mean_reading_score + (3*standard_deviation_reading_score)

# 3 Lists of data in standard deviations
reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_score_second_std_deviation_start and result < reading_score_second_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_score_third_std_deviation_start and result < reading_score_third_std_deviation_end]

# Defining the figure
fig = ff.create_distplot([reading_score_list], ["reading score"], show_hist = False)

# Prints
print("The mean, median and mode of each student's reading score is {}, {} and {} respectively".format(mean_reading_score, median_reading_score, mode_reading_score))
print("The standard deviation of each student's reading score is " + str(standard_deviation_reading_score))
print("{}% of data for each student's reading score lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for each student's reading score lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for each student's reading score lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))