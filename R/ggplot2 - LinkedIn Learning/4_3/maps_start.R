# Data Visualization with ggplot
# Working with Map Data
# Video 4.3

library(tidyverse)
library(ggmap)

# Insert your own API key below
register_google(key="AIzaSyA7abR6711_8hmR_kUKMMx0UKWFyNEYoNI")

qmap("New York, NY", zoom=7)

nyc_map <- get_map("New York, NY", zoom=10)
ggmap(nyc_map)
