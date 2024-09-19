microcode = '''
def macroop EVEX_VPMOVB2M_K_XMM {
    gem5_evex_movepi8 k, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPMOVB2M_K_YMM {
    gem5_evex_movepi8 k, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPMOVB2M_K_ZMM {
    gem5_evex_movepi8 k, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPMOVW2M_K_XMM {
    gem5_evex_movepi16 k, xmmm, size=2, ext=XMM
};

def macroop EVEX_VPMOVW2M_K_YMM {
    gem5_evex_movepi16 k, ymmm, size=2, ext=YMM
};

def macroop EVEX_VPMOVW2M_K_ZMM {
    gem5_evex_movepi16 k, zmmm, size=2, ext=ZMM
};

def macroop EVEX_VPMOVD2M_K_XMM {
    gem5_evex_movepi32 k, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPMOVD2M_K_YMM {
    gem5_evex_movepi32 k, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPMOVD2M_K_ZMM {
    gem5_evex_movepi32 k, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPMOVQ2M_K_XMM {
    gem5_evex_movepi64 k, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPMOVQ2M_K_YMM {
    gem5_evex_movepi64 k, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPMOVQ2M_K_ZMM {
    gem5_evex_movepi64 k, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPMOVM2B_XMM_K {
    gem5_evex_movm_epi8 xmm, km, size=1, ext=XMM
};

def macroop EVEX_VPMOVM2B_YMM_K {
    gem5_evex_movm_epi8 ymm, km, size=1, ext=YMM
};

def macroop EVEX_VPMOVM2B_ZMM_K {
    gem5_evex_movm_epi8 zmm, km, size=1, ext=ZMM
};

def macroop EVEX_VPMOVM2W_XMM_K {
    gem5_evex_movm_epi16 xmm, km, size=2, ext=XMM
};

def macroop EVEX_VPMOVM2W_YMM_K {
    gem5_evex_movm_epi16 ymm, km, size=2, ext=YMM
};

def macroop EVEX_VPMOVM2W_ZMM_K {
    gem5_evex_movm_epi16 zmm, km, size=2, ext=ZMM
};

def macroop EVEX_VPMOVM2D_XMM_K {
    gem5_evex_movm_epi32 xmm, km, size=4, ext=XMM
};

def macroop EVEX_VPMOVM2D_YMM_K {
    gem5_evex_movm_epi32 ymm, km, size=4, ext=YMM
};

def macroop EVEX_VPMOVM2D_ZMM_K {
    gem5_evex_movm_epi32 zmm, km, size=4, ext=ZMM
};

def macroop EVEX_VPMOVM2Q_XMM_K {
    gem5_evex_movm_epi64 xmm, km, size=8, ext=XMM
};

def macroop EVEX_VPMOVM2Q_YMM_K {
    gem5_evex_movm_epi64 ymm, km, size=8, ext=YMM
};

def macroop EVEX_VPMOVM2Q_ZMM_K {
    gem5_evex_movm_epi64 zmm, km, size=8, ext=ZMM
};

def macroop EVEX_VPMOVB2M_K_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVB2M_K_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVW2M_K_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVW2M_K_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVD2M_K_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVD2M_K_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVQ2M_K_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VPMOVQ2M_K_P {
    fault "std::make_shared<UnimpInstFault>()"
};

'''
