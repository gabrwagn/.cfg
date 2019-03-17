""""""""""""""""""""""""""""""
" Vundle
""""""""""""""""""""""""""""""

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" " alternatively, pass a path where Vundle should install plugins
" "call vundle#begin('~/some/path/here')
"
" " let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-commentary'
Plugin 'Yggdroot/indentLine'
Plugin 'morhetz/gruvbox'
Plugin 'neovimhaskell/haskell-vim'
Plugin 'tmhedberg/SimpylFold'
" Plugin 'Valloric/YouCompleteMe'
Plugin 'tikhomirov/vim-glsl'

call vundle#end()            " required

"""" NERDTree
" Autostart NERDTree when no file spec
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" Open hotkey
map <C-n> :NERDTreeToggle<CR>

" Open in new tab automatically
let NERDTreeMapOpenInTab='\r'


""""""""""""""""""""""""""""""
" General                    
""""""""""""""""""""""""""""""

" Enable filetype plugins
filetype indent on
filetype plugin on
set encoding=utf-8

command W w !sudo tee % > /dev/null
command Wq wq

"""""""""""""""""""""""""""""
" Interface
"""""""""""""""""""""""""""""

" Backspace acts as it should
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

" Height of command bar
set cmdheight=2

" Ignore case when searching
set ignorecase

" Highlight search
set hlsearch

" Search like in modern browsers
set incsearch

" Show matching brackets when text indicator is over them
set showmatch

" Disable error sounds
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" Add a bit of extra margin to the left
set foldcolumn=1

" Show line numbers
set number

"""""""""""""""""""""""""""""
" Colors and fonts
"""""""""""""""""""""""""""""

" Enable syntax highlighting
syntax enable
" Enable 256 colors
"
set t_Co=256

" Colorscheme
set background=dark
colorscheme gruvbox-custom
highlight Normal ctermfg=grey ctermbg=black


"""""""""""""""""""""""""""""
" Text, tab and indent
"""""""""""""""""""""""""""""

" Use spaces instead of tabs
set expandtab

" Be smart when using tabs
set smarttab

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4
" Remove 4 spaces on backspace after tab
set softtabstop=4

" Line break on 500 chars
set lbr
set tw=500

set ai " auto indent
set si " smart indent
set wrap "wrap lines

""""""""""""""""""""""""""""""
" Editing mappings
""""""""""""""""""""""""""""""
" for normal mode indent
nnoremap <S-Tab> <<
nnoremap <Tab> >>


" for visual mode indent
vnoremap <Tab> >gv
vnoremap <S-Tab> <gv

" for insert mode
inoremap <S-Tab> <C-d>

" switch tab using ctrl tab (does not work)
" noremap <C-Tab> gt

" Delete trailing white space on save, useful for some filetypes ;)
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun

if has("autocmd")
    autocmd BufWritePre *.txt,*.js,*.py,*.wiki,*.sh,*.coffee :call CleanExtraSpaces()
endif

""""""""""""""""""""""""""""""
" Airline
""""""""""""""""""""""""""""""

set guifont='~/.fonts/Powerline.ttf'
let g:airline_powerline_fonts=1
let g:airline_theme='powerlineish'
let g:airline_enable_branch=1
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"

""""""""""""""""""""""""""""""
" IndentLine
""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""
" SimplyFold
""""""""""""""""""""""""""""""
let g:SimplyFold_docstring_preview = 1



