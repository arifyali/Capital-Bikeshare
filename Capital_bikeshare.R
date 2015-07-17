setwd("~/Dropbox/Capital-Bikeshare/")
Q1_bikeshare = read.csv("2015-Q1-Trips-History-Data.csv")
total_duration_seconds = Q1_bikeshare[1]*0.001
sum(total_duration_seconds<60)
