DELIMITER $$
CREATE PROCEDURE canal(in curso varchar(50))
BEGIN
	declare x varchar(20);
    set x = 'Matheus Paizante';
    select x, curso;
END $$

DELIMITER ;
CALL canal('SQL');