
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
    lastUpdated timestamp not null default NOW()
);

create table Cart (
  billId    int REFERENCES Bill (billId) ON UPDATE CASCADE ON DELETE CASCADE, 
  productId int REFERENCES product (productId) ON UPDATE CASCADE, 
  amount     numeric NOT NULL DEFAULT 0, 
  CONSTRAINT bill_product_pkey PRIMARY KEY (billId, productId) 
);