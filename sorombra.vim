" File: sorombra.vim
" Maintainer: SrVariable
" License: MIT

if (!has("gui_running") && &t_Co < 256)
    finish
endif

if exists("syntax on")
    syntax reset
endif

let g:colors_name = "sorombra"

if &background == 'dark'
    hi Normal ctermbg=235 ctermfg=253 guibg=#222222 guifg=#dddddd
    hi ColorColumn cterm=NONE ctermbg=236 ctermfg=NONE guibg=#333333 guifg=NONE
    hi CursorColumn cterm=NONE ctermbg=236 ctermfg=NONE guibg=#333333 guifg=NONE
    hi CursorLine cterm=NONE ctermbg=236 ctermfg=NONE guibg=#333333 guifg=NONE
    hi Comment ctermfg=242 guifg=#666666
    hi Conceal ctermbg=235 ctermfg=253 guibg=#222222 guifg=#dddddd
    hi Constant cterm=italic ctermfg=253 guifg=#dddddd
    hi Boolean cterm=italic ctermfg=247 guifg=#999999
    hi Number cterm=italic ctermfg=247 guifg=#999999
    hi Cursor ctermbg=253 ctermfg=235 guibg=#dddddd guifg=#222222
    hi CursorLineNr cterm=bold ctermbg=236 ctermfg=221 guibg=#333333 guifg=#f2ca51
    hi Delimiter ctermfg=253 guifg=#dddddd
    hi DiffAdd ctermbg=77 ctermfg=235 guibg=#51f26c guifg=#222222
    hi DiffChange ctermbg=221 ctermfg=235 guibg=#f2ca51 guifg=#222222
    hi DiffDelete cterm=NONE ctermbg=203 ctermfg=253 guibg=#f25151 guifg=#dddddd
    hi DiffText cterm=NONE ctermbg=203 ctermfg=253 guibg=#f25151 guifg=#dddddd
    hi Directory ctermfg=75 guifg=#5194f2
    hi Error ctermbg=203 ctermfg=253 guibg=#f25151 guifg=#dddddd
    hi ErrorMsg ctermbg=203 ctermfg=253 guibg=#f25151 guifg=#dddddd
    hi WarningMsg ctermbg=221 ctermfg=235 guibg=#f2ca51 guifg=#222222
    hi EndOfBuffer ctermfg=242 guifg=#666666
    hi NonText ctermfg=242 guifg=#666666
    hi Function ctermfg=221 guifg=#f2ca51
    hi Identifier cterm=NONE ctermfg=221 guifg=#f2ca51
    hi Ignore ctermbg=NONE ctermfg=NONE guibg=NONE guifg=NONE
    hi IncSearch cterm=reverse ctermfg=NONE gui=reverse guifg=NONE term=reverse
    hi LineNr ctermbg=235 ctermfg=242 guibg=#222222 guifg=#666666
    hi MatchParen cterm=italic ctermbg=NONE ctermfg=203 guibg=NONE guifg=#f25151
    hi ModeMsg ctermfg=253 guifg=#dddddd
    hi MoreMsg ctermfg=253 guifg=#dddddd
    hi PreProc ctermfg=247 guifg=#999999
    hi Question ctermfg=77 guifg=#51f26c
    hi QuickFixLine ctermbg=215 ctermfg=235 guibg=#f29951 guifg=#222222
    hi Search ctermbg=221 ctermfg=235 guibg=#f2ca51 guifg=#222222
    hi Special ctermfg=75 guifg=#5194f2
    hi SpecialKey ctermfg=236 guifg=#333333
    hi Statement cterm=bold ctermfg=221 guifg=#f2ca51
    hi StatusLine cterm=reverse ctermbg=236 ctermfg=253 gui=reverse guibg=#333333 guifg=#dddddd term=reverse
    hi StatusLineTerm cterm=reverse ctermbg=236 ctermfg=253 gui=reverse guibg=#333333 guifg=#dddddd term=reverse
    hi StatusLineNC cterm=reverse ctermbg=235 ctermfg=253 gui=reverse guibg=#222222 guifg=#dddddd term=reverse
    hi StatusLineTermNC cterm=reverse ctermbg=235 ctermfg=253 gui=reverse guibg=#222222 guifg=#dddddd term=reverse
    hi StorageClass ctermfg=221 guifg=#f2ca51
    hi Tag cterm=italic ctermfg=50 guifg=#51f2d7
    hi Title cterm=underline ctermfg=50 gui=NONE guifg=#51f2d7
    hi Todo cterm=bold ctermbg=NONE ctermfg=203 guibg=NONE guifg=#f25151
    hi Type ctermfg=247 guifg=#999999
endif
