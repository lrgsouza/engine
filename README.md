# Discord Tool Bot
> Teste a aplicação na íntegra: [Discord Server](https://discord.gg/GbsgJEeK2k)

## Como rodar a aplicação

Para rodar a aplicação localmente, utilizando seu próprio servidor no Discord:

1. Criação do Bot do Discord
    1. Crie um servidor do Discord.

    2. Crie uma nova aplicação do Discord, em [Discord Developer Portal](https://discord.com/developers/applications)

    3. Na seção `Bot`, copie o token do Bot em `Token > Reset Token`

    4. Em `Installation`, selecione o Authorization Method `Guild Install` e Install Link `Discord Provided Link`. Copie a url e acesse no seu navegador.

    5. Na página a seguir, permita que o Bot acesse seu servidor.

2. Rodando a aplicação localmente
    1. Rode o comando:
        ```sh
        export DISCORD_TOKEN="discord-token-aqui"
        ```

    2. Rode o arquivo [/app/main.py](./app/main.py)

    3. Utilize os comandos no canal designado, definido como "recursos" por padrão, mas que pode ser modificado em [/app/variables.py](./app/variables.py)

3. Rodando a aplicação usando Docker Compose

    1. Crie um arquivo .env, dessa forma:
        ```python
        DISCORD_TOKEN="discord-token-aqui"
        ```

    2. Certifique-se de ter instalado Docker e Docker Compose em seu computador. [Saiba mais](https://docs.docker.com/compose/install/).

    3. Rode o comando
        ```sh
        docker-compose up --build
        ```




# Unit Test - Overview
## Organização de Testes em Classes
É comum organizar os testes em classes, onde cada classe herda de `unittest.TestCase`. Isso facilita a organização e execução dos testes.
```py
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # verifica se s.split falha quando o separador não é uma string
        with self.assertRaises(TypeError):
            s.split(2)
```

## SetUp e TearDown
Estes são métodos especiais que são executados antes e depois de cada método de teste. Eles são úteis para configurar o ambiente de teste e limpar recursos após a execução do teste.
```py
import unittest

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        # Configuração inicial
        self.x = 10
        self.y = 5

    def tearDown(self):
        # Limpeza após cada teste
        self.x = None
        self.y = None

    def test_add(self):
        result = self.x + self.y
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = self.x - self.y
        self.assertEqual(result, 5)
```

## Testes Parametrizados
Você pode usar o método `@unittest.parameterized`.parameterized para executar um teste com diferentes conjuntos de dados.
```py
import unittest
from parameterized import parameterized

class TestMathFunctions(unittest.TestCase):
    @parameterized.expand([
        (1, 1, 2),
        (2, 3, 5),
        (10, -5, 5),
    ])
    def test_add(self, x, y, expected):
        result = x + y
        self.assertEqual(result, expected)
```

## Mocks e Stubs
Você pode usar bibliotecas como `unittest.mock` para criar mocks e stubs, o que é útil para isolar o código em teste e simular o comportamento de dependências externas.
```py
import unittest
from unittest.mock import Mock

def do_something_with_dependency(dep):
    # Faz algo com a dependência
    return dep.get_value() * 2

class TestDependency(unittest.TestCase):
    def test_do_something_with_dependency(self):
        mock_dependency = Mock()
        mock_dependency.get_value.return_value = 10
        result = do_something_with_dependency(mock_dependency)
        self.assertEqual(result, 20)
```

## Execução Condicional de Testes
Você pode usar `@unittest.skip` para pular a execução de um teste.
```py
import unittest

class TestMathFunctions(unittest.TestCase):
    @unittest.skip("Exemplo de teste pulado")
    def test_add(self):
        result = 1 + 2
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = 5 - 2
        self.assertEqual(result, 3)
```
`@unittest.skipIf()` e `@unittest.skipUnless()` são usados para pular a execução do teste com base em condições específicas.

`@unittest.skipIf()`: Pula a execução de um teste se uma condição específica for verdadeira.
```py
import unittest
import sys

class TestMathFunctions(unittest.TestCase):
    @unittest.skipIf(sys.platform.startswith('win'), "Não suportado no Windows")
    def test_linux_only_feature(self):
        # Teste para uma funcionalidade que só é suportada no Linux
        self.assertTrue(True)
```
`@unittest.skipUnless()`: Pula a execução de um teste a menos que uma condição específica seja verdadeira
```py
import unittest
import os

class TestMathFunctions(unittest.TestCase):
    @unittest.skipUnless(os.getenv('CI') == 'true', "Este teste só deve ser executado em ambientes de CI")
    def test_ci_environment_only(self):
        # Teste que deve ser executado apenas em ambientes de integração contínua
        self.assertTrue(True)
```

## Asserts

1. `assertEqual(a, b)`: Verifica se `a` é igual a `b`.
2. `assertNotEqual(a, b)`: Verifica se `a` não é igual a `b`.
3. `assertTrue(expr)`: Verifica se `expr` é verdadeiro.
4. `assertFalse(expr)`: Verifica se `expr` é falso.
5. `assertIs(a, b)`: Verifica se `a` é o mesmo objeto que `b`.
6. `assertIsNot(a, b)`: Verifica se `a` não é o mesmo objeto que `b`.
7. `assertIsNone(expr)`: Verifica se `expr` é `None`.
8. `assertIsNotNone(expr)`: Verifica se `expr` não é `None`.
9. `assertIn(a, b)`: Verifica se `a` está contido em `b`.
10. `assertNotIn(a, b)`: Verifica se `a` não está contido em `b`.
11. `assertIsInstance(obj, cls)`: Verifica se `obj` é uma instância de `cls`.
12. `assertNotIsInstance(obj, cls)`: Verifica se `obj` não é uma instância de `cls`.
13. `assertAlmostEqual(a, b)`: Verifica se `a` é aproximadamente igual a `b`. Útil para números de ponto flutuante.
14. `assertNotAlmostEqual(a, b)`: Verifica se `a` não é aproximadamente igual a `b`.
15. `assertGreater(a, b)`: Verifica se `a` é maior que `b`.
16. `assertGreaterEqual(a, b)`: Verifica se `a` é maior ou igual a `b`.
17. `assertLess(a, b)`: Verifica se `a` é menor que `b`.
18. `assertLessEqual(a, b)`: Verifica se `a` é menor ou igual a `b`.
19. `assertRegex(s, regex)`: Verifica se a string `s` corresponde à expressão regular `regex`.
20. `assertNotRegex(s, regex)`: Verifica se a string `s` não corresponde à expressão regular `regex`.
21. `assertCountEqual(a, b)`: Verifica se `a` e `b` contêm os mesmos elementos, independentemente da ordem.
22. `assertMultiLineEqual(a, b)`: Verifica se `a` e `b` são iguais, mesmo se forem strings de várias linhas.


## Outros

### Integração com o Ecossistema Python
O `unittest` é parte integrante da biblioteca padrão do Python, o que significa que não requer instalação adicional e está prontamente disponível para qualquer projeto Python.

### Test Discovery
O `unittest` inclui um recurso de descoberta de testes, o que significa que você pode executar todos os testes em um diretório com um único comando. Isso é útil para projetos maiores com muitos testes.

### Integração com Outras Ferramentas:
O unittest se integra bem com outras ferramentas de teste e cobertura de código, como `coverage`, `pytest`, `nose`, entre outras, permitindo uma cobertura de teste eficaz e análise de cobertura de código.

- #### pytest
    O `unittest` pode ser facilmente integrado com o `pytest`, que é uma estrutura de teste mais flexível e poderosa. Você pode simplesmente executar o `pytest` em seu diretório de teste, e ele descobrirá e executará automaticamente todos os testes unittest presentes.Exemplo de comando para executar testes unittest com `pytest`:
    ```py
    pytest
    ```

- #### coverage
    O `coverage` é uma ferramenta para medir a cobertura de código em Python. Você pode usar o `coverage` junto com o unittest para medir a cobertura de código de seus testes.Exemplo de comando para executar testes unittest com `coverage`:
    ```py
    coverage run -m unittest discover
    ```
    Em seguida, você pode gerar relatórios de cobertura usando:
    ```py
    coverage report
    ```

- #### nose
    O `nose` é outro framework de teste popular para Python, que pode ser usado como uma alternativa ao `unittest`. Ele fornece recursos adicionais e pode ser mais conveniente para algumas situações.Exemplo de comando para executar testes `unittest` com `nose`:
    ```py
    nosetests
    ```

### Assertion Library Integrada
O `unittest` inclui um conjunto robusto de métodos de assert (como `assertEqual`, `assertTrue`, `assertFalse`, etc.) para verificar os resultados dos testes de forma clara e legível.

### Flexibilidade e Extensibilidade
Embora o `unittest` forneça uma estrutura básica para testes, ele também é flexível o suficiente para suportar práticas avançadas, como testes parametrizados, mocks e stubs, configuração e limpeza de testes, entre outros.

### Suporte a Plugins
Embora seja menos comum do que em outras ferramentas de teste como `pytest`, o `unittest` também oferece suporte a plugins que podem estender sua funcionalidade e permitir recursos adicionais, como relatórios personalizados, geração de dados de teste, etc.

Um exemplo de plugin para o unittest é o `unittest-xml-reporting`, que gera relatórios de teste no formato XML.

1. Primeiro, instale o pacote `unittest-xml-reporting` via pip:
    ```py
    pip install unittest-xml-reporting
    ```
2. Em seguida, você pode usar o plugin no seu script de teste `unittest`:
    ```py
    import unittest
    import xmlrunner

    class TestStringMethods(unittest.TestCase):
        def test_upper(self):
            self.assertEqual('hello'.upper(), 'HELLO')

        def test_isupper(self):
            self.assertTrue('HELLO'.isupper())
            self.assertFalse('Hello'.isupper())

    if __name__ == '__main__':
        # Indicando o diretório onde os relatórios XML serão salvos
        runner = xmlrunner.XMLTestRunner(output='test-reports')
        unittest.main(testRunner=runner)
    ```
    Neste exemplo, `xmlrunner.XMLTestRunner` é usado como o test runner para executar os testes e gerar relatórios no formato XML. O argumento `output` especifica o diretório onde os relatórios XML serão salvos.
3. Execute o script de teste como você faria normalmente. Os relatórios XML serão gerados no diretório especificado

# Funções Bot Discord
|Fun. Discord|Desc|Fun. Backend|Libs e APIs|Fun. Teste|Assert|
|:--:|:--:|:--:|:--:|:--:|:--:|
|/graph (function)|Gera gráficos de funções|validateFunction, defineDegree, pointsGen, graphGen| numpy, pyplot|testValidateFunction, testDefineDegree, testPointsGen, testGraphGen|assertIsNotNone, assertEquals, assertIn, assertIsInstance|
|/trigraph (sen\|cos\|tan)|Gera funções trigonométricas|pointsGen, graphGen|numpy, pyplot|testPointsGen, testGraphGen|assertIn, assertIsInstance|
|/dice|Gera 1 número aleatório (1-6)|roll|random|testDiceGenProbability, testDiceOutOfRange|assertGreater, assertIn|
|/currency (origin) (destiny)|Mostra a conversão de moedas (USD, BRL, EUR, JPY, CHF, BTC, ETH, USDC, SOL)|exchange||testOutput|assertRegex|

