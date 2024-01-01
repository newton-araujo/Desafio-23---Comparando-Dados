<h1>Verificação de Clientes com Pendências
</h1>
<p>
    Este código tem como objetivo criar listas de clientes e pendências, utilizar conjuntos (set) para encontrar os nomes que estão presentes em ambas as listas e, em seguida, imprimir os clientes que têm pendências.
</p>

<ol>
<h2><li>Criação das Listas:</li></h2>
<ul>
    <li>Inicia as variáveis clientes e pendencia com listas contendo nomes de clientes e uma lista de pendências, respectivamente.</li>
</ul>

    clientes = ['Pedro', 'Ana', 'Carlos', 'Maria', 'Antonio']
    pendencia = ['Pedro', 'Flavio', 'Maria', 'Claudio', 'Laura']


<h2><li>Conjunto de Verificação:</li></h2>
<ul>
    <li>Utiliza a função set para criar conjuntos a partir das listas clientes e pendencia.</li>
    <li>Em seguida, utiliza a função intersection para encontrar os nomes que estão presentes em ambas as listas.</li>
</ul>

    verificar = set(clientes).intersection(set(pendencia))


<h2><li>Saída de Dados:</li></h2>
<ul><li>Utiliza um loop for para iterar sobre a lista resultante do conjunto de verificação e imprimir os nomes dos clientes que têm pendências.</li></ul>

    for nome in list(verificar):
    print(nome)
</ol>

<h3>Interatividade:</h3>
<p>O código proporciona uma solução interativa ao identificar os clientes que possuem pendências com base nas duas listas.</p>


<h3>Conclusão:</h3>
<p>Ao executar este código, serão impressos os nomes dos clientes que estão presentes tanto na lista de clientes como na lista de pendências. Isso destaca o uso de conjuntos para encontrar a interseção entre duas listas em Python.</p>
