microcode = '''
def macroop EVEX_VMOVDDUP_XMM_XMM {
    gem5_avx_movedup_pd xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVDDUP_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_movedup_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VMOVDDUP_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_movedup_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VMOVDDUP_YMM_YMM {
    gem5_avx_movedup_pd ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVDDUP_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_movedup_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VMOVDDUP_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_movedup_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VMOVDDUP_ZMM_ZMM {
    gem5_avx_movedup_pd zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVDDUP_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_movedup_pd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VMOVDDUP_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_movedup_pd zmm, uvec1, size=8, ext=ZMM
};

# EVEX_VMOVSLDUP
def macroop EVEX_VMOVSLDUP_XMM_XMM {
    gem5_avx_moveldup_ps xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVSLDUP_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_moveldup_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VMOVSLDUP_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_moveldup_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VMOVSLDUP_YMM_YMM {
    gem5_avx_moveldup_ps ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVSLDUP_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_moveldup_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VMOVSLDUP_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_moveldup_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VMOVSLDUP_ZMM_ZMM {
    gem5_avx_moveldup_ps zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVSLDUP_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_moveldup_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VMOVSLDUP_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_moveldup_ps zmm, uvec1, size=4, ext=ZMM
};

# EVEX_VMOVSHDUP
def macroop EVEX_VMOVSHDUP_XMM_XMM {
    gem5_avx_movehdup_ps xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVSHDUP_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_movehdup_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VMOVSHDUP_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_movehdup_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VMOVSHDUP_YMM_YMM {
    gem5_avx_movehdup_ps ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVSHDUP_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_movehdup_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VMOVSHDUP_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_movehdup_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VMOVSHDUP_ZMM_ZMM {
    gem5_avx_movehdup_ps zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVSHDUP_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_movehdup_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VMOVSHDUP_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_movehdup_ps zmm, uvec1, size=4, ext=ZMM
};

'''
