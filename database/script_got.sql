-- Drop all tables if exists
drop table if exists Amante;
drop table if exists Grupo;
drop table if exists Dragon;
drop table if exists Hijo;
drop table if exists Subdito;
drop table if exists Territorio;
drop table if exists Guerrero;

-- Create tables
-- Table Grupo
create table if not exists Grupo
(
  Id serial primary key,
  Nombre_Grupo varchar(30) not null
);

-- Table Amante
create table if not exists Amante
(
  Id serial primary key,
  Id_Grupo integer references Grupo(Id) not null,
  Nombre_Amante varchar(30) not null,
  IsDigno boolean null,
  IsEjecutado boolean null
);

-- Table Dragon
create table if not exists Dragon
(
  Id serial primary key,
  IsDisponible boolean not null,
  Edad integer not null,
  Fuerza integer not null,
  Color varchar(20) not null,
  Nombre varchar(30) not null,
  Numero_Muertes integer not null,
  Comida_Favorita varchar(30) not null
);

-- Table Territorio
create table if not exists Territorio
(
  Id serial primary key,
  Nombre_Territorio varchar(30) not null,
  IsConquistado boolean not null,
  Caracteristicas text not null,
  Clima varchar(30) not null,
  Principales_Productos text not null
);

-- Table Subdito
create table if not exists Subdito
(
  Id serial primary key,
  Nombre_Subdito varchar(30) not null,
  Aflicion varchar(100) not null,
  Id_Territorio integer references Territorio(Id) not null
);

-- Table Hijo
create table if not exists Hijo
(
  Id serial primary key,
  Nombre_Hijo varchar(30) not null,
  Id_Subdito integer references Subdito(Id) not null
);

-- Table Guerrero
create table if not exists Guerrero
(
  Id serial primary key,
  Nombre_Guerrero varchar(30) not null,
  Especialidad varchar(50) not null,
  Cargo varchar(50) not null,
  Numero_Muertes integer not null,
  IsReinaInteresada boolean not null
);