select cast(getdate() as date) data, 'incidente_aberto_corretivo_30' tp, count(*) valor 
from vivaz.dbo.SM_I14_INCIDENTES t1 
left join vivaz.dbo.SM_I01_CATEGORIAS t2   
on t1.I01_CD_CATEGORIA = t2.I01_CD_CATEGORIA      
left join vivaz.dbo.SM_I17_STATUS t3      
on t1.I17_CD_STATUS = t3.I17_CD_STATUS
inner join vivaz.dbo.SM_G28_SERVICOS t4 
on t4.G28_CD_SERVICO = t1.G28_CD_SERVICO 
and t4.G28_TX_CAMINHO_COMPLETO like '%534%' 
where t1.I01_CD_CATEGORIA in (336,337)
and t1.I17_CD_STATUS not in (2,3,14,18)
and cast((t1.I14_DT_INCIDENTE+30) as date) < cast(getdate() as date)
;