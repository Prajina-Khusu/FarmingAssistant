-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2023 at 03:51 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user-system`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminpost`
--

CREATE TABLE `adminpost` (
  `adash-id` int(11) NOT NULL,
  `adminpost` varchar(255) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminpost`
--

INSERT INTO `adminpost` (`adash-id`, `adminpost`, `userid`) VALUES
(3, 'It is notify to all the farmer that the fertilizer will be distributed by coming saturday. Please bring your citizensip card to collect them.', 1),
(4, 'To celebrate envrionment day, it is notify to all the user to participate in the program and build a strong formation  bewteen each other ', 1);

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `fcomplaintid` int(11) NOT NULL,
  `fcomplain` varchar(225) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`fcomplaintid`, `fcomplain`, `userid`) VALUES
(8, 'Hello Sir, when will the fertilizer will be distributed. ', 6);

-- --------------------------------------------------------

--
-- Table structure for table `farmer`
--

CREATE TABLE `farmer` (
  `userid` int(11) NOT NULL,
  `name` varchar(49) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `farmer`
--

INSERT INTO `farmer` (`userid`, `name`, `email`, `password`) VALUES
(6, 'Prajina ', 'prajinakhusu@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `farmerproduct`
--

CREATE TABLE `farmerproduct` (
  `CropName` varchar(50) NOT NULL,
  `quantity` int(4) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `remarks` varchar(254) NOT NULL,
  `farmerpostid` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `farmerproduct`
--

INSERT INTO `farmerproduct` (`CropName`, `quantity`, `contact`, `remarks`, `farmerpostid`, `userid`) VALUES
('Wheat', 1000, '9869619868', 'Prajina Khusu, Itachhen-15 ', 26, 6),
('Cabbge ', 10, '9851611111', ' Itachhen', 27, 6);

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

CREATE TABLE `seller` (
  `userid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seller`
--

INSERT INTO `seller` (`userid`, `name`, `email`, `password`) VALUES
(5, 'Sachin', 'sachin@gmail.com', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `sellercomplaint`
--

CREATE TABLE `sellercomplaint` (
  `scomplaintid` int(11) NOT NULL,
  `scomplain` varchar(255) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sellerpost`
--

CREATE TABLE `sellerpost` (
  `CropName` varchar(50) NOT NULL,
  `quantity` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `remarks` varchar(50) NOT NULL,
  `sellerpostid` int(11) NOT NULL,
  `userid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userid`, `name`, `email`, `password`) VALUES
(1, 'Bhaktapur', 'Bhaktapur@gmail.com', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminpost`
--
ALTER TABLE `adminpost`
  ADD PRIMARY KEY (`adash-id`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`fcomplaintid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `farmer`
--
ALTER TABLE `farmer`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `farmerproduct`
--
ALTER TABLE `farmerproduct`
  ADD PRIMARY KEY (`farmerpostid`),
  ADD KEY `FK_userid` (`userid`);

--
-- Indexes for table `seller`
--
ALTER TABLE `seller`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `sellercomplaint`
--
ALTER TABLE `sellercomplaint`
  ADD PRIMARY KEY (`scomplaintid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `sellerpost`
--
ALTER TABLE `sellerpost`
  ADD PRIMARY KEY (`sellerpostid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminpost`
--
ALTER TABLE `adminpost`
  MODIFY `adash-id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `fcomplaintid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `farmer`
--
ALTER TABLE `farmer`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `farmerproduct`
--
ALTER TABLE `farmerproduct`
  MODIFY `farmerpostid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `seller`
--
ALTER TABLE `seller`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sellercomplaint`
--
ALTER TABLE `sellercomplaint`
  MODIFY `scomplaintid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `sellerpost`
--
ALTER TABLE `sellerpost`
  MODIFY `sellerpostid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adminpost`
--
ALTER TABLE `adminpost`
  ADD CONSTRAINT `adminpost_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`);

--
-- Constraints for table `complaint`
--
ALTER TABLE `complaint`
  ADD CONSTRAINT `complaint_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `farmer` (`userid`);

--
-- Constraints for table `farmerproduct`
--
ALTER TABLE `farmerproduct`
  ADD CONSTRAINT `FK_userid` FOREIGN KEY (`userid`) REFERENCES `farmer` (`userid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sellercomplaint`
--
ALTER TABLE `sellercomplaint`
  ADD CONSTRAINT `sellercomplaint_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `seller` (`userid`);

--
-- Constraints for table `sellerpost`
--
ALTER TABLE `sellerpost`
  ADD CONSTRAINT `sellerpost_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `seller` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
