insert into artists (name)
	values  ('Bob Marley'), 
			('Metallica'), 
			('Tupac Shakur'), 
			('Lady Gaga');
		
insert into genres (name)
	values  ('Pop'), 
			('Metal'), 
			('Rap'), 
			('Reggie');
		
insert into genresartists
	values (1,4), (4,1), (1,2), (2,2), (3,3);

insert into albums (name, year)
	values  ('Sun Is Shining', '2011-01-01'),
			('Ride the lightning', '1984-01-01'),
			('Born This Way', '2011-01-01'),
			('Gaga 2020', '2020-01-01');
		
insert into albumsartists (albums_id, artists_id)
	values  (1,1), (2,2), (3,4), (4,4)

insert into tracks (name, length, album_id)
    values  ('Keep on Moving', '00:05:12', 1);
	        ('Dont Rock My Boat', '00:02:22', 1),
			('Fight Fire With Fire', '00:11:22', 2),
			('For Whom The Bell Tolls', '00:03:03', 2),
			('Judas', '00:02:02', 3),
			('Scheiße', '00:05:01', 3)
			('Let my people go', '00:03:12', 3),
			('One and only', '00:03:33', 4);

insert into collections (name, year)
	values  ('Romantic collection', '1999-01-01'),
			('Rock this dancefloor', '2021-01-01'),
			('Best of 20th Centurty', '2000-01-01'),
			('All time hits', '2022-01-01');
			('My 2019', '2019-01-01')

insert into trackscollections (tracks_id, collections_id)
	values (3,4), (4,2), (4,3), (4,4), (5,2), (6,1);
			
	
	
