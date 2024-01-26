CREATE TABLE IF NOT exists Genres (
	id serial primary key,
	name varchar(32) not null
);

CREATE TABLE IF NOT exists Artists (
	id serial primary key,
	name varchar(32) not null
);

create table if not exists GenresArtists (
	genres_id integer references Genres(id),
	artists_id integer references Artists(id),
	constraint pk primary key (genres_id, artists_id)
);

CREATE TABLE IF NOT exists Albums (
	id serial primary key,
	name varchar(32) not null,
	year date not null
);

create table if not exists AlbumsArtists (
	albums_id integer references Albums(id),
	artists_id integer references Artists(id),
	constraint pkaa primary key (albums_id, artists_id)
);

CREATE TABLE IF NOT exists Tracks (
	id serial primary key,
	name varchar(32) not null,
	length time not null,
	album_id integer references Albums(id)
);


CREATE TABLE IF NOT exists Collections (
	id serial primary key,
	name varchar(32) not null,
	year date not null
);

create table if not exists TracksCollections (
	tracks_id integer references Tracks(id),
	collections_id integer references Collections(id),
	constraint pktc primary key (tracks_id, collections_id)
	);