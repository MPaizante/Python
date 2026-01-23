/*create table tipocliente(
	i_tipocliente_tipocliente int primary key auto_increment,
    s_dsctipocliente_tipocliente varchar(100) not null
);
*/
alter table cliente add constraint fk_tipocliente foreign key (i_tipo_cliente) references tipocliente (i_tipocliente_tipocliente);