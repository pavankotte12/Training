CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    city VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (customer_name, email, phone, city, address)
VALUES
('Ravi Kumar', 'ravi@example.com', '9876543210', 'Hyderabad', 'Ameerpet'),
('Anita Sharma', 'anita@example.com', '9876543211', 'Bangalore', 'MG Road'),
('John Mathew', 'john@example.com', '9876543212', 'Chennai', 'T Nagar');