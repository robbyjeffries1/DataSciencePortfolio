# Data Visualization with ggplot
# Modifying the Background
# Video 3.1

# Load the dataset as described in Video 1.3
library(tidyverse)
college <- read_csv('http://672258.youcanlearnit.net/college.csv')
college <- college %>%
  mutate(state=as.factor(state), region=as.factor(region),
         highest_degree=as.factor(highest_degree),
         control=as.factor(control), gender=as.factor(gender),
         loan_default_rate=as.numeric(loan_default_rate))

# Create the bar graph from Video 2.3
ggplot(data=college) +
  geom_bar(mapping=aes(x=region, fill=control))




