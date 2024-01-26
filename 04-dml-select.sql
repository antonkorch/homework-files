select name, length from tracks 
	where length = (select max(length) from tracks)

select name from tracks
	where length > '00:03:30'

select name, year from collections
	where year between '2018-01-01' and '2020-12-31'

select name from artists
	where name not like '% %'

select name from tracks
	where name like '%my%' or 
		  name like	'%мой%'

	
select name, count(ga.artists_id) from genres g 
left join genresartists ga on g.id = ga.genres_id 
	group by name

select count(t.name) from albums a 
right join tracks t on a.id = t.album_id 
	where year between '2019-01-01' and '2020-12-31'

select a.name, avg(t.length)  from albums a 
right join tracks t on a.id = t.album_id 
	group by a.name

select distinct ar.name from albumsartists aa
right join artists ar on aa.artists_id = ar.id 
left join albums al on aa.albums_id = al.id  
	where al.year not between '2020-01-01' and '2020-12-31'
	
select distinct c.name from trackscollections tc
join collections c on tc.collections_id = c.id 
join tracks t on tc.tracks_id = t.id 
join albumsartists aa on aa.albums_id = t.album_id
join artists ar on ar.id = aa.artists_id  
	where ar.name = 'Metallica'
	
select  al.name  from albumsartists aa
join genresartists ga on aa.artists_id = ga.artists_id
join albums al on al.id = aa.albums_id  
	group by al.name
	having count(ga.genres_id)>1

select distinct t.name from tracks t 
left join trackscollections tc on t.id = tc.tracks_id
	where collections_id>0
	
select a.name from tracks t
join albumsartists aa on t.album_id  = aa.albums_id 
join artists a on a.id = aa.artists_id 
	where length = (select min(length) from tracks)

select a.name, count (album_id) as count_items from tracks t 
join albums a on a.id = t.album_id 
group by album_id, a.name 
order by count_items	
limit 1