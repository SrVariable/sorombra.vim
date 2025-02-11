#!/usr/bin/python3

BLACK = {"cterm": "235", "gui": "#222222"}
WHITE = {"cterm": "253", "gui": "#dddddd"}
RED = {"cterm": "203", "gui": "#f25151"}
YELLOW = {"cterm": "221", "gui": "#f2ca51"}
ORANGE = {"cterm": "215", "gui": "#f29951"}
GREEN = {"cterm": "77", "gui": "#51f26c"}
CYAN = {"cterm": "50", "gui": "#51f2d7"}
BLUE = {"cterm": "75", "gui": "#5194f2"}
PURPLE = {"cterm": "99", "gui": "#8751f2"}
PINK = {"cterm": "206", "gui": "#f251e5"} # currently unused
DARKGRAY = {"cterm": "236", "gui": "#333333"}
GRAY = {"cterm": "242", "gui": "#666666"}
LIGHTGRAY = {"cterm": "247", "gui": "#999999"}

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

def dark() -> str:
    return f'''hi Normal ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} guibg={BLACK["gui"]} guifg={WHITE["gui"]}
    hi ColorColumn cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi CursorColumn cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi CursorLine cterm=NONE ctermbg={DARKGRAY["cterm"]} ctermfg=NONE guibg={DARKGRAY["gui"]} guifg=NONE
    hi Comment ctermfg={GRAY["cterm"]} guifg={GRAY["gui"]}
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
    hi PreProc ctermfg={LIGHTGRAY["cterm"]} guifg={LIGHTGRAY["gui"]}
    hi Question ctermfg={GREEN["cterm"]} guifg={GREEN["gui"]}
    hi QuickFixLine ctermbg={ORANGE["cterm"]} ctermfg={BLACK["cterm"]} guibg={ORANGE["gui"]} guifg={BLACK["gui"]}
    hi Search ctermbg={YELLOW["cterm"]} ctermfg={BLACK["cterm"]} guibg={YELLOW["gui"]} guifg={BLACK["gui"]}
    hi Special ctermfg={BLUE["cterm"]} guifg={BLUE["gui"]}
    hi SpecialKey ctermfg={DARKGRAY["cterm"]} guifg={DARKGRAY["gui"]}
    hi Statement cterm=bold ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi StatusLine cterm=reverse ctermbg={DARKGRAY["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={DARKGRAY["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineTerm cterm=reverse ctermbg={DARKGRAY["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={DARKGRAY["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineNC cterm=reverse ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={BLACK["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StatusLineTermNC cterm=reverse ctermbg={BLACK["cterm"]} ctermfg={WHITE["cterm"]} gui=reverse guibg={BLACK["gui"]} guifg={WHITE["gui"]} term=reverse
    hi StorageClass ctermfg={YELLOW["cterm"]} guifg={YELLOW["gui"]}
    hi Tag cterm=italic ctermfg={CYAN["cterm"]} guifg={CYAN["gui"]}
    hi Title cterm=underline ctermfg={CYAN["cterm"]} gui=NONE guifg={CYAN["gui"]}
    hi Todo cterm=bold ctermbg=NONE ctermfg={RED["cterm"]} guibg=NONE guifg={RED["gui"]}
    hi Type ctermfg={LIGHTGRAY["cterm"]} guifg={LIGHTGRAY["gui"]}'''

# NOTE: Light is currently unsupported. I might support it in the future.
def color() -> str:
    return f'''if &background == \'dark\'
    {dark()}
endif
'''

if __name__ == "__main__":
    filename = "sorombra.vim"
    with open(filename, "w") as f:
        f.write(header(filename = filename))
        f.write(init(filename))
        f.write(color())
