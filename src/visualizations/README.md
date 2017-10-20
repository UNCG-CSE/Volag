### Visualizations

Use plotly to create more visualizations of our data set. These can be used to better understand our data, any trends,
and the overall shapes of our observations.

We saw in our correlation analysis that there isn't very strong correlation between flight delays and weather features
(see ../flight\_weather\_correlation.ipynb)

We could use more visualizations to spot different trends in the data that may be more significant

Ideas:
- Create a map of all flight delays (use delay time as 'heat'?). This may help us better understand geographic trends of flight delays. Maybe we can start to focus on specific regions or climates?
    - This may also show that flight delays are equally prevalent everywhere, could indicate that weather is not
        that good of a predictor

- Plot flights delays vs. time (day-to-day, or month-to-month). Will we see that flight delays tend to happen at certain times of the year? If so, this _may_ mean that there is correlation to season (and perhaps weather). Otherwise, we might see that flight delays occur equally throughout the year, indicating that weather doesn't play a strong role.
