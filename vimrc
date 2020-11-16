
set background=dark
colorscheme PaperColor

execute pathogen#infect()
filetype plugin indent on

" show line number
set nu!

" set windows size
set lines=30 
set columns=110

" setup linespace
set linespace=4

" highlight the syntax
syntax on

" Set font and size
set guifont=Roboto\ Mono\ for\ Powerline\ 16

" Turn off the menu bar
set guioptions-=m

" Turn off the tool bar
set guioptions-=T

" Turn off the scroll bar
set guioptions-=L
set guioptions-=r
" set guioptions-=b

" this is a smart autoindent, for all program languages
" set smartindent

" use the same indent as previous line for new line
" set autoindent

" setting the width unit for << and >> operation
set shiftwidth=4

" change the width of one tab, instead of tagstop=4
set softtabstop=4

" configure the NERDTree to F3
map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>

" configure the Tagbar to F8
map <F4> :TagbarToggle<CR>

" airline configure
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline#extensions#tabline#formatter = 'default'
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
" https://github.com/vim-airline/vim-airline-themes/wiki/Screenshots
let g:airline_theme = 'bubblegum'

" tmuxline configure
let g:tmuxline_powerline_separators = 0

" verilog_systemverilog configure
set foldmethod=syntax
let g:SuperTabDefaultCompletionType = 'context'
let mapleader=','
nnoremap <leader>i :VerilogFollowInstance<CR>
nnoremap <leader>p :VerilogFollowPort<CR>
nnoremap <leader>u :VerilogGotoInstanceStart<CR>

" enable the mouse operation
set mouse=a

" set ctags
set tags=tags,../tags,../../tags,../../../tags,../../../../tags,../../../../../tags,../../../../../../tags

" enable F5 to execute program
map <F5> :call CompileRunGcc()<CR>
    func! CompileRunGcc()
        exec "w"
	let file_ext = expand("%:e")
if &filetype == 'c'
            exec "!g++ % -o %<"
            exec "!time ./%<"
elseif &filetype == 'cpp'
            exec "!g++ % -o %<"
            exec "!time ./%<"
elseif &filetype == 'java'
            exec "!javac %"
            exec "!time java %<"
elseif &filetype == 'sh'
            exec "!time bash %"
elseif &filetype == 'python'
            exec "!time python3 %"
elseif &filetype == 'perl'
            exec "!perl %"
elseif &filetype == 'html'
            exec "!firefox % &"
elseif &filetype == 'mkd'
            exec "!~/.vim/markdown.pl % > %.html &"
            exec "!firefox %.html &"
endif
    endfunc

iab funcdec # =====================================================<Enter># Function    : <Enter># Description : <Enter># =====================================================
iab cccc # ---------------------------------------------------
iab tttt # ================================================================
