-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 28, 2023 at 04:26 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_bidding_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `bidding_details`
--

CREATE TABLE `bidding_details` (
  `id` int(50) NOT NULL,
  `productname` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `cus_name` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `cus_price` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bidding_details`
--

INSERT INTO `bidding_details` (`id`, `productname`, `brand`, `amount`, `cus_name`, `contact`, `cus_price`, `status`) VALUES
(1, 'tyre', 'mrf', '500', 'guru', '7895241454', '6000', 'Final Accept');

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` varchar(50) NOT NULL,
  `retailer_name` varchar(50) NOT NULL,
  `chat` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `user` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`id`, `retailer_name`, `chat`, `username`, `user`) VALUES
('2', 'vimal', 'hi', 'guru', ''),
('2', 'vimal', 'solunga', 'guru', ''),
('3', 'vimal', 'how are you', 'guru', '');

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`id`, `name`, `contact`, `email`, `address`, `gender`, `username`, `password`) VALUES
(1, 'guru', '7895241454', 'guru@gmail.com', 'thillai nagar', 'male', 'guru', '123'),
(2, 'nandha', '9876543121', 'nandha@gmail.com', 'thillai nagar', 'male', 'nandha', '123');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(50) NOT NULL,
  `holder_name` varchar(50) NOT NULL,
  `accno` varchar(50) NOT NULL,
  `cvv` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `account_no` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `holder_name`, `accno`, `cvv`, `username`, `product_name`, `account_no`, `amount`) VALUES
(1, 'vimal', '7894565454455', '789', 'guru', 'tyre', 'mrf', '500'),
(2, 'vimal', '45665651', '789', 'guru', 'tyre', 'mrf', '500');

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `id` int(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `start_price` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`id`, `product_name`, `brand`, `start_price`, `image`, `category`, `status`) VALUES
(1, 'car', 'toyata', '500000', 'tyre.png', 'Old', ''),
(2, 'tyre', 'mrf', '6000', 'tyre.png', 'new', '1');

-- --------------------------------------------------------

--
-- Table structure for table `retailer_details`
--

CREATE TABLE `retailer_details` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `retailer_details`
--

INSERT INTO `retailer_details` (`id`, `name`, `contact`, `address`, `email`, `gender`, `username`, `password`) VALUES
(1, 'vimal', '7895123456', 'thillai nagar', 'guru@gmail.com', 'male', 'guru', '123');
