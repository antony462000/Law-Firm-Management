-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2023 at 06:15 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lawfirm`
--

-- --------------------------------------------------------

--
-- Table structure for table `casedetails`
--

CREATE TABLE `casedetails` (
  `case_id` int(11) NOT NULL,
  `case_title` varchar(100) DEFAULT NULL,
  `case_desc` varchar(200) DEFAULT NULL,
  `case_file` varchar(300) DEFAULT NULL,
  `adv_name` varchar(100) DEFAULT NULL,
  `usename` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `casedetails`
--

INSERT INTO `casedetails` (`case_id`, `case_title`, `case_desc`, `case_file`, `adv_name`, `usename`) VALUES
(9, 'Boundary Dispute', 'I have a dispute with my neighbour regarding boundary', '', 'Asony', 'anton'),
(10, 'criminal case', 'Attempt to murder', '', 'Asony', 'anton'),
(11, 'Fraud', 'Fraud in Bussiness', '', 'Asony', 'anton'),
(12, 'criminal case', 'hostage', '', 'Asony', 'anton');

-- --------------------------------------------------------

--
-- Table structure for table `ipc`
--

CREATE TABLE `ipc` (
  `ipc_id` int(100) NOT NULL,
  `ipc_section` varchar(100) DEFAULT NULL,
  `ipc_description` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ipc`
--

INSERT INTO `ipc` (`ipc_id`, `ipc_section`, `ipc_description`) VALUES
(3, 'Sections 498A', 'Of Cruelty by Husband or Relatives of Husband'),
(4, 'Section 511', 'Of Attempts to Commit Offences');

-- --------------------------------------------------------

--
-- Table structure for table `tbladv`
--

CREATE TABLE `tbladv` (
  `adv_id` int(11) NOT NULL,
  `adv_name` varchar(100) NOT NULL,
  `adv_spec` varchar(100) NOT NULL,
  `adv_qual` varchar(100) NOT NULL,
  `adv_email` varchar(100) NOT NULL,
  `adv_exp` varchar(100) NOT NULL,
  `adv_roll` varchar(100) NOT NULL,
  `adv_mob` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbladv`
--

INSERT INTO `tbladv` (`adv_id`, `adv_name`, `adv_spec`, `adv_qual`, `adv_email`, `adv_exp`, `adv_roll`, `adv_mob`) VALUES
(5, 'asony', 'Civil', 'LLB', 'asony@gmail.com', '5', '112233', 2147483647);

-- --------------------------------------------------------

--
-- Table structure for table `tblcl`
--

CREATE TABLE `tblcl` (
  `cl_id` int(11) NOT NULL,
  `cl_name` varchar(100) NOT NULL,
  `cl_mail` varchar(100) NOT NULL,
  `cl_mob` varchar(100) NOT NULL,
  `cl_adhaar` varchar(100) NOT NULL,
  `cl_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblcl`
--

INSERT INTO `tblcl` (`cl_id`, `cl_name`, `cl_mail`, `cl_mob`, `cl_adhaar`, `cl_address`) VALUES
(3, 'abc', 'abc@', '456', '4565', 'SJCET\r\nPALAI'),
(1, 'Bismil Fahid', 'adv@gmail.com', '1236547852', '12587496305', 'SJCET\r\nPalai'),
(2, 'siddhart', 'sidharth@gmail.com', '1236547852', '12587496305', 'hfhbiw\r\n'),
(4, 'Sony', 'sony@gmail.com', '1234567890', '11223366', 'SJCET\r\nPalai');

-- --------------------------------------------------------

--
-- Table structure for table `tblfeedback`
--

CREATE TABLE `tblfeedback` (
  `feed_id` int(11) NOT NULL,
  `feed_title` varchar(100) DEFAULT NULL,
  `feed_desc` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tblfeedback`
--

INSERT INTO `tblfeedback` (`feed_id`, `feed_title`, `feed_desc`) VALUES
(6, 'Bad', 'Very bad experiences from attorney'),
(7, 'Good', 'Good approach from advocates');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE `tbllogin` (
  `login_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`login_id`, `username`, `password`, `type`) VALUES
(1, 'admin@gmail.com', 'admin123', 'admin'),
(2, 'adv@gmail.com', 'qwert', 'client'),
(3, 'sidharth@gmail.com', '789', 'client'),
(7, 'abc@', '456', 'client'),
(8, 'sony@gmail.com', 'sony', 'client'),
(9, 'asony@gmail.com', 'asony', 'advocate');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `casedetails`
--
ALTER TABLE `casedetails`
  ADD PRIMARY KEY (`case_id`);

--
-- Indexes for table `ipc`
--
ALTER TABLE `ipc`
  ADD PRIMARY KEY (`ipc_id`);

--
-- Indexes for table `tbladv`
--
ALTER TABLE `tbladv`
  ADD PRIMARY KEY (`adv_email`),
  ADD UNIQUE KEY `adv_id` (`adv_id`);

--
-- Indexes for table `tblcl`
--
ALTER TABLE `tblcl`
  ADD PRIMARY KEY (`cl_mail`),
  ADD UNIQUE KEY `cl_id` (`cl_id`);

--
-- Indexes for table `tblfeedback`
--
ALTER TABLE `tblfeedback`
  ADD PRIMARY KEY (`feed_id`);

--
-- Indexes for table `tbllogin`
--
ALTER TABLE `tbllogin`
  ADD PRIMARY KEY (`login_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `casedetails`
--
ALTER TABLE `casedetails`
  MODIFY `case_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `ipc`
--
ALTER TABLE `ipc`
  MODIFY `ipc_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbladv`
--
ALTER TABLE `tbladv`
  MODIFY `adv_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tblcl`
--
ALTER TABLE `tblcl`
  MODIFY `cl_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tblfeedback`
--
ALTER TABLE `tblfeedback`
  MODIFY `feed_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `tbllogin`
--
ALTER TABLE `tbllogin`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
