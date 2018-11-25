# [What factors affect employment after bootcamp completion?](https://www.kaggle.com/chessybo/bootcamp-success-vs-age)

Do you use any free "learn to code" website to teach yourself programming? Clay used publicly available [survey data](https://github.com/freeCodeCamp/2016-new-coder-survey) taken by [FreeCodeCamp](https://www.freecodecamp.org/), to understand the demographic of self-taught coders.

## Data Analysis Insights
- A contribution to [issue #6](https://github.com/freeCodeCamp/2016-new-coder-survey/issues/36), "What factors affect employment after bootcamp completion?"
  - I [demonstrate](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/survey_plots.py) that older applicants are [decreasingly likely](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/bootcamp_job_normed.png) to get a job after bootcamp. (I normalized the graph since the [age distribution](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/bootcamp_attendance.png) was biased)
- How post bootcamp employment status after coding bootcamp affects whether a participant will reccomend doing a coding bootcamp.
  - predictably, those who get a job post bootcamp are [more likely](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/jobreccomend.png) to reccomend doing a bootcamp. I used SQL (sqllite3) to [demonstrate](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/post%20bootcamp%20employment%20status%20vs%20bootcamp%20reccomendation.py) there's [no correlation](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/age_sentiment_norm.png) between age and likelyhood of reccomending
- How does attending coding events correlate with employment status?
  - I did a ["sentiment analysis"](https://github.com/chessybo/Bootcamp-Survey-Data-Analysis/blob/master/survey_analysis_(attend%20coding%20events).py) of keywords in a free response survey answers.


## About the Data
The [survey](https://twitter.com/FreeCodeCamp/status/714930182721679360) was conducted anonymously and [published on the web](https://medium.freecodecamp.org/we-just-launched-the-biggest-ever-survey-of-people-learning-to-code-cac81dadf1ea) and promoted via social media from March 28 through May 2, 2016, targeting people who are relatively new to programming.

## Relevant Recent Data
- [Stack Overflow's 2016 Developer Survey](https://medium.freecodecamp.com/2-out-of-3-developers-are-self-taught-and-other-insights-from-stack-overflow-s-2016-survey-of-50-8cf0ee5d4c21#.yhlo2k5oz)
- [O'Reilly's 2016 Developer Salary Survey](https://medium.freecodecamp.org/5-000-developers-talk-about-their-salaries-d13ddbb17fb8?gi=446485605218#.umwcssab4)
