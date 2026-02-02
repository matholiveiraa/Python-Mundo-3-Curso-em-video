def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)

    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOÁVEL'
        else:
            dados['situacao'] = 'RUIM'

    return dados

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)