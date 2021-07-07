-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: comsedi
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `salt` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (4,'fran','fran@comsedi.com','$2b$08$j6Cm.5h0QzSsDaYFZVogd.P9OOYAYFSeBr3KSmWUu2XePU3MXANrO','$2b$08$j6Cm.5h0QzSsDaYFZVogd.'),(5,'pamela','pamela@comsedi.com','$2b$08$B2D/RoGeV15Frvh4r11BuumI9iz4mh8Zo56Cka5bELWQeASTwuwiC','$2b$08$B2D/RoGeV15Frvh4r11Buu'),(6,'hector','hector@comsedi.com','$2b$08$8qzn.VzmzMuARSs64XScduXSsLGTm7r9MG9lolluSNGX6D5A1Tj0i','$2b$08$8qzn.VzmzMuARSs64XScdu'),(7,'chema','chema@comsedi.com','$2b$08$stl7nOIFGwdU1QWymt59B.PCdYADokF91CdGO758rryoiIxnlGRBm','$2b$08$stl7nOIFGwdU1QWymt59B.'),(8,'vale','vale@comsedi.com','$2b$08$8Gk2acw2Ul0FZKYoPeqFWeKdAdYLjx1TzLqAwxRbkr2FIDR3oMUwK','$2b$08$8Gk2acw2Ul0FZKYoPeqFWe'),(9,'javier','javier@comsedi.com','$2b$08$O3FYqCK5OJqcAQIcJPG.zehmFsdQZMw9r11c3J.vZjtlgyB5Rmu0G','$2b$08$O3FYqCK5OJqcAQIcJPG.ze');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-06 19:31:41
