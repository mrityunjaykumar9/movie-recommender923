# Movie-recommender239
This is Movie_recommender which recommend movies according to user's choice. To visit this :  https://movie-reco239.herokuapp.com/


How to run project in local system :-
1. clone the project
2. open up in any python supporting IDE(like pycharm).
3. in terminal : pip install streamlit
4. in terminal : streamlit run app.py

--> In order to create this project i have used two IDE jupyter notebook and pycharm.

work in jupyter notebook:-
1. Preprocessing of dataset.
2. converting data of each movie into vector and find similarity in between.
3. With the help of sorting algorithm it recommend some most similar movie of user's choice.
4. store the required information in file with extension .pkl in write binary mode.

work in pycharm:-
1. create a virtual environment.
2. copy those .pkl file paste it in current folder.
3. I have used streamlit library for to create GUI.
4. With the help of API and movie_id it fetch the movie's information from TMDB site and render it to browser.


