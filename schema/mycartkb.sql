
create table CartUser (
	id  serial primary key,
	username text not null,
	lastUpdated timestamp not null default NOW(),
	email varchar(255),
	isAdmin boolean not null default false,
    unique (username,email)
);

create table Category (
	id  serial primary key,
	categoryName text not null,
	lastUpdated timestamp not null default NOW()
);


create table Product (
    productId serial primary key,
	categoryId bigint not null references Category(id),
	productName text not null,
	productDescription text not null default 'N/A',
    ProductPrice numeric not null

);

create table Bill (
    billId  serial PRIMARY KEY,
    userId bigint not null references CartUser(id),
    bill     text NOT NULL,
    amount     numeric NOT NULL DEFAULT 0, 
    lastUpdated timestamp not null default NOW()
);
