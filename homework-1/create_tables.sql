-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id serial PRIMARY KEY,
    first_name  varchar(50),
    last_name   varchar(50),
    title       varchar(255),
    birth_date  varchar(50),
    notes       text
);

CREATE TABLE customers
(
    customer_id  varchar(50) PRIMARY KEY,
    company_name varchar(255),
    contact_name varchar(255)
);

CREATE TABLE orders
(
    order_id    serial PRIMARY KEY,
    customer_id varchar(50) REFERENCES customers (customer_id),
    employee_id int  NOT NULL REFERENCES employees (employee_id),
    order_date  date NOT NULL,
    ship_city   varchar(255)
);