#!/usr/bin/python3

BLACK = {"cterm": "235", "gui": "#222222"}
WHITE = {"cterm": "253", "gui": "#dddddd"}
RED = {"cterm": "203", "gui": "#f25151"}
YELLOW = {"cterm": "221", "gui": "#f2ca51"}
ORANGE = {"cterm": "215", "gui": "#f29951"}
GREEN = {"cterm": "77", "gui": "#51f26c"}
CYAN = {"cterm": "50", "gui": "#51f2d7"}
BLUE = {"cterm": "75", "gui": "#5194f2"}
PURPLE = {"cterm": "141", "gui": "#aa85f2"}
PINK = {"cterm": "219", "gui": "#ffafff"} # currently unused
DARKGRAY = {"cterm": "236", "gui": "#333333"}
SHADOWGRAY = {"cterm": "238", "gui": "#4d4d4d"}
GRAY = {"cterm": "242", "gui": "#666666"}
LIGHTGRAY = {"cterm": "247", "gui": "#999999"}
SILVERGRAY = {"cterm": "250", "gui": "#b3b3b3"}

def header(filename: str = "generated.vim",
           maintainer: str = "SrVariable",
           license: str = "MIT") -> str:
    return f'''" File: {filename}
" Maintainer: {maintainer}
" License: {license}

'''

def init(filename: str = "generated.vim") -> str:
    return f'''if (!has("gui_running") && &t_Co < 256)
    finish
endif

if exists("syntax on")
    syntax reset
endif

let g:colors_name = "{filename[:-4]}"

'''

