-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 10 mars 2017 kl 09:35
-- Serverversion: 5.7.14
-- PHP-version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `wp`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `wp_users2add`
--

CREATE TABLE `wp_users2add` (
  `ID` bigint(20) UNSIGNED NOT NULL,
  `user_login` varchar(60) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_pass` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_nicename` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_email` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_url` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_registered` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_activation_key` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '',
  `user_status` int(11) NOT NULL DEFAULT '0',
  `display_name` varchar(250) COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumpning av Data i tabell `wp_users2add`
--

INSERT INTO `wp_users2add` (`ID`, `user_login`, `user_pass`, `user_nicename`, `user_email`, `user_url`, `user_registered`, `user_activation_key`, `user_status`, `display_name`) VALUES
(10, 'Anna', '$P$B42HLrxkqBvk9V3esVXv7yj/I3P2E11', 'anna', 'anna@gmail.com', 'http://Zeke_bar_landet', '2017-02-21 13:13:13', '', 0, 'anna enamn'),
(20, 'Bea', '$P$B42HLrxkqBvk9V3esVXv7yj/I3P2E11', 'bea', 'bea@gmail.com', 'http://Zeke_bar_landet', '2017-02-21 13:13:13', '', 0, 'bea enamn'),
(50, 'Eva', '$P$B42HLrxkqBvk9V3esVXv7yj/I3P2E11', 'eva', 'eva@gmail.com', 'http://Zeke_bar_landet', '2017-02-21 11:57:26', '', 0, 'eva enman'),
(40, 'Dilba', '$P$B42HLrxkqBvk9V3esVXv7yj/I3P2E11', 'dilba', 'dilba@gmail.com', 'http://Zeke_bar_landet', '2017-02-21 13:13:13', '', 0, 'dilba enamn'),
(30, 'Carina', '$P$B42HLrxkqBvk9V3esVXv7yj/I3P2E11', 'carina', 'carina@gmail.com', 'http://Zeke_bar_landet', '2017-02-21 11:57:26', '', 0, 'carina enamn');

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `wp_users2add`
--
ALTER TABLE `wp_users2add`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `user_login_key` (`user_login`),
  ADD KEY `user_nicename` (`user_nicename`),
  ADD KEY `user_email` (`user_email`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `wp_users2add`
--
ALTER TABLE `wp_users2add`
  MODIFY `ID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
