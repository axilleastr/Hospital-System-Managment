-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Φιλοξενητής: 127.0.0.1
-- Χρόνος δημιουργίας: 05 Ιουν 2017 στις 16:31:14
-- Έκδοση διακομιστή: 5.7.14
-- Έκδοση PHP: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `hosp`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `anhkei`
--

CREATE TABLE `anhkei` (
  `id_giatrou` varchar(6) DEFAULT NULL,
  `eidikothta_klinikis` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `apothiki`
--

CREATE TABLE `apothiki` (
  `id_apothikis` int(3) NOT NULL,
  `eidikothta_klinikis` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `asthenis`
--

CREATE TABLE `asthenis` (
  `id_astheni` varchar(6) NOT NULL,
  `firstname` varchar(20) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `hlikia` int(3) DEFAULT NULL,
  `dieuthinsi` varchar(50) DEFAULT NULL,
  `fulo` varchar(1) DEFAULT NULL,
  `phone_num` bigint(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `asthenoforo`
--

CREATE TABLE `asthenoforo` (
  `diathesimo` tinyint(1) DEFAULT NULL,
  `arithmos_pinakidas` varchar(8) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `epiblepei`
--

CREATE TABLE `epiblepei` (
  `id_ergazomenou` varchar(6) DEFAULT NULL,
  `eidikothta_klinikis` varchar(20) DEFAULT NULL,
  `id_apothikis` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ergazomenos`
--

CREATE TABLE `ergazomenos` (
  `id_ergazomenou` varchar(6) NOT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `hlikia` int(3) DEFAULT NULL,
  `dieuthinsi` varchar(50) DEFAULT NULL,
  `fulo` varchar(1) DEFAULT NULL,
  `phone_num` bigint(10) DEFAULT NULL,
  `misthos` float DEFAULT NULL,
  `wrario` varchar(25) DEFAULT NULL,
  `uperories` int(2) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `farmako`
--

CREATE TABLE `farmako` (
  `id_farmakou` varchar(10) NOT NULL,
  `onoma_farmakou` varchar(25) DEFAULT NULL,
  `posothta_se_apothema` int(3) DEFAULT NULL,
  `id_apothikis` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `iatrika_ergaleia`
--

CREATE TABLE `iatrika_ergaleia` (
  `id_iatriko_ergaleio` varchar(10) NOT NULL,
  `iatriko_ergaleio` varchar(25) DEFAULT NULL,
  `apothema` int(3) DEFAULT NULL,
  `id_apothikis` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `iatros`
--

CREATE TABLE `iatros` (
  `eidikothta` varchar(20) DEFAULT NULL,
  `id_ergazomenou` varchar(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `istoriko_grammateias`
--

CREATE TABLE `istoriko_grammateias` (
  `id_astheni` varchar(6) DEFAULT NULL,
  `id_istorikou` varchar(10) NOT NULL,
  `shmeiwseis` text,
  `id_ergazomenou` varchar(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `kliniki`
--

CREATE TABLE `kliniki` (
  `eidikothta_klinikis` varchar(20) NOT NULL,
  `arithmos_dwmatiwn` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `logariasmos_plhrwmhs`
--

CREATE TABLE `logariasmos_plhrwmhs` (
  `timh` float DEFAULT NULL,
  `apodeiksi_plhrwmhs` varchar(20) NOT NULL,
  `id_astheni` varchar(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `noshleuetai`
--

CREATE TABLE `noshleuetai` (
  `id_astheni` varchar(6) NOT NULL,
  `id_thalamou` int(3) NOT NULL,
  `hmeromhnia_eisagwghs` date DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `nosokoma`
--

CREATE TABLE `nosokoma` (
  `id_ergazomenou` varchar(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `pairnei_eksithrio`
--

CREATE TABLE `pairnei_eksithrio` (
  `hmeromhnia_eksagwghs` date DEFAULT NULL,
  `id_astheni` varchar(6) NOT NULL,
  `id_thalamou` int(3) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `parakoloythei`
--

CREATE TABLE `parakoloythei` (
  `id_astheni` varchar(6) DEFAULT NULL,
  `id_ergazomenou` varchar(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `proswpiko_grammateias`
--

CREATE TABLE `proswpiko_grammateias` (
  `id_ergazomenou` varchar(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `prwtes_ules`
--

CREATE TABLE `prwtes_ules` (
  `id_prwth_ulh` varchar(10) NOT NULL,
  `prwth_ulh` varchar(25) DEFAULT NULL,
  `apothema` int(3) DEFAULT NULL,
  `id_apothikis` int(3) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `thalamos`
--

CREATE TABLE `thalamos` (
  `id_thalamou` int(3) NOT NULL,
  `eidikothta_klinikis` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `ypallhlos_asthenoforou`
--

CREATE TABLE `ypallhlos_asthenoforou` (
  `id_ergazomenou` varchar(6) NOT NULL,
  `arithmos_pinakidas` varchar(8) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `anhkei`
--
ALTER TABLE `anhkei`
  ADD KEY `ANHKEI_fk0` (`id_giatrou`),
  ADD KEY `ANHKEI_fk1` (`eidikothta_klinikis`);

--
-- Ευρετήρια για πίνακα `apothiki`
--
ALTER TABLE `apothiki`
  ADD PRIMARY KEY (`id_apothikis`),
  ADD KEY `APOTHIKI_fk0` (`eidikothta_klinikis`);

--
-- Ευρετήρια για πίνακα `asthenis`
--
ALTER TABLE `asthenis`
  ADD PRIMARY KEY (`id_astheni`);

--
-- Ευρετήρια για πίνακα `asthenoforo`
--
ALTER TABLE `asthenoforo`
  ADD PRIMARY KEY (`arithmos_pinakidas`);

--
-- Ευρετήρια για πίνακα `epiblepei`
--
ALTER TABLE `epiblepei`
  ADD KEY `EPIBLEPEI_fk0` (`id_ergazomenou`),
  ADD KEY `EPIBLEPEI_fk1` (`eidikothta_klinikis`),
  ADD KEY `EPIBLEPEI_fk2` (`id_apothikis`);

--
-- Ευρετήρια για πίνακα `ergazomenos`
--
ALTER TABLE `ergazomenos`
  ADD PRIMARY KEY (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `farmako`
--
ALTER TABLE `farmako`
  ADD PRIMARY KEY (`id_farmakou`),
  ADD KEY `FARMAKO_fk0` (`id_apothikis`);

--
-- Ευρετήρια για πίνακα `iatrika_ergaleia`
--
ALTER TABLE `iatrika_ergaleia`
  ADD PRIMARY KEY (`id_iatriko_ergaleio`),
  ADD KEY `IATRIKA_ERGALEIA_fk0` (`id_apothikis`);

--
-- Ευρετήρια για πίνακα `iatros`
--
ALTER TABLE `iatros`
  ADD PRIMARY KEY (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `istoriko_grammateias`
--
ALTER TABLE `istoriko_grammateias`
  ADD PRIMARY KEY (`id_istorikou`),
  ADD KEY `ISTORIKO_GRAMMATEIAS_fk0` (`id_astheni`),
  ADD KEY `ISTORIKO_GRAMMATEIAS_fk1` (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `kliniki`
--
ALTER TABLE `kliniki`
  ADD PRIMARY KEY (`eidikothta_klinikis`);

--
-- Ευρετήρια για πίνακα `logariasmos_plhrwmhs`
--
ALTER TABLE `logariasmos_plhrwmhs`
  ADD PRIMARY KEY (`apodeiksi_plhrwmhs`),
  ADD KEY `LOGARIASMOS PLHRWMHS_fk0` (`id_astheni`);

--
-- Ευρετήρια για πίνακα `noshleuetai`
--
ALTER TABLE `noshleuetai`
  ADD PRIMARY KEY (`id_astheni`,`id_thalamou`),
  ADD KEY `NOSHLEUETAI_fk1` (`id_thalamou`);

--
-- Ευρετήρια για πίνακα `nosokoma`
--
ALTER TABLE `nosokoma`
  ADD PRIMARY KEY (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `pairnei_eksithrio`
--
ALTER TABLE `pairnei_eksithrio`
  ADD PRIMARY KEY (`id_astheni`,`id_thalamou`),
  ADD KEY `PAIRNEI EKSITHRIO_fk1` (`id_thalamou`);

--
-- Ευρετήρια για πίνακα `parakoloythei`
--
ALTER TABLE `parakoloythei`
  ADD KEY `PARAKOLOYTHEI_fk0` (`id_astheni`),
  ADD KEY `PARAKOLOYTHEI_fk1` (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `proswpiko_grammateias`
--
ALTER TABLE `proswpiko_grammateias`
  ADD PRIMARY KEY (`id_ergazomenou`);

--
-- Ευρετήρια για πίνακα `prwtes_ules`
--
ALTER TABLE `prwtes_ules`
  ADD PRIMARY KEY (`id_prwth_ulh`),
  ADD KEY `PRWTES_ULES_fk0` (`id_apothikis`);

--
-- Ευρετήρια για πίνακα `thalamos`
--
ALTER TABLE `thalamos`
  ADD PRIMARY KEY (`id_thalamou`),
  ADD KEY `THALAMOS_fk0` (`eidikothta_klinikis`);

--
-- Ευρετήρια για πίνακα `ypallhlos_asthenoforou`
--
ALTER TABLE `ypallhlos_asthenoforou`
  ADD PRIMARY KEY (`id_ergazomenou`),
  ADD KEY `YPALLHLOS_ASTHENOFOROU_fk1` (`arithmos_pinakidas`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
