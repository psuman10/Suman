-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 02, 2020 at 05:48 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airline ticket booking system`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `passport` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `pickup` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `boarding` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`passport`, `name`, `gender`, `date`, `pickup`, `email`, `boarding`) VALUES
(1, 'uu', 'Male', '45858', 'Delhi', 'fgtt', 'New York'),
(8, '8', 'Female', '8', 'kathmandu-Nepal', '8', 'kathmandu-Nepal'),
(78, '78', 'Other', '78', 'sydney', '78', 'kathmandu-Nepal'),
(89, 'uu', 'Male', '45858', 'brisbane', 'ss', 'New York'),
(9840, 'suman parajuli', 'Male', '6/20/2021', 'sydney', 'Sp554540@gmail.com', 'Kathmandu-Nepal'),
(49502, 'suman parajuli', 'Male', '12/20/2021', 'sydney', 'Sp554540@gmail.com', 'Kathmandu-Nepal'),
(108690, 'sp', 'Male', '8/20/2020', 'sydney', 'Sp554540@gmail.com', 'Kathmandu-Nepal'),
(190265, 'psp', 'Female', '12/20/2021', 'sydney', 'Sp554540@gmail.com', 'kathmandu-Nepal'),
(11454479, 'Suman Parajuli', 'Male', '12/12/2020', 'kathmandu-Nepal', 'sp554540@gmail.com', 'sydney');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `passport` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `username`, `password`, `name`, `address`, `phone`, `email`, `passport`) VALUES
(1, 'u', 'u', 'u', 'u', 'u', 'u', 'u'),
(2, '1', '1', '1', '1', '1', '1', '1'),
(3, '2', '2', '2', '2', '2', '2', '2'),
(4, '1', '1', '1', '1', '1', '1', '1'),
(5, '1', '1', '1', '1', '1', '1', '1'),
(6, '2', '2', '2', '22', '2', '2', '22'),
(7, '', '', '', '', '', '', ''),
(8, '', '', '', '', '', '', ''),
(9, '', '', '', '', '', '', ''),
(10, '', '', '', '', '', '', ''),
(11, '', '', '', '', '', '', ''),
(12, '', '', '', '', '', '', ''),
(13, '', '', '', '', '', '', ''),
(14, '', '', '', '', '', '', ''),
(15, '3', '3', '3', '3', '3', '3', '3'),
(16, '55', '55', '1', '1', '1', '1', '1'),
(17, '190265', 'sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com'),
(18, '190265', 'sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com'),
(19, '190265', 'sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com'),
(20, '190265', 'sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com'),
(21, 'Psuman', 'Change', 'Suman Parajuli', 'Tikathali', '11454479', 'Nepal', 'sp554540@gmail.com'),
(22, 'Psuman', 'change', 'Suman Parajuli', 'Tikathali', '11454479', 'Nepal', 'sp554540@gmail.com'),
(23, '190265', 'sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`passport`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `passport` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11454480;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
