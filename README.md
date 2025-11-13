## Descrição do problema

O programa Identifier tem como objetivo verificar se um identificador é válido de acordo com as seguintes regras:

- Deve começar com uma letra (a–z ou A–Z);
- Pode conter apenas letras e dígitos;
- Deve ter entre 1 e 6 caracteres (inclusive).
- A função retorna True se o identificador for válido e False caso contrário.

## Classes de Equivalência
Critério	Classe Válida	Classe Inválida
Comprimento	1 a 6 caracteres	0 caracteres ou > 6 caracteres
Caractere inicial	Letra (a-z, A-Z)	Dígito, símbolo ou vazio
Caracteres permitidos	Letras e dígitos	Símbolos ou caracteres especiais

## Análise de Valor Limite
Critério	Limite Inferior	Limite Superior	Testes Próximos ao Limite
Comprimento	0 (inválido) → 1 (válido)	6 (válido) → 7 (inválido)	"", "o", "a23456", "a234567"

## Tabela de Casos de Teste
| ID   | Entrada  | Classe de Equivalência                                           | Resultado Esperado |
|------|-----------|------------------------------------------------------------------|--------------------|
| CT01 | 123abc    | Inicia com número                                               | Inválido           |
| CT02 | a1b2c3    | Válido (letra inicial, letras e dígitos, 6 caracteres)          | Válido             |
| CT03 | ammm6     | Válido (letra inicial, 5 caracteres)                            | Válido             |
| CT04 | a_-72     | Contém símbolo                                                  | Inválido           |
| CT05 | a234567   | 7 caracteres (muito longo)                                      | Inválido           |
| CT06 | o         | 1 caractere (limite inferior)                                   | Válido             |
| CT07 | ro        | 2 caracteres válidos                                            | Válido             |
| CT08 | abc*e     | Contém caractere especial                                       | Inválido           |
| CT09 | mar       | 3 caracteres válidos                                            | Válido             |



## Execução dos testes localmente

Instale o pytest (caso não tenha):

```
pip install pytest
```

Rode os testes:

```
pytest -v
```

Os resultados esperados devem indicar que todos os testes passaram com sucesso ✅
