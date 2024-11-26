CREATE DATABASE IF NOT EXISTS ophthalmology_patients;
USE ophthalmology_patients;
CREATE TABLE IF NOT EXISTS patient
(
  patientid CHAR(8) NOT NULL,
  patient_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (patientid)
);

CREATE TABLE IF NOT EXISTS queue
(
  registrationid VARCHAR(255) NOT NULL,
  patientid CHAR(8) NOT NULL,
  queuedate DATE NOT NULL,
  queueat TIME NOT NULL,
  PRIMARY KEY (registrationid),
  FOREIGN KEY (patientid) REFERENCES patient(patientid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS queuedetail
(
  id int NOT NULL AUTO_INCREMENT,
  registrationid VARCHAR(255) NOT NULL,
  subspecialty VARCHAR(255) NOT NULL,
  waitingtime INT NOT NULL,
  examtime INT NOT NULL,
  caretime INT NOT NULL,
  insurance VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (registrationid) REFERENCES queue(registrationid) ON DELETE CASCADE
);

# Patient
INSERT INTO patient(patientid, patient_name) VALUES ('12632466', 'Ediyanto'),
('12641025','Fatkul Rozak'),
('12573804','Dharmawan Utomo'),
('12683246','Ibnu Krisdianto'),
('12697269','Arif Delianto');

# Queue
INSERT INTO queue (patientid, registrationid, queuedate, queueat) VALUES
('12632466','001', '2018-09-10', '04:37'),
('12641025','002', '2018-09-03', '01:51'),
('12573804','003', '2018-09-17', '05:35'),
('12683246','004', '2018-09-10', '07:08'),
('12697269','005', '2018-09-10', '07:19');

# Queue Detail
INSERT INTO queuedetail (registrationid, subspecialty, waitingtime, examtime, caretime, insurance) VALUES
('001', 'Rekonstruksi', 534, 111, 645, 'BPJS'),
('002', 'Rekonstruksi', 555, 86, 641, 'BPJS'),
('003', 'Retina', 294, 284, 579, 'Mandiri'),
('004', 'Neuro Ophthalmology', 159, 358, 517, 'BPJS'),
('005', 'Glaukoma', 508, 101, 609, 'BPJS')
;