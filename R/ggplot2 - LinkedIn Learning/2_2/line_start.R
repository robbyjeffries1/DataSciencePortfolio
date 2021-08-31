# Data Visualization with ggplot
# Lines and Smoothers
# Video 2.2

# Load the dataset as described in Video 1.3
library(tidyverse)
college <- read_csv('http://672258.youcanlearnit.net/college.csv')
college <- college %>%
  mutate(state=as.factor(state), region=as.factor(region),
         highest_degree=as.factor(highest_degree),
         control=as.factor(control), gender=as.factor(gender),
         loan_default_rate=as.numeric(loan_default_rate))

# We had a nice plot of tuition vs. SAT scores when we worked with scatterplots
ggplot(data=college) +
  geom_point(mapping=aes(x=tuition, y=sat_avg, color=control))

