# TucumaSoft 1.4

> **Versão**: 1.4

## Descrição

Projeto Django base para atividade prática do curso de versionemento de código.

## Pré-requisitos

- Python 3
- `venv` (já incluso no Python 3)
- Django

## Instalação e Configuração

1. **Crie um ambiente virtual**
   ```bash
   python3 -m venv .venv  # cria o virtualenv na pasta .venv
   ```

2. **Ative o ambiente virtual**
   - **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows PowerShell**:
     ```powershell
     .venv\Scripts\activate
     ```

3. **Instale as dependências**
   ```bash
   pip install Django
   ```

## Migrações do Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

## Executando o Servidor

```bash
python manage.py runserver
```

## Acesso

Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

## Versão

- **TucumaSoft**: 1.3
- Registre sua versão a partir dessa.

## Equipe

- **Nome da equipe**: Softlink
- **Tech Leader**: Gillane Rosas
- **Dev1**: Antônio Gabriel
- **Dev2**: Emilly Paixão
- **Dev3**: Márcio Jean

