CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    class VARCHAR(50) NOT NULL,
    qr_code TEXT NOT NULL
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
