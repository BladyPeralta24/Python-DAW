drop database if exists agencia_de_viajes;

create database agencia_de_viajes;
use agencia_de_viajes;

drop table if exists aeropuerto;
drop table if exists avion;
drop table if exists billete;
drop table if exists viaje;

create table viaje(
    id_viaje int PRIMARY KEY,
    origen varchar(50) not null,
    destino varchar(50) not null,
    avion varchar(50) not null
);

create table billete(
    id_billete int PRIMARY KEY,
    id_viaje int,
    nombre VARCHAR(50) not null,
    apellidos varchar(50) not null,
    
    constraint FK_id_viaje foreign key (id_viaje) references viaje(id_viaje)
);

create table avion(
    id_avion int PRIMARY KEY,
    modelo VARCHAR(50),
    capacidad int not null
);

create table aeropuerto(
    id_aeropuerto int PRIMARY KEY,
    sede varchar(50)
);
