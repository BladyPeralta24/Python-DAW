drop database if exists agencia_de_viajes;
create database agencia_de_viajes;
use agencia_de_viajes;



drop table if exists aeropuerto;
create table aeropuerto(
    id_aeropuerto int PRIMARY KEY,
    sede varchar(50) not null
);
INSERT INTO aeropuerto 
VALUES 
(16,'Barcelona'),
(17,'Las Palmas'),
(15,'Londres'),
(14,'Madrid');


drop table if exists avion;
create table avion(
    id_avion int PRIMARY KEY,
    modelo VARCHAR(50) not null,
    capacidad int not null
);
INSERT INTO avion 
VALUES 
(1,'Boeing737',600),
(2,'Airbus300',200);


drop table if exists viaje;
create table viaje(
    id_viaje int PRIMARY KEY,
    id_origen int not null,
    id_destino int not null,
    id_avion int not null,

    constraint FK_id_origen foreign key (id_origen) references aeropuerto(id_aeropuerto) on delete cascade,
    constraint FK_id_destino foreign key (id_destino) references aeropuerto(id_aeropuerto) on delete cascade,
    constraint FK_id_avion foreign key (id_avion) references avion(id_avion) on delete cascade
);
INSERT INTO viaje 
VALUES 
(1,14,16,1);


drop table if exists billete;
create table billete(
    id_billete int PRIMARY KEY,
    id_viaje int,
    nombre VARCHAR(50) not null,
    apellidos varchar(50) not null,
    
    constraint FK_id_viaje foreign key (id_viaje) references viaje(id_viaje) on delete cascade
);
INSERT INTO billete 
VALUES 
(1, 1,'Bladimir','Peralta Herrera');