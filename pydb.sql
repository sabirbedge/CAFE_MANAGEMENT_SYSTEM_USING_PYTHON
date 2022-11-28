-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 28, 2022 at 09:41 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblcustomer`
--

DROP TABLE IF EXISTS `tblcustomer`;
CREATE TABLE IF NOT EXISTS `tblcustomer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nm` varchar(20) DEFAULT NULL,
  `addr` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcustomer`
--

INSERT INTO `tblcustomer` (`id`, `nm`, `addr`) VALUES
(1, 'Sabir Bedge', 'Miraj');

-- --------------------------------------------------------

--
-- Table structure for table `tblprod`
--

DROP TABLE IF EXISTS `tblprod`;
CREATE TABLE IF NOT EXISTS `tblprod` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pnm` varchar(30) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblprod`
--

INSERT INTO `tblprod` (`pid`, `pnm`, `qty`, `price`, `id`) VALUES
(1, 'Tandoori Paneer', 2, 180, 1),
(2, 'Chicken Burger', 2, 180, 1),
(3, 'Cold Coffee', 1, 100, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
