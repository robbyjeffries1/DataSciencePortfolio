# Data Visualization with ggplot
# Plotting Points on a Map
# Video 4.6

library(tidyverse)
library(ggmap)

# Insert your own API key here
register_google(key="YOUR_API_KEY_HERE")

# Geocode a few locations
nyc <- geocode("New York, NY")
usa <- geocode("United States")
