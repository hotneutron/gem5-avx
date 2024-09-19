microcode = '''
def macroop EVEX_VRCP14PD_XMM_XMM {
    gem5_avx_rcp14_pd xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VRCP14PD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_rcp14_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VRCP14PD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_rcp14_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VRCP14PD_YMM_YMM {
    gem5_avx_rcp14_pd ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VRCP14PD_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_rcp14_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VRCP14PD_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_rcp14_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VRCP14PD_ZMM_ZMM {
    gem5_avx_rcp14_pd zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VRCP14PD_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_rcp14_pd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VRCP14PD_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_rcp14_pd zmm, uvec1, size=8, ext=ZMM
};

'''
