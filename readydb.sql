-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 08, 2020 at 05:05 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `readydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `assignments`
--

CREATE TABLE `assignments` (
  `sub` varchar(20) NOT NULL,
  `ass_no` int(11) NOT NULL,
  `deadline` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assignments`
--

INSERT INTO `assignments` (`sub`, `ass_no`, `deadline`) VALUES
('Chemistry', 1, '2020-08-15'),
('physics', 2, '2020-08-17'),
('mathematics', 5, '2020-06-18'),
('biology', 6, '2020-07-25');

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

CREATE TABLE `grades` (
  `Student` varchar(20) NOT NULL,
  `Roll_No` int(11) NOT NULL,
  `Score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `grades`
--

INSERT INTO `grades` (`Student`, `Roll_No`, `Score`) VALUES
('Tina', 25, 25),
('reena', 56, 56),
('piku', 45, 38),
('zuzu', 69, 78),
('alvin', 5, 98);

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `sub` varchar(20) NOT NULL,
  `notes_no` int(11) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notes`
--

INSERT INTO `notes` (`sub`, `notes_no`, `description`) VALUES
('Chemistry', 1, 'Engineering Chemistry program integrates advanced knowledge of organic chemistry, analytical chemistry, and electro-chemistry into the design curriculum. By studying this subject, students can gain experience in the design of large-scale chemical manufacturing plants.'),
('physics', 2, '|\r\n|\r\nEngineering physics, or engineering science, refers to the study of the combined disciplines of physics, mathematics, biology, social science, and engineering, particularly computer, nuclear, electrical, electronic, aerospace, materials or mechanical engineering.'),
('mathematics ', 3, '|\r\n|\r\nEngineering mathematics is a branch of applied mathematics concerning mathematical methods and techniques that are typically used in engineering and industry. Along with fields like engineering physics and engineering geology, both of which may belong in the wider category engineering science, engineering mathematics is an interdisciplinary subject motivated by engineers\' needs both for practical, theoretical and other considerations outwith their specialization, and to deal with constraints to be effective in their work.'),
('biology', 4, '|\r\n|\r\nBiology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sname` varchar(20) NOT NULL,
  `roll` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sname`, `roll`) VALUES
('alvin', 5),
('TINA', 25),
('Tinku', 38),
('piku', 45),
('Reena ', 56),
('zuzu', 69);

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `tid` int(11) NOT NULL,
  `tname` varchar(20) NOT NULL,
  `tpass` varchar(20) NOT NULL,
  `sub` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`tid`, `tname`, `tpass`, `sub`) VALUES
(1, 'Anto', 'anto', 'Chemistry'),
(3, 'Sony', 'sony', 'mathematics '),
(4, 'Das', 'das', 'biology'),
(6, 'Rosy', 'rosy', 'Physics');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`ass_no`);

--
-- Indexes for table `grades`
--
ALTER TABLE `grades`
  ADD KEY `Roll_No` (`Roll_No`),
  ADD KEY `Roll_No_2` (`Roll_No`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`notes_no`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`roll`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`tid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assignments`
--
ALTER TABLE `assignments`
  MODIFY `ass_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `notes_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `grades`
--
ALTER TABLE `grades`
  ADD CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`Roll_No`) REFERENCES `student` (`roll`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
