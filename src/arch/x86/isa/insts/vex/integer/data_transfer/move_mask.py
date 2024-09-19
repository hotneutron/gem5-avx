microcode = '''
def macroop VEX_VPMOVMSKB_R_XMM {
    gem5_avx_movemask_epi8 reg, xmmm, size=1, ext=XMM
};

def macroop VEX_VPMOVMSKB_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VPMOVMSKB_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VPMOVMSKB_R_YMM {
    gem5_avx_movemask_epi8 reg, ymmm, size=1, ext=YMM
};

def macroop VEX_VPMOVMSKB_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VPMOVMSKB_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

'''
