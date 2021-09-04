# Data Visualization with ggplot
# Geocoding Points
# Video 4.4

library(tidyverse)
library(ggmap)

# Insert your API key below
register_google(key="AIzaSyA7abR6711_8hmR_kUKMMx0UKWFyNEYoNI")

nyc <- geocode("New York, NY")
nyc

lynda <- geocode("Lynda.com")
lynda

whitehouse <- geocode("white House")
whitehouse

nyc_map <- get_map(nyc)
ggmap(nyc_map)

ggmap(get_map(lynda))

whitehouse_map <- ggmap(get_map(whitehouse, zoom=18))
whitehouse_map
