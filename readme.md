# Remover Fundo de Imagem

Este é um projeto simples em Python que permite aos usuários remover o fundo de imagens, utilizando a biblioteca **rembg** para realizar o processo de remoção. A interface gráfica foi criada com o **Tkinter**, permitindo que o usuário escolha facilmente a imagem e o diretório para salvar a imagem processada.

## Funcionalidades

- Permite escolher uma imagem do computador.
- Escolhe o diretório onde a imagem processada será salva.
- A imagem processada será salva com o nome do arquivo original seguido de `_removebg`.
- A interface exibe o status do processamento (concluído ou erro).

## Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Python 3.x
- `rembg` - para remover o fundo das imagens.
- `Pillow` - para manipulação de imagens.
- `Tkinter` - para a interface gráfica do usuário.

### Para instalar os requisitos e executar:

```bash
pip install rembg pillow
python removebg.py