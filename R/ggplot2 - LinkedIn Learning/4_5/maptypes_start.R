# Data Visualization with ggplot
# Changing Map Types
# Video 4.5

library(tidyverse)
library(ggmap)

# Insert your own API key here
register_google(key="AIzaSyA7abR6711_8hmR_kUKMMx0UKWFyNEYoNI")

# Pull up a map of New York City again
nyc <- geocode("New York, NY")
ggmap(get_map(nyc, maptype = "terrain-lines"))

