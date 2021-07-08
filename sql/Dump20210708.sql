CREATE DATABASE  IF NOT EXISTS `comsedi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `comsedi`;
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
-- Table structure for table `form_gruas`
--

DROP TABLE IF EXISTS `form_gruas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `form_gruas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `modelo` int NOT NULL,
  `cantidad` int NOT NULL,
  `ubicacion` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  `tiempo` int NOT NULL,
  `estado` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `form_gruas`
--

LOCK TABLES `form_gruas` WRITE;
/*!40000 ALTER TABLE `form_gruas` DISABLE KEYS */;
/*!40000 ALTER TABLE `form_gruas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `form_servicios`
--

DROP TABLE IF EXISTS `form_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `form_servicios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_envio` date NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `ubicacion` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `form_servicios`
--

LOCK TABLES `form_servicios` WRITE;
/*!40000 ALTER TABLE `form_servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `form_servicios` ENABLE KEYS */;
UNLOCK TABLES;

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
  `role` varchar(45) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `salt` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'pamela','pamela@comsedi.com','Administrador','$2b$08$FPWiroxhkj8vq41OOYPgFu0Tdm08CSRbOlMd.FyXeXOKeogPjOFk.','$2b$08$FPWiroxhkj8vq41OOYPgFu'),(2,'javier','javier@comsedi.com','Administrador','$2b$08$N.zEyxTj3bV3IDlzIpmWP.9d/yGVuNCH5ISEBUGRPji3B7Ut2Trv6','$2b$08$N.zEyxTj3bV3IDlzIpmWP.'),(3,'francisco','francisco@comsedi.com','Administrador','$2b$08$0WxVkvdk0vBsD9vpEOxjCOQgT7OrY4a1TGQPJf9MBH4P9RcCoCvIy','$2b$08$0WxVkvdk0vBsD9vpEOxjCO'),(4,'hector','hector@comsedi.com','Cliente','$2b$08$4awiu8kDv9x45agw8vWtUeXPQnqRtAX3IaivEqeHAWigrwGPG4lyy','$2b$08$4awiu8kDv9x45agw8vWtUe'),(5,'jose','jose@comsedi.com','Cliente','$2b$08$s0.wPCVTsMsAN3f.mR0wju/C7tHZVjcOxyD2UcRYYOZF6YhfLpewq','$2b$08$s0.wPCVTsMsAN3f.mR0wju'),(6,'valeria','valeria@comsedi.com','Cliente','$2b$08$d6yE1sX6auMYY9nsiel0yeG8yT8GiX8rJKnGB1XCQ4o742ELsJ6sm','$2b$08$d6yE1sX6auMYY9nsiel0ye');
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

-- Dump completed on 2021-07-08  2:20:29
