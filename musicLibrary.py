def music(song):

    songs ={
    "skyfall":"https://www.youtube.com/watch?v=DeumyOzKqgI",
    "countingstars":"https://www.youtube.com/watch?v=hT_nvWreIhg",
    "shapeofyou":"https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "perfect":"https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "snowman":"https://www.youtube.com/watch?v=gset79KMmt0",
    "beliver":"https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "uddtapunjab":"https://www.youtube.com/watch?v=JgH3zj1K9Bw",
    "tumhiho":"https://www.youtube.com/watch?v=QW1Gd6vXcZI",
    }
    return songs.get(song.lower())