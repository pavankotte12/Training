create table reviews(
	review_id serial primary key,
	rating integer not null check (rating > 1 and rating < 5),
	comment text
);

select * from reviews