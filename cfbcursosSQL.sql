/*
sum - soma
avg - media
count - contagem
round - arredondar
*/


select *, round((f_precoun_produtovenda * ifnull(i_qtde_produtovenda,0)),2) as 'Total' from produtovenda;