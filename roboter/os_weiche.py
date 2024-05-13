import os
is_win_nt='yes_is_win_nt'
is_tux='yes_else_is_not_nt_assuming_tux'

def get_os():
    if os.name == 'nt':
        return is_win_nt
    else: 
        return is_tux
    
