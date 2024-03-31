In the early stages of the COVID-19 vaccination rollout in Denmark, only certain groups of people were offered vaccines due to limited supply. 
However, for people who were still waiting to receive their vaccination invitation, it was possible to sign up to a daily wait list for leftover vaccines on the website of their region.
The wait list was reset daily, meaning that people had to enter their details again and again in order to be on the list.

To avoid having to do this manually every day, I wrote this Python script which automates the process for Region Nordjylland.
The script visits the wait list sign-up webpage, checks of some specified locations are doing vaccinations on the current date, and if so, submits the user's specified details.

Since COVID-19 vaccines became widely available, this "leftover vaccines" offer (and the website) no longer exists.
