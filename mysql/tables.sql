CREATE TABLE IF NOT EXISTS incidentes_historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    incidente_aberto_corretivo INT,
    incidente_aberto_corretivo_30 INT,	
    incidente_sem_classificacao INT,
    incidente_sem_alocacao INT);

insert into incidentes_historico(incidente_aberto_corretivo,incidente_sem_alocacao) values(1,1);
insert into incidentes_historico(incidente_aberto_corretivo,incidente_sem_alocacao) values(2,2);
insert into incidentes_historico(incidente_aberto_corretivo,incidente_sem_alocacao) values(3,3);