# General highlighting for dark theme, I might add specific highlighting
# for different filetypes in the future
def dark_general() -> str:
    return f'''hi Normal ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} guibg={BLACK["gui"]} guifg={WHITE["gui"]}
    hi ColorColumn cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi CursorColumn cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi CursorLine cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi Comment cterm=italic ctermfg={PURPLE["cterm"]} guifg={PURPLE["gui"]}
    hi Conceal ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} guibg={BLACK["gui"]} guifg={WHITE["gui"]}
    hi Constant cterm=italic ctermfg={WHITE["cterm"]} guifg={WHITE["gui"]}
    hi Boolean cterm=italic ctermfg={LIGHTGRAY["cterm"]} guifg={LIGHTGRAY["gui"]}
    hi Number cterm=italic ctermfg={LIGHTGRAY["cterm"]} guifg={LIGHTGRAY["gui"]}
    hi Cursor ctermbg={WHITE["cterm"]} ctermfg={BLACK["cterm"]} guibg={WHITE["gui"]} guifg={BLACK["gui"]}
    hi CursorLineNr cterm=bold ctermbg={DARKGRAY["cterm"]} ctermfg={YELLOW["cterm"]} guibg={DARKGRAY["gui"]} guifg={YELLOW["gui"]}
    hi Delimiter ctermfg={WHITE["cterm"]} guifg={WHITE["gui"]}
    hi DiffAdd ctermbg={GREEN["cterm"]} ctermfg={BLACK["cterm"]} guibg={GREEN["gui"]} guifg={BLACK["gui"]}
    hi DiffChange ctermbg={YELLOW["cterm"]} ctermfg={BLACK["cterm"]} guibg={YELLOW["gui"]} guifg={BLACK["gui"]}
    hi DiffDelete cterm=NONE ctermbg={RED["cterm"]} ctermfg={WHITE["cterm"]} guibg={RED["gui"]} guifg={WHITE["gui"]}
    hi DiffText cterm=NONE ctermbg={RED["cterm"]} ctermfg={WHITE["cterm"]} guibg={RED["gui"]} guifg={WHITE["gui"]}
    hi Directory ctermfg={BLUE["cterm"]} guifg={BLUE["gui"]}
    hi Error ctermbg={RED["cterm"]} ctermfg={WHITE["cterm"]} guibg={RED["gui"]} guifg={WHITE["gui"]}
    hi ErrorMsg ctermbg={RED["cterm"]} ctermfg={WHITE["cterm"]} guibg={RED["gui"]} guifg={WHITE["gui"]}
    hi WarningMsg ctermbg={YELLOW["cterm"]} ctermfg={BLACK["cterm"]} guibg={YELLOW["gui"]} guifg={BLACK["gui"]}
    hi EndOfBuffer ctermfg={GRAY["cterm"]} guifg={GRAY["gui"]}
    hi NonText ctermfg={GRAY["cterm"]} guifg={GRAY["gui"]}
    hi Function ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi Identifier cterm=NONE ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi Ignore ctermbg=NONE ctermfg=NONE guibg=NONE guifg=NONE
    hi IncSearch cterm=reverse ctermfg=NONE gui=reverse guifg=NONE term=reverse
    hi LineNr ctermbg={BLACK["cterm"]} ctermfg={GRAY["cterm"]} guibg={BLACK["gui"]} guifg={GRAY["gui"]}
    hi MatchParen cterm=italic ctermbg=NONE ctermfg={RED["cterm"]} guibg=NONE guifg={RED["gui"]}
    hi ModeMsg ctermfg={WHITE["cterm"]} guifg={WHITE["gui"]}
    hi MoreMsg ctermfg={WHITE["cterm"]} guifg={WHITE["gui"]}
    hi PreProc ctermfg={SILVERGRAY["cterm"]} guifg={SILVERGRAY["gui"]}
    hi Question ctermfg={GREEN["cterm"]} guifg={GREEN["gui"]}
    hi QuickFixLine ctermbg={ORANGE["cterm"]} ctermfg={BLACK["cterm"]} guibg={ORANGE["gui"]} guifg={BLACK["gui"]}
    hi Search ctermbg={YELLOW["cterm"]} ctermfg={BLACK["cterm"]} guibg={YELLOW["gui"]} guifg={BLACK["gui"]}
    hi Special cterm=italic ctermfg={BLUE["cterm"]} guifg={BLUE["gui"]}
    hi SpecialKey ctermfg={SHADOWGRAY["cterm"]} guifg={SHADOWGRAY["gui"]}
    hi Statement cterm=bold ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi StatusLine cterm=reverse ctermbg={DARKGRAY["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={DARKGRAY["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineTerm cterm=reverse ctermbg={DARKGRAY["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={DARKGRAY["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineNC cterm=reverse ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={BLACK["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineTermNC cterm=reverse ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={BLACK["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StorageClass ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi VertSplit ctermbg={DARKGRAY["cterm"]} ctermfg={DARKGRAY["cterm"]} guibg={DARKGRAY["gui"]} guifg={DARKGRAY["gui"]}
    hi Tag cterm=italic ctermfg={CYAN["cterm"]} guifg={CYAN["gui"]}
    hi Title cterm=bold ctermfg={WHITE["cterm"]} gui=NONE guifg={WHITE["gui"]}
    hi Todo cterm=bold ctermbg=NONE ctermfg={RED["cterm"]} guibg=NONE guifg={RED["gui"]}
    hi Type ctermfg={LIGHTGRAY["cterm"]} guifg={LIGHTGRAY["gui"]}
    hi Visual ctermbg={SHADOWGRAY["cterm"]} ctermfg=NONE guibg={SHADOWGRAY["gui"]} guifg=NONE
    hi Folded ctermbg={SHADOWGRAY["cterm"]} ctermfg=NONE guibg={SHADOWGRAY["gui"]} guifg=NONE
    hi FoldColumn ctermbg={SHADOWGRAY["cterm"]} ctermfg=NONE guibg={SHADOWGRAY["gui"]} guifg=NONE'''

def dark_makefile() -> str:
    return f'''hi link makeCommands Normal'''

def dark_sql() -> str:
    return f'''hi link sqlKeyword sqlStatement'''

# NOTE: Light is currently unsupported. I might support it in the future.
def color() -> str:
    return f'''if &background == \'dark\'
    {dark_general()}
    {dark_makefile()}
    {dark_sql()}
endif
'''

if __name__ == "__main__":
    filename = "sorombra.vim"
    with open(filename, "w") as f:
        f.write(header(filename = filename))
        f.write(init(filename))
        f.write(color())
