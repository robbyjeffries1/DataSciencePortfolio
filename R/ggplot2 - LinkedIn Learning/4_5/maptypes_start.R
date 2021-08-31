# Data Visualization with ggplot
# Changing Map Types
# Video 4.5

library(tidyverse)
library(ggmap)

# Insert your own API key here
register_google(key="YOUR_API_KEY_HERE")

# Pull up a map of New York City again
nyc <- geocode("New York, NY")
ggmap(get_map(nyc))

