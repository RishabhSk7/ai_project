from the confusion matrix image, we can see 6,2 have a value of 10, which means, they get confused often. Similarly, 0,3 and 1,5 have a value of 5 and hence get confused often. This is likely because these sub datasets have matching features, which  results in the model being inaccurate in its prediction. Removing one subdataset from each pair results in higher accuracy, in this case we only remove "rock", i.e., 0 and "hiphop", i.e., 6. This is likely because the dataset is from auto generated playlists which have been tailored for me (Rishabh) specificly. This results in similar songs, that don't differ too much from each other, or repeated songs in playlists, which can lead to feature similarity between classes, ultimately leading to inaccuracy in our model. 