import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
                        "http://vignette4.wikia.nocookie.net/pixar/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20160329080002",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     "http://intlportal2.s3.foxfilm.com/intlportal2/56ba791b20287.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

annabelle_creations = media.Movie("Annabelle Creations",
                                  "Former toy maker Sam Mullins and his wife, Esther,are happy to welcome a nun and six orphaned girls into their California farmhouse. Years earlier, the couple's 7-year-old daughter Annabelle died in a tragic car accident. Terror soon strikes when one child sneaks into a forbidden room and finds a seemingly innocent doll that appears to have a life of its own.",
                                  "https://i1.wp.com/bloody-disgusting.com/wp-content/uploads/2017/03/ANNABELLE-CREATION-POSTER.jpg?resize=691%2C1024",
                                  "https://www.youtube.com/watch?v=KisPhy7T__Q")
it = media.Movie("It",
                 "Seven young outcasts in Derry, Maine, are about to face their worst nightmare -- an ancient, shape-shifting evil that emerges from the sewer every 27 years to prey on the town's children. Banding together over the course of one horrifying summer, the friends must overcome their own personal fears to battle the murderous, bloodthirsty clown known as Pennywise.",
                 "https://i.pinimg.com/736x/3e/33/92/3e3392d339c2b8028007d0f9af979be4---movies-it-movie-.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")

simran = media.Movie("Simran",
                     "A Gujarati housekeeping lady in the US allows ambition to get the better of her & gets involved in a world of crime. Simran is a racy, fun film with Kangana Ranaut playing the titular role.",
                     "https://cdn.pinkvilla.com/files/SimranPoster.jpg",
                     "https://www.youtube.com/watch?v=_LUe4r6eeQA")

logan = media.Movie("Logan",
                    "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant (Dafne Keen) who is very much like him. Logan must now protect the girl and battle the dark forces that want to capture her.",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5CYQBjtbAMg5wyQirPA_vIC_41-KwjaogMdFg3YL9ADz9T2DUpg",
                    "https://www.youtube.com/watch?v=gbug3zTm3Ws")

movies = [toy_story, avatar, annabelle_creations, it, logan, simran]
fresh_tomatoes.open_movies_page(movies)
