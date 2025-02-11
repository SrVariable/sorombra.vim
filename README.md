# sorombra.vim

## Description

Sorombra is a simple dark color scheme for Vim.

## Usage

Currently, the easiest way to install this theme (at least on Linux) is using the following commands:
```shell
mkdir -p ~/.vim/colors
curl https://raw.githubusercontent.com/SrVariable/sorombra.vim/refs/heads/main/sorombra.vim > ~/.vim/colors
```
Then in vim you just have to execute `:colorscheme sorombra`.

Additionally, if you want to set this color scheme by default, you can add `colorscheme sorombra` to your `.vimrc`.

## Modification

For simplicity, I created a [python script](https://github.com/SrVariable/sorombra.vim/blob/main/themegen.py) which acts as a "template" for the color scheme, allowing to easily modify the color scheme. The colors are located at the beginning of the file. Once you do the changes, execute the script and it will generate the color scheme.

## Preview

### termguicolors
![image](https://github.com/user-attachments/assets/ebd927e8-db3d-4121-8008-2de5bcefcf0b)

### notermguicolors (256 term colors)
![image](https://github.com/user-attachments/assets/e511bd1c-d651-43fd-b9a0-7ee297a89511)


You can check this test code in [here](https://gist.github.com/SrVariable/a8bf09fe8a679212e2f3e092bf3363b3).

> [!NOTE]
>
> The font used is IosevkaTerm Nerd Font

## References

- [iceberg.vim](https://github.com/cocopon/iceberg.vim)
- [Creating your lovely color scheme](https://speakerdeck.com/cocopon/creating-your-lovely-color-scheme)
- vim `:hi` and `:help hi` commands
- [grubber-darker-theme](https://github.com/rexim/gruber-darker-theme)
- [themedgehog](https://github.com/SrVariable/themedgehog)
