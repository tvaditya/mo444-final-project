__author__="jose"

def get_law_words():
    return ["alinea", "anexo", "apendice", "art", "artigo", "caderno", "capitulo", "caput", "clausula", "ementa", "inciso", "item", "livro", "nota", "paragrafo", "parte", "preliminar", "secao", "subanexo", "subitem", "subsecao", "subtitulo", "tabela"]

def get_termos_interesse():
    termos = "Normativo Normativos Lucro Servico Credito Agricolas Presumido Desembaraco Extrativismo Base Normativo valor Declaracao Fiscal grafico Fiscal Mercadoria Resolucao Social SEST IPI IRPJ Nacional Antecipacao Pecuaria Retencao Mercadorias incidencia SEFIP Diferimento CSLL publica Pessoa DIFA ICMS ST Concomitante suspensao GABINETE Laticinios divergencia Tab sobre Simples Bebidas Pauta ICMS Economica IRRF Lalur Pareceres COFINS o Contribuicao mva Cooperativa Ajustado imunidade Retido Prestacoes ISS Retida Minimos calamidade fiscal Operacoes Codigo Aliquota calculo sinal Interpretativo Gerador Importacao Madeiras Boletim ICMS ST Frente SENAT PIS Precos nao incidencia MINISTRO valorem Imposto cnae Atividade GFIP Renda Nacional Lancamento INSS Solucao consulta Recebimento CGSN Liquido Fato Pagamento documento Classe aliquota Ato RAIS modelo Declaratorio Progr Aduaneiro Juridica COFINS ST Executivo isencao Camex Lei Fcont"
    termos = [a.lower() for a in termos.split()]
    return list(set(termos))

def get_termos_interesse_raw():
    return ["aliquota", 
        "Aliquota ad valorem", 
        "Ato Declaratorio", 
        "Ato Declaratorio Executivo", 
        "Ato Declaratorio Interpretativo", 
        "Ato Declaratorio Normativo", 
        "Ato Normativo", 
        "bit", 
        "bk", 
        "Boletim de Precos de Mercadorias", 
        "calamidade publica", 
        "Camex", 
        "CGSN", 
        "Classe FiscalMercadoria", 
        "cnae", 
        "Codigo de Atividade Economica Nacional.", 
        "Codigo do modelo do documento fiscal.", 
        "Codigo Fiscal de Operacoes e Prestacoes de Servico", 
        "COFINS", 
        "COFINS Cooperativa", 
        "COFINS Importacao", 
        "COFINS-ST", 
        "Contribuicao Social sobre o Lucro Liquido", 
        "CSLL Retida", 
        "Declaracao", 
        "Dt. Desembaraco Aduaneiro", 
        "Dt. Fato Gerador", 
        "Dt. Lancamento", 
        "Dt. Pagamento", 
        "Dt. Recebimento", 
        "Fcont", 
        "GABINETE DO MINISTRO", 
        "GFIP", 
        "ICMS", 
        "ICMS Antecipacao", 
        "ICMS DIFA", 
        "ICMS-ST-Concomitante", 
        "ICMS-ST-Frente", 
        "Imposto de Importacao", 
        "Imposto de Renda Pessoa Juridica", 
        "Imposto sobre a Renda", 
        "INSS", 
        "INSS Retido", 
        "IPI", 
        "IRPJ", 
        "IRRF", 
        "IRRF Tab. Progr.", 
        "ISS", 
        "Lalur", 
        "mva", 
        "mva Ajustado", 
        "Pareceres Normativos", 
        "Pauta de Precos Minimos de Agricolas, Laticinios e Extrativismo", 
        "Pauta de Precos Minimos de Madeiras", 
        "Pauta de Precos Minimos de Mercadorias", 
        "Pauta de Precos Minimos de Pecuaria", 
        "Pauta de Precos Minimos Pauta de Precos Minimos", 
        "PIS", 
        "PIS Cooperativa", 
        "PIS Importacao", 
        "RAIS", 
        "Resolucao", 
        "Retencao", 
        "SEFIP", 
        "SENAT", 
        "SEST", 
        "Simples Nacional", 
        "sinal grafico", 
        "Solucao de consulta", 
        "Solucao de divergencia", 
        "Lei", 
        "Boletim de Precos de Bebidas", 
        "Aliquota", 
        "Base de calculo", 
        "Credito Presumido", 
        "Diferimento", 
        "imunidade", 
        "incidencia", 
        "isencao", 
        "nao-incidencia", 
        "Classe de valor", 
        "Pauta", 
        "suspensao"]